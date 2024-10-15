class archiving:
    #7z a -tzip -mx5 -r0 c:\temp\archive.zip c:\temp

    def write_is_password(password , what_is_name_archive , directory_to_file_or_folder , compression_ratio , directory_create_is_script):

        if directory_create_is_script == 'abc':
            with open('script.sh','w') as fp:
                commande = '7zz a -tzip -ssw -mx' + compression_ratio + ' -p' + password + ' ' + what_is_name_archive + ' ' + directory_to_file_or_folder
                fp.write(commande)

        else:
            with open(directory_create_is_script + '/script.sh','w') as fp:
                commande = '7zz a -tzip -ssw -mx' + compression_ratio + ' -p' + password + ' ' + what_is_name_archive + ' ' + directory_to_file_or_folder
                fp.write(commande)

    def write_no_password(what_is_name_archive , directory_to_file_or_folder , compression_ratio , directory_create_is_script):

        if directory_create_is_script == 'abc':
            with open('script.sh','w') as fp:
                commande = '7zz a -tzip -ssw -mx' + compression_ratio + ' ' + what_is_name_archive + ' ' + directory_to_file_or_folder
                fp.write(commande)

        else:
            with open(directory_create_is_script + '/script.sh','w') as fp:
                commande = '7zz a -tzip -ssw -mx' + compression_ratio + ' ' + what_is_name_archive + ' ' + directory_to_file_or_folder
                fp.write(commande)


class extract:
    #7z x c:\temp\archive.7z -o"c:\temp\"
    def write_is_password(password , directory_to_archive , directory_to_extract , directory_create_is_script):

        if directory_create_is_script == 'abc':
            with open('script.sh','w') as fp:
                commande = '7zz x -p' + password + ' ' + directory_to_archive + ' -o' + directory_to_extract
                fp.write(commande)

        else:
            with open(directory_create_is_script + '/script.sh','w') as fp:
                commande = '7zz x -p' + password + ' ' + directory_to_archive + ' -o' + directory_to_extract
                fp.write(commande)
    

    def write_no_password(directory_to_archive , directory_to_extract , directory_create_is_script):
    
        if directory_create_is_script == 'abc':
            with open('script.sh','w') as fp:
                commande = '7zz x ' + directory_to_archive + ' -o' + directory_to_extract
                fp.write(commande)

        else:
            with open(directory_create_is_script + '/script.sh','w') as fp:
                commande = '7zz x ' + directory_to_archive + ' -o' + directory_to_extract
                fp.write(commande)