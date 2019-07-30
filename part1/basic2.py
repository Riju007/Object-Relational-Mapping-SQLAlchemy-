from sqlalchemy import create_engine, Table, MetaData, select

engine = create_engine('sqlite:///census.sqlite')
# creating a connection object
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
# building a select statement for census table
statement = select([census])  # same as select * from census
print(statement)
# connection.execute() gives a result proxy object
result_proxy = connection.execute(statement)
print(result_proxy)
# ResultSet gives the actual data for the query in a list format
results = result_proxy.fetchall()
first_row = results[0]
print(first_row)
print(first_row[0])  # to get the first column value by index
print(first_row['state'])  # to get the column value by column name
