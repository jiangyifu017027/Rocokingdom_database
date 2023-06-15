from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

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
    print(list_data)
    conn.commit()
    cursor.close()
    conn.close()
    return list_data

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/<number>", methods=['POST','GET'])
def login(number):
    if number == '1':
        if request.method =='POST':
            name = request.form.get('name')
            passwd = request.form.get('passwd')
            data = conn_DB()
            for temp in data:
                print(temp['用户名'], temp['密码'])
                if temp['用户名'] == name and temp['密码']==passwd:
                    return redirect(url_for("index"))
    if number == '0':
        if request.method =='POST':
            name = request.form.get('name')
            passwd = request.form.get('passwd')
            gamename = request.form.get('gamename')
            conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
            cursor = conn.cursor()
            sql = "INSERT INTO `player` (`id`, `gender`, `gameid`, `grade`, `family`, `password`) VALUES ('%s', 'man', '%s', 1200 , NULL,'%s');"%(name, passwd, gamename)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
    return render_template("Rocologin.html")


if __name__ == '__main__':
    app.run(debug=True)