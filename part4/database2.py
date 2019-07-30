# importing the necessary module
from sqlalchemy import create_engine, MetaData
from sqlalchemy import insert, Table, Column
from sqlalchemy import Integer, Float, String, Boolean

# creating the database
engine = create_engine("sqlite:///data1.sqlite")
connection = engine.connect()
metadata = MetaData()

# defining the table
data1 = Table('data1', metadata,
              Column('name', String(250), unique=True),
              Column('count', Integer(), default=1),
              Column('amount', Float()),
              Column('valid', Boolean, default=False)
              )
metadata.create_all(engine)
# print(engine.table_names())

# inserting multiple values into the table
values_list = [
    {"name": "Anna", "count": 1, "amount": 1000.00, "valid": True},
    {"name": "Taylor", "count": 1, "amount": 750.00, "valid": True}
]
# insert statement for the data1 table: stmt
stmt = insert(data1)
results = connection.execute(stmt, values_list)
print(results.rowcount)

"""stmt1 = select([data1])
print(stmt1)
results = connection.execute(stmt1).fetchall()
print(results)"""