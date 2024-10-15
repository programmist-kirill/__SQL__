import os
import sys

import create_database
import __init__
import rename

sys.path.append('7zip/')
import core_zip

class action_element:
    def new_file(name_element, value_element, name_basedata):

        with open('system','r') as file:
            system = file.read().strip('\n')

        if os.path.exists(name_basedata):
            print('')
        else:
            create_database.main(name_basedata)

        with open(name_basedata + "/" + name_element, 'w') as fp:
            fp.write(value_element)

        #архивация базы данных с элементом
        core_zip.archiving.write_no_password(name_basedata + '.zip' , name_basedata + "/" + name_element , '1', 'abc')
        rename.edit_file.preparation_and_start_script_linux()

        if system == 'Windows':
            rename.new_file.preparation_database_and_file_windows(name_basedata)
        
        elif system == 'Linux':
            rename.new_file.preparation_database_and_file_linux(name_basedata)

    def edit_file(name_element, value_element , name_basedata):
        
        with open('system','r') as file:
            system = file.read().strip('\n')

        if system == 'Windows':
            os.system('rename ' + name_basedata + '.db' + ' ' + name_basedata + '.zip')
        
        if system == 'Linux':
            os.system('mv ' + name_basedata + '.db' + ' ' + name_basedata + '.zip')

        with open('directory_to_program','r') as file:
            directory_to_program = file.read().strip('\n')

        directory_to_archive = name_basedata + '.zip'
        directory_to_extract = directory_to_program + "/"
        directory_create_is_script = 'abc'

        core_zip.extract.write_no_password(directory_to_archive, directory_to_extract, directory_create_is_script)

        rename.edit_file.preparation_and_start_script_linux()

        if os.path.exists(name_basedata + '/' + name_element):
            with open(name_basedata + '/' + name_element, 'w') as fp:
                fp.write(value_element)

            os.system('rm -rf user.zip')

            directory_to_file_or_folder = name_basedata
            what_is_name_archive = directory_to_program + "/" + name_basedata
            compression_ratio = '1'
            directory_create_is_script = 'abc'
            core_zip.archiving.write_no_password(directory_to_file_or_folder , what_is_name_archive , compression_ratio , directory_create_is_script)

            rename.edit_file.preparation_and_start_script_linux()
            rename.new_file.preparation_database_and_file_linux(name_basedata)
        else:
            print('\n\n\n----------------------------------------------------')
            print(f'Запись {name_element} не найдена в базе данных.')
            print('----------------------------------------------------')
            

    def delete_file(name_element , name_basedata):
        
        with open('directory_to_program','r') as file:
            directory_to_program = file.read().strip('\n')

        rename.edit_file.preparation_database_and_file_linux(name_basedata)
        print('\n\n\n\nrename.edit.file')

        directory_to_archive = name_basedata + '.zip'
        directory_to_extract = directory_to_program
        directory_create_is_script = 'abc'
        core_zip.extract.write_no_password(directory_to_archive , directory_to_extract , directory_create_is_script)
        print('core_zip.extract')

        rename.edit_file.preparation_and_start_script_linux()


        directory_for_delete = name_basedata + '/' + name_element
        os.remove(directory_for_delete)
        print('os.remove')

        os.remove(name_basedata + '.zip')

        what_is_name_archive = name_basedata + '.zip'
        directory_to_file_or_folder = name_basedata + '/'
        compression_ratio = '1'
        directory_create_is_script = 'abc'
        core_zip.archiving.write_no_password(what_is_name_archive , directory_to_file_or_folder , compression_ratio , directory_create_is_script)
        print('core_zip.archiving')

        rename.edit_file.preparation_and_start_script_linux()
        print('rename.edit_file')
        rename.new_file.preparation_database_and_file_linux(name_basedata)
        print('rename.new_file')
class init:
    def main():
        __init__.platform()
        __init__.directory_program()
        
        print('\n\n1 = новый элемент')
        print('2 = изменить элемент')
        print('3 = удалить запись')
        action = input('что вы хотите сделать - ')
        if action == '1':
            name_element = input('Введите название элемента - ')
            value_element = input('Введите значение или содержание записи - ')
            name_basedata = input('Введите название базы данных - ')
            
            action_element.new_file(name_element, value_element,name_basedata)
        
        elif action == '2':
            name_element = input('Введите название элемента - ')
            value_element = input('Введите новое значение или новое содержание записи - ')
            name_basedata = input('Введите название базы данных - ')
            action_element.edit_file(name_element, value_element, name_basedata)
        
        elif action == '3':
            name_element = input('Введите название элемента - ')
            name_basedata = input('Введите название базы данных - ')
            action_element.delete_file(name_element, name_basedata)

        else:
            print('\n\n\n----------------------------------------------------')
            print('Неправильный ввод.')
            print('----------------------------------------------------')
init.main()