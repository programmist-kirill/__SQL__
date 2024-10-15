import os
import time

with open('system','r') as file:
    system = file.read().strip('\n')

class new_file:

    def preparation_database_and_file_windows(name_basedata):
        os.system('rename + ' + name_basedata + '.zip' + ' ' + name_basedata + '.db')
        os.system('rmdir ' + name_basedata)
        os.system('delete script.sh')
    
    def preparation_database_and_file_linux(name_basedata):
        os.system('mv ' + name_basedata + '.zip' + ' ' + name_basedata + '.db')
        #os.system('rm -rf ' + name_basedata)
        os.system('rm -rf system.sh')

class edit_file:

    def preparation_database_and_file_windows(name_basedata):
        os.system('rename + ' + name_basedata + '.db' + ' ' + name_basedata + '.zip')
    
    def preparation_database_and_file_linux(name_basedata):
        os.system('mv ' + name_basedata + '.db' + ' ' + name_basedata + '.zip')
    
    def preparation_and_start_script_linux():
        os.system('sudo chmod +x "./script.sh"')
        os.system('"./script.sh"')

    def preparation_script_windows():
        print('Подготовка скрипта')
        time.sleep(0.1)