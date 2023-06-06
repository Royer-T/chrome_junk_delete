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
        recursive folder deletion (using administrator privileges) of folders
        containing a substring in their folder name from a targeted directory

        :parameter: root folder to search (string)
        :parameter: substring being searched for (string)
        :return: Nothing
        """
        instances = 0

        for root, dirs, files in os.walk(self.path, topdown=False):
            for dir_name in dirs:
                if substring in dir_name:
                    # folder may need to administrator permission to delete
                    folder_path = os.path.join(self.path, dir_name)

                    try:
                        # Check if the current user has admin permissions
                        if not os.access(folder_path, os.W_OK):
                            # request admin permissions
                            params = f'/C takeown /F "{folder_path}" /R /D Y ' \
                                     f'&& icacls "{folder_path}" /grant:r ' \
                                     f'{os.getlogin()}:F /T && rmdir /S /Q "{folder_path}"'
                            os.system(f'cmd.exe {params}')

                            instances = instances + 1
                        else:
                            # admin permissions are already granted, delete the folder
                            shutil.rmtree(folder_path)

                            instances = instances + 1

                    except Exception as e:
                        logger.info(f'{folder_path} could not be deleted '
                                    f'because of administrator permission '
                                    f'problem')
                        logger.info(f'{folder_path} has an "{e}" problem')

        logger.info(f"{instances} folders were automatically from: {self.path} "
                    f"containing the '{substring}' substring")

        return None
