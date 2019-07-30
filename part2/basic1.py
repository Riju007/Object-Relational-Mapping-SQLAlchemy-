from sqlalchemy import create_engine, select, Table, MetaData, and_, desc

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

"""stmt1 = select([census]).where(census.columns.state == 'New York')
results = connection.execute(stmt1).fetchall()

for result in results:
    print(result.age, result.sex, result.pop2008)

stmt2 = select([census]).where(and_(census.columns.state == 'California', census.columns.sex != 'M'))
for result in connection.execute(stmt2):
    print(result.age, result.sex)


stmt3 = select([census.columns.state]).order_by(census.columns.state)
results = connection.execute(stmt3).fetchall()
print(results[:10])


stmt4 = select([census.columns.state]).order_by(desc(census.columns.state))
result = connection.execute(stmt4).fetchall()
print(result[:10])"""

stmt5 = select([census.columns.state, census.columns.age]).order_by(desc(census.columns.age), census.columns.state)
result = connection.execute(stmt5).fetchall()
print(result[:50])