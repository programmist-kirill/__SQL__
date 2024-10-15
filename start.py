import os
import sys

sys.path.append('7zip/')
import core_zip

with open('directory_to_program','r') as file:
    directory_to_program = file.read().strip('\n')

directory_to_archive = 'user.zip'
directory_to_extract = directory_to_program
directory_create_is_script = 'abc'

core_zip.extract.write_no_password(directory_to_archive, directory_to_extract, directory_create_is_script)

os.system('sudo chmod +x "./script.sh"')
os.system('"./script.sh"')