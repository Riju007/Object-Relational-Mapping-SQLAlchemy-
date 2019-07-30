from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine("sqlite:///census.sqlite")
# print(engine.table_names())
connection = engine.connect()
metadata = MetaData()

census = Table('census', metadata, autoload=True, autoload_with=engine)
# print(census.columns)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)
# print(state_fact.columns)

stmt1 = select([census, state_fact])
stmt1 = stmt1.select_from(census.join(state_fact, census.columns.state == state_fact.columns.name))
result = connection.execute(stmt1).first()
for key in result.keys():
    print(key, getattr(result, key))