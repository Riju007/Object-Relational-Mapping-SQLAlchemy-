from sqlalchemy import create_engine, MetaData, Table, select, func

engine = create_engine("sqlite:///census.sqlite")
# print(engine.table_names())
metadata = MetaData()
connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)
# print(census.columns)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)
# print(state_fact.columns)

stmt = select([census.columns.state, func.sum(census.columns.pop2008), state_fact.columns.census_division_name])
stmt = stmt.select_from(census.join(state_fact, census.columns.state == state_fact.columns.name))
stmt = stmt.group_by(state_fact.columns.name)
# print(stmt)
result = connection.execute(stmt).fetchall()
for record in result:
    print(record)