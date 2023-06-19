from flask import Flask, render_template, redirect, url_for, request
import pymysql
from flask import session

app = Flask(__name__)
app.secret_key = 'liangziwulitaisble'

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

def conn_DB1(name):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = '''
    select gameid from player where id = %s
    '''
    cursor.execute(sql,(name))
    data=cursor.fetchall()
    print(data[0][0])
    print(type(data))
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB2():
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select actiid,actiname,reward,actitype from activity'
    cursor.execute(sql)
    list_data=[]
    data=cursor.fetchall()
    for i in data:
        dic={'actiid':i[0], 'actiname':i[1],'reward':i[2],'actitype':i[3]}
        list_data.append(dic)
    print(list_data)
    conn.commit()
    cursor.close()
    conn.close()
    return list_data

def conn_DB3():
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'insert into petbag(id,petid) values(%s,%s)'%(getid,getpetid)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def conn_DB4(name):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = '''
    select id from player where id = %s
    '''
    cursor.execute(sql,(name))
    data=cursor.fetchall()
    print(data[0][0])
    print(type(data))
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB5(name):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = '''
    select family from player where id = %s
    '''
    cursor.execute(sql,(name))
    data=cursor.fetchall()
    print(data[0][0])
    print(type(data))
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB6(inquiryid):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = '''
    select pet.petid,pet.petname,pet.department,pet.racevalue,pet.bloodline,pet.skill
    from pet,player,petbag
    where player.id = petbag.id and pet.petid = petbag.petid and player.id = %s
    '''%(inquiryid)
    cursor.execute(sql)
    list_data=[]
    data=cursor.fetchall()
    for i in data:
        dic={'petid':i[0], 'petname':i[1],'department':i[2],'racevalue':i[3],'bloodline':i[4],'skill':i[5]}
        list_data.append(dic)
    print(list_data)
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
        data1 = conn_DB1(name)
        data2 = conn_DB4(name)
        data3 = conn_DB5(name)
        session['name'] = data1 #昵称
        session['id'] = data2 #id
        session['family'] = data3 #家族
        for temp in data:
            print(temp['用户名'], temp['密码'])
            if temp['用户名'] == name and temp['密码']==passwd:
                return redirect(url_for("self"))
    return render_template("Rocologin.html", show_login=True)

@app.route("/register", methods=['POST','GET'])
def register():
    if request.method =='POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        gamename = request.form.get('gamename')
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
        cursor = conn.cursor()
        sql = "INSERT INTO `player` (`id`, `gender`, `gameid`, `grade`, `family`, `password`) VALUES ('%s', 'man', '%s', 1200 , NULL,'%s');"%(name, gamename, passwd)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("login"))
    return render_template("Rocoregister.html", show_login=False)

@app.route("/table")
def table():
    activities = conn_DB2();
    return render_template("table.html",activities=activities)

@app.route("/self")
def self():
    player = session['name']
    id = session['id']
    family = session['family']
    return render_template("self.html",player=player,id=id,family=family)

@app.route('/input', methods=['POST','GET'])
def input():
    global getid
    global getpetid
    if request.method =='POST':
        getid = request.form.get('name')
        getpetid = request.form.get('petname')
        print(getid)
        print(getpetid)
        conn_DB3()
        return redirect(url_for("table"))
    return render_template("input.html")

@app.route('/playerpet')
def playerpet():
    global inquiryid
    inquiryid = session['id']
    pets = conn_DB6(inquiryid)
    return render_template('pet.html',pets=pets)

@app.route("/manager")
def manager():
    return render_template("managerself.html")

@app.route("/updateacti", methods=['POST','GET'])
def updateacti():
    if request.method =='POST':
        upactiid = request.form.get('actiid')
        upactiname = request.form.get('actiname')
        upreward = request.form.get('reward')
        upactitype = request.form.get('actitype')
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
        cursor = conn.cursor()
        sql = "INSERT INTO `activity` (`actiid`, `actiname`, `reward`, `actitype`) VALUES ('%s', '%s', '%s','%s');"%(upactiid,upactiname,upreward,upactitype)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("manager"))
    return render_template("updateacti.html")



if __name__ == '__main__':
    app.run(debug=True)