# receive data
# define function
# identify number, text or character
# try validate data
# design database and connect DB
# from sqlalchemy import *
# from config import host, port, database, user, password


from create_table import *
from sqlalchemy import *
user = input('Please enter a number or text: ')
def run(user):
    try:
        float(user)        
        query_acumulated= connection.execute('SELECT COUNT(id_n)+1 FROM numbers')
        for row in query_acumulated:
            data = row[0]     
        # print(data)
        query = insert(numbers).values(number=user, accumulated=data)
        ResultProxy = connection.execute(query)
        return print('is a number')
    # if type(input)== int and type(input)== float:
    #     return print('is a number')
    except:
        if type(user)== str:
            # print('text')

            character_list = list(filter(lambda c: c in '@´´-+*\^{}[]_.,;:/#$%&()=¿?¡!áéíóú', user ))
            if len(character_list)>0:
                # print(characters)
                arr_characters = [] 
                for items in character_list:
                    arr_characters.append(items)
                    # print(characters)
                print(arr_characters)
                ls_character = "".join(map(str, arr_characters))
                print(ls_character)
                query = insert(characters).values(character=ls_character)
                ResultProxy = connection.execute(query)
                return print('text with special character')
            else:
                first = user[0]
                # print(first)
                long = len(user)
                int(long)
                last = user[long-1]
                # print(last)
                query = insert(texts).values(texts=user,initial=first,end=last)
                ResultProxy = connection.execute(query)
                print('is a text')


if __name__ == '__main__':
    run(user)