from sqlalchemy import *
from config import host, port, database, user, password

conn_str = f'postgresql://{user}:{password}@{host}/{database}'
engine = create_engine(conn_str)
connection = engine.connect()
metadata = MetaData()
numbers = Table('numbers', metadata,
   Column('id_n', Integer, primary_key=True),
   Column('number', Integer, nullable=False),
   Column('accumulated', Integer, nullable=False)
)
texts = Table('texts', metadata,
   Column('id_t', Integer, primary_key=True),
   Column('texts', String (255) , nullable=False),
   Column('initial', String (255), nullable=False),
   Column('end', String (255), nullable=False)
)
characters = Table('characters', metadata,
   Column('id_c', Integer, primary_key=True),   
   Column('character', String (255), nullable=False)
)
metadata.create_all(engine)
# query = insert(numbers).values(number=123, accumulated=1)
# ResultProxy = connection.execute(query)

