# obj:  Build query to return state names by population difference from 2008 to 2000:

from sqlalchemy import create_engine, MetaData, Table, select, desc,case, cast, Float, func

engine = create_engine('sqlite:///census.sqlite')
# print(engine.table_names())
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
# print(census.columns)

"""stmt1 = select([census.columns.state, (census.columns.pop2008 - census.columns.pop2000).label('pop_change')])
stmt1 = stmt1.group_by(census.columns.state)
stmt1 = stmt1.order_by(desc('pop_change')).limit(8)

results = connection.execute(stmt1).fetchall()
for result in results:
    print(f'{result.state}: {result.pop_change}')"""

# To calculate female percentage in the year 2000
# 1 sum of female population
# total population in the year 2000
# percentage calculation

female_pop2000 = func.sum(case([(census.columns.sex == 'F', census.columns.pop2000)], else_ = 0))
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)
stmt2 = select([female_pop2000 / total_pop2000 * 100])
percent_female = connection.execute(stmt2).scalar()
print(percent_female)