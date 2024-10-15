import os

def main(name_database):
    if not os.path.exists(name_database):
        os.mkdir(name_database)
    else:
        print(f'База данных {name_database} уже существует.')