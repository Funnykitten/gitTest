import pymysql

# 1.创建数据库连接对象
db = pymysql.connect(
    host='127.0.0.1',  # 主机地址
    port=3306,  # 端口
    user='root',  # 用户名
    password='root',  # 密码
    database='Tedu',  # 数据库名
    charset='utf8'  # 编码方式
)

# 2.创建游标对象
cur = db.cursor()

# 3.执行SQL语句
insert_sql = "insert into classes values(7,'珠儿','13533335678',31,'女','2020-1-9',82,now(),curtime(),'殷野王的女儿');"
#  phone | age  | gender | school_date | score | study_times| view_time | comment

cur.execute(insert_sql)

# 4.数据的提交（写操作：删除/修改/插入）
db.commit()

# 5.关闭游标对象
cur.close()

# 6.关闭数据库连接对象
db.close()
