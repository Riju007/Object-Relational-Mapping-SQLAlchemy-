from sqlalchemy import create_engine, MetaData, func, select, Table
import pandas as pd
from matplotlib import pyplot as plt

engine = create_engine("sqlite:///census.sqlite")
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
# print(census.columns)

"""stmt1 = select([func.count(func.distinct(census.columns.state))])
result_proxy = connection.execute(stmt1).scalar()
print(result_proxy)

stmt2 = select([census.columns.state, func.count(census.columns.age)]).group_by(census.columns.state)
print(stmt2)
result = connection.execute(stmt2).fetchall()
print(result[0].keys())
print(result)"""

# to avoid name confusion
pop2008_sum = func.sum(census.columns.pop2008).label('population_2008')
stmt3 = select([census.columns.state, pop2008_sum]).group_by(census.columns.state)
result = connection.execute(stmt3).fetchall()
# print(result[0].keys())
# print(result)


df = pd.DataFrame(result)
df.columns = result[0].keys()
print(df.head())

df.plot.bar(color="green")
plt.xlabel('Age')
plt.ylabel("Population in 2008")
plt.show()
