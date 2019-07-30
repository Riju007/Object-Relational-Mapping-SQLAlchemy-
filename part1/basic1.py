from sqlalchemy import create_engine, Table, MetaData

# sqlite is the database driver.
engine = create_engine('sqlite:///census.sqlite')
print(engine.table_names())
# Getting metadata from the table using MetaData class.
metadata = MetaData()
# using reflection to read from the census table.
census = Table('census', metadata, autoload=True, autoload_with=engine)
print(repr(census))
# alternate way to print census data
print(repr(metadata.tables['census']))
# printing the columns of the database
print(f'columns are: {census.columns.keys()}')
