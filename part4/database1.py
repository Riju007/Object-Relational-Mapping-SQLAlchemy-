from sqlalchemy import create_engine, MetaData, Table, Column, select, insert
from sqlalchemy import Integer, Float, Boolean, String

engine = create_engine("sqlite:///data.sqlite")
metadata = MetaData()
connection = engine.connect()

data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
             )
metadata.create_all(engine)
# print(engine.table_names())
# print(repr(data))
# stmt = insert(data).values(name="Anna", count=1, amount=1000.00, valid=True)
# results = connection.execute(stmt)
# print(results.rowcount)

stmt = select([data]).where(data.columns.name == "Anna")
print(connection.execute(stmt).first())
