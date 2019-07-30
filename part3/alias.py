from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine("sqlite:///employees.sqlite")
# print(engine.table_names())
connection = engine.connect()
metadata = MetaData()
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
# print(employees.columns)

# making a alias of the employee table
managers = employees.alias()
stmt1 = select([managers.columns.name.label('manager'), employees.columns.name.label('employee')])
# print(stmt1)
stmt1 = stmt1.where(managers.columns.id == employees.columns.mgr)
stmt1 = stmt1.order_by(managers.columns.name)
# print(stmt1)
result = connection.execute(stmt1).fetchall()
print(type(result))
for record in result:
    print(record)