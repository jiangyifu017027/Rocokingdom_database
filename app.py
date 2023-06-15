from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

# 创建数据库连接
conn = pymysql.connect(
    host = '127.0.0.1', # 连接主机, 默认127.0.0.1 
    user = 'root',      # 用户名
    passwd = '123456',# 密码
    port = 3306,        # 端口，默认为3306
    db = 'lkwg',        # 数据库名称
    charset = 'gb2312'    # 字符编码
)

# 生成游标对象 cursor
cursor = conn.cursor()

# 查询数据库版本
cursor.execute("select version()") # 返回值是查询到的数据数量
# 通过 fetchall方法获得数据
data = cursor.fetchone()
print("Database Version:%s" % data)

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

cursor.close()  # 关闭游标
conn.close()    # 关闭连接

def conn_DB():
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select id, password from player'
    cursor.execute(sql)
    list_data=[]
    data=cursor.fetchall()
    for i in data:
        dic={'用户名':i[0], '密码':i[1]}
        list_data.append(dic)

    conn.commit()
    cursor.close()
    conn.close()
    return list_data

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method =='POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        data = conn_DB()
        for temp in data:
            print(temp['用户名'], temp['密码'])
            if temp['用户名'] == name and temp['密码']==passwd:
                return redirect('/admin')
    return render_template("Rocologin.html")


if __name__ == '__main__':
    app.run(debug=True)