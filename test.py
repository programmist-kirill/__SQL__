import main

name_element = input('name_element = ')
name_basedata = input('name_basedata = ')

main.action_element.delete_file(name_element,name_basedata)

action = input('okay or none = ')
if action == 'y':
    main.action_element.two_delete_File(name_element,name_basedata)
if action == 'n':
    print('error test.py')