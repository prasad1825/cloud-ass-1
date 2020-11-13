import pandas as pg

pg1 = pg.read_csv('/root/cloud-ass-1/data1.csv')

pg1.head()

pg1.info()

pg1.PostTypeId.value_counts()

pg1.Body.head()

pg1.Body[0]

pg1.Body[1]

pg1.Tags.head()

pg1.Tags[0]

pg1.Tags[1]

type(pg1.Tags[0])

pg1[pg1['Body'].str.contains("hadoop")==True].head(2)


pg1.drop(['Body'], axis=1, inplace=True)

pg2 = pg.read_csv('/root/cloud-ass-1/data2.csv')


pg3 = pg.read_csv('/root/cloud-ass-1/data3.csv')

pg4 = pg.read_csv('/root/cloud-ass-1/data4.csv')

pg2.drop(['Body'], axis=1, inplace=True)
pg3.drop(['Body'], axis=1, inplace=True)

pg4.drop(['Body'], axis=1, inplace=True)

pg_fine = pg1.append(pg2)

pg_fine = pg_fine.append(pg3)

pg_fine = pg_fine.append(pg4)

pg_fine.reset_index(drop=True, inplace=True)

pg_fine.info()

sum(pg_fine.duplicated())

pg_fine.Id.nunique()


pg_fine[pg_fine.duplicated()==True].head(3)

pg_fine.drop_duplicates(inplace=True)


pg_fine.info()

pg_fine.reset_index(drop=True, inplace=True)

pg_fine.to_csv('/root/cloud-ass-1/final_data.csv')
