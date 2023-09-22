from pymysql import Connection

com = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)

print(com.get_server_info())

com_cor = com.cursor()

com.select_db('test')


com_cor.execute("insert into student values ('测试','男',18)")

com_cor.execute("delete from student where name = '测试'")

com_cor.execute('select * from student')

com_fat = com_cor.fetchall()

for fat in com_fat:
    print(fat)

com.close()