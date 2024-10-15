import os
import sys

def platform():
    if not os.path.exists('system'):
        print('\n\n1 = Windows')
        print('2 = Linux')

        system = input('Введите название вашей операционной системы - ')
        
        if system == '1':
            with open('system','w') as fp:
                fp.write('Windows')
        
        elif system == '2':
            with open('system','w') as fp:
                fp.write('Linux')
        
        else:
            print('\n\n------------------------------------------')
            print('Неизвестная операционная система')
            print('------------------------------------------')

            input('\n\nДля продолжения нажмите Enter')
            sys.exit()

    else:
        print('file "system" exist')


def directory_program():
    if not os.path.exists('directory_to_program'):
        directory_program = input('Введите директорию программы(заканчивать на /) - ')
        with open('directory_to_program','w') as fp:
            fp.write(directory_program)

    else:
        print('file "directory_to_program" exist')