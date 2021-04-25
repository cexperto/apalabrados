# receive data
# define function
# identify number, text or character
# try validate data
# design database and connect DB
# from sqlalchemy import *
# from config import host, port, database, user, password

# conn_str = f'postgresql://{user}:{password}@{host}/{database}'
# engine = create_engine(conn_str)
# connection = engine.connect()
# metadata = MetaData()

user = input('please enter a number or text')
def run(user):
    try:
        float(user)
        return print('is a number')
    # if type(input)== int and type(input)== float:
    #     return print('is a number')
    except:
        if type(user)== str:
            # print('text')
             
            characters = list(filter(lambda c: c in '@´´-+*\^{}[]_.,;:/#$%&()=¿?¡!áéíóú', user ))
            if len(characters)>0:
                # print(characters)
                for items in characters:
                    print(items)
            else:
                print('is a text')
                first = user[0]
                print(first)                
                long = len(user)
                int(long)
                last = user[long-1]
                print(last)      
    

if __name__ == '__main__':
    run(user)