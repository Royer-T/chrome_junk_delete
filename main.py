import logging

#  import packages (modules/classes)
from junk_delete.deletion import Junkdelete

# constants
import constants

#  create and configure logger
log_file = constants.LOG_FILE
log_path = f'{constants.LOGDIRECTORY}/{log_file}'

logging.basicConfig(filename=log_path,
                    level=logging.DEBUG,
                    filemode='a',
                    force=True,
                    format='%(asctime)s - %(levelname)s - '
                           '%(name)s:%(message)s')


def delete_folders(junk_delete_obj, substring):
    """
    Deletes folders containing the specified substring.

    Args:
        junk_delete_obj (Junkdelete): An instance of the Junkdelete class.
        substring (str): The substring to search for in folder names.

    Returns:
        None
    """
    junk_delete_obj.delete_folders_with_substring(substring)


def main():
    """
   Main function that performs folder deletion tasks.

   Returns:
       None
   """
    # 1. delete from C:\Program Files (x86)
    x86 = Junkdelete(constants.INX86)
    delete_folders(x86, 'scoped_dir')

    # 2. delete from C:\Program Files
    program = Junkdelete(constants.INPROGRAM)
    delete_folders(program, 'chrome_BITS_')
    delete_folders(program, 'chrome_ComponentUnpacker_BeginUnzipping')
    delete_folders(program, 'chrome_url_fetcher_')


if __name__ == '__main__':
    main()
