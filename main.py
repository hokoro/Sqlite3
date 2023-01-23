import DBfunction

table = DBfunction.sqliteDB("db1.db","table1")


#table.createTable([["name","text"],["age","interger"]])

table.insertTable(rows=['Aiden',25])
table.insertTable(rows=['moyo',22])
table.insertTable(rows=['elsea',23])
table.insertTable(rows=['MK',29])


print(table.selectaTableall())


table.updataTable('name','name','smeb','Aiden')

table.deleteTable('name','MK')



print(table.selectaTableall())

table.commitTable()