from sqlalchemy import create_engine, MetaData, Table, select, func

engine = create_engine("sqlite:///employees.sqlite")
# print(engine.table_names())
metadata = MetaData()
connection = engine.connect()
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
# print(employees.columns)

managers = employees.alias()
# print(mangers.columns)

stmt = select([managers.columns.name, func.count(employees.columns.id)])
stmt = stmt.where(managers.columns.id == employees.columns.mgr)
stmt = stmt.group_by(managers.columns.name)

result = connection.execute(stmt).fetchall()
print(result)
