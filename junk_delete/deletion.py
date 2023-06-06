import os
import logging
import shutil

#  set the logging behaviour
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s '
                                               '- %(name)s:%(message)s')
logger = logging.getLogger(__name__)


class Junkdelete:
    def __init__(self, path):
        self.path = path

    def delete_folders_with_substring(self, substring):
        """
        Deletes folders within the specified path that contain the given
        substring.

        Args:
            substring (str): The substring to search for in folder names.

        Returns:
            None

        Raises:
            OSError: If there is an error accessing or deleting the folders.

        Notes:
            This method recursively searches for folders within the specified
            path and deletes those whose names contain the specified substring.
            If the current user does not have administrator permissions, an
            attempt will be made to request and acquire the necessary
            permissions before deleting the folder. If the permissions cannot
            be obtained, the folder will be logged as unable to delete due to
            administrator permission problems.

            If the current user already has administrator permissions, the
            folder will be deleted directly without requesting additional
            permissions.

            The method logs the number of folders deleted and the path from
            which they were deleted, along with the provided substring.
        """
        instances = 0

        for root, dirs, files in os.walk(self.path, topdown=False):
            for dir_name in dirs:
                if substring in dir_name:
                    folder_path = os.path.join(self.path, dir_name)
                    try:
                        if not os.access(folder_path, os.W_OK):
                            # Request admin permissions using command prompt
                            params = f'/C takeown /F "{folder_path}" /R /D Y ' \
                                     f'&& icacls "{folder_path}" /grant:r ' \
                                     f'{os.getlogin()}:F /T && rmdir /S /Q "{folder_path}"'
                            os.system(f'cmd.exe {params}')
                        else:
                            # Delete the folder directly
                            shutil.rmtree(folder_path)
                        instances += 1
                    except Exception as e:
                        logger.info(f'{folder_path} could not be deleted '
                                    f'because of an administrator permission '
                                    f'problem')
                        logger.info(f'{folder_path} has an "{e}" problem')

        logger.info(f"{instances} folders were automatically deleted from: "
                    f"{self.path} containing the '{substring}' substring")

        return None
