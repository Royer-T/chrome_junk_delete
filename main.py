import logging

#  import packages (modules/classes)
import junk_delete

# constants
import constants

#  create and configure logger
log_file = constants.LOG_FILE

logging.basicConfig(filename=f'{constants.LOGDIRECTORY}/{log_file}',
                    level=logging.DEBUG,
                    filemode='a',
                    force=True,
                    format='%(asctime)s - %(levelname)s - %(name)s:'
                           '%(message)s')

# 1. delete from C:\Program Files (x86)
# creating an object of the class, this invokes a parameterized constructor
x86 = junk_delete.deletion.Junkdelete(constants.INX86)

# 1.1 delete folders containing 'scoped_dir'
x86.delete_folders_with_substring('scoped_dir')

# 2. delete from C:\Program Files
# creating an object of the class, this invokes a parameterized constructor
program = junk_delete.deletion.Junkdelete(constants.INPROGRAM)

# 2.1 delete folders containing:
program.delete_folders_with_substring('chrome_BITS_')
program.delete_folders_with_substring('chrome_ComponentUnpacker_BeginUnzipping')
program.delete_folders_with_substring('chrome_url_fetcher_')
