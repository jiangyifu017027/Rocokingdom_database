from flask import Flask, render_template, redirect, url_for, request, flash
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
    sql = 'select `actiid`,`actiname`,`reward`,`actitype` from `activity`'
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
    sql = 'insert into `petbag`(`id`,`petid`) values("%s","%s")'%(getid,getpetid)
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

def conn_DB7(name):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select exists (select `id` from `player` where `id` = "%s");'%(name)
    cursor.execute(sql)
    data=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB8(deleteid,deletepetname):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select exists (select `petid`,`petname` from `pet` where `petid`="%s" and `petname`="%s");'%(deleteid,deletepetname)
    cursor.execute(sql)
    data=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB9(updateacti):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select exists (select `actiid` from `activity` where `actiid`="%s");'%(updateacti)
    cursor.execute(sql)
    data=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB10(uppetid):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select exists (select `petid` from `pet` where `petid`="%s");'%(uppetid)
    cursor.execute(sql)
    data=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB11(punishid):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select exists (select `id` from `player` where `id`="%s");'%(punishid)
    cursor.execute(sql)
    data=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB12(uppetid):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select exists (select `petid` from `pet` where `petid`="%s");'%(uppetid)
    cursor.execute(sql)
    data=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB13(upename):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select exists (select `ename` from `equipment` where `ename`="%s");'%(upename)
    cursor.execute(sql)
    data=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB14(inquiryid):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = '''
    select equipment.ename,equipment.etype,equipment.actiid
    from player,equipment,equipbag
    where player.id = equipbag.id and equipment.ename = equipbag.ename and player.id = %s
    '''%(inquiryid)
    cursor.execute(sql)
    list_data=[]
    data=cursor.fetchall()
    for i in data:
        dic={'ename':i[0], 'etype':i[1],'actiid':i[2]}
        list_data.append(dic)
    print(list_data)
    conn.commit()
    cursor.close()
    conn.close()
    return list_data

def conn_DB15():
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = 'select manaid, manapasswd from manager'
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

def conn_DB16(name):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = '''
    select manaid from manager where manaid = %s
    '''
    cursor.execute(sql,(name))
    data=cursor.fetchall()
    print(data[0][0])
    print(type(data))
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

def conn_DB17(name):
    global sql
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
    cursor = conn.cursor()
    sql = '''
    select manaid from manager where manaid = %s
    '''
    cursor.execute(sql,(name))
    data=cursor.fetchall()
    print(data[0][0])
    print(type(data))
    conn.commit()
    cursor.close()
    conn.close()
    return data[0][0]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():
    loginbool = False
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
                loginbool = True
        if loginbool == False:
            flash("Invalid id or password!", category="error")
    return render_template("Rocologin.html", show_login=True)

@app.route("/register", methods=['POST','GET'])
def register():
    if request.method =='POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        passwdnew = request.form.get('passwdnew')
        gamename = request.form.get('gamename')
        playerexist = conn_DB7(name)
        print(playerexist)
        print(type(playerexist))
        if passwd != passwdnew:
            flash("Confirm password error!", category="error")
        else:
            if playerexist:
                flash("The account has been registered!", category="error")
            else:
                conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
                cursor = conn.cursor()
                sql = "INSERT INTO `player` (`id`, `gender`, `gameid`, `grade`, `family`, `password`) VALUES ('%s', 'man', '%s', 1200 , 'ds','%s');"%(name, gamename, passwd)
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
        gettype = request.form.get('actitype')
        print(getid)
        print(getpetid)
        if gettype == "pet":
            conn_DB3()
            return redirect(url_for("table"))
        else:
            conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
            cursor = conn.cursor()
            sql = 'insert into equipbag(`id`,`ename`) values("%s","%s")'%(getid,getpetid)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for("table"))
    return render_template("input.html")

@app.route('/playerpet')
def playerpet():
    global inquiryid
    inquiryid = session['id']
    pets = conn_DB6(inquiryid)
    return render_template('pet.html',pets=pets)

@app.route("/managerself")
def managerself():
    mananame = session["mananame"]
    return render_template("managerself.html")


@app.route("/managerlogin", methods=['POST','GET'])
def managerlogin():
    loginbool = False
    if request.method =='POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        data = conn_DB15()
        data1 = conn_DB16(name)
        data2 = conn_DB17(name)
        session['mananame'] = data1 #昵称
        session['manaid'] = data2 #id
        for temp in data:
            print(temp['用户名'], temp['密码'])
            if temp['用户名'] == name and temp['密码']==passwd:
                return redirect(url_for("managerself"))
                loginbool = True
        if loginbool == False:
            flash("Invalid id or password!", category="error")
    return render_template("managerlogin.html")

@app.route("/updateacti", methods=['POST','GET'])
def updateacti():
    if request.method =='POST':
        upactiid = request.form.get('actiid')
        upactiname = request.form.get('actiname')
        upreward = request.form.get('reward')
        upactitype = request.form.get('actitype')
        data = conn_DB9(upactiid)
        if data:
            flash("This id has existed!", category="error")
        else:
            conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
            cursor = conn.cursor()
            sql = "INSERT INTO `activity` (`actiid`, `actiname`, `reward`, `actitype`) VALUES ('%s', '%s', '%s','%s');"%(upactiid,upactiname,upreward,upactitype)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for("manager"))
    return render_template("updateacti.html")

@app.route("/updatepet", methods=['POST','GET'])
def updatepet():
    if request.method =='POST':
        uppetid = request.form.get('petid')
        updepartment = request.form.get('department')
        upracevalue = request.form.get('racevalue')
        upbloodline = request.form.get('bloodline')
        upacqstate = request.form.get('acqstate')
        upskill = request.form.get('skill')
        uppetname = request.form.get('petname')
        data = conn_DB10(uppetid)
        if data:
            flash("This pet has existed!", category="error")
        else:
            conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
            cursor = conn.cursor()
            sql = "INSERT INTO `pet`(`petid`,`department`,`racevalue`,`bloodline`,`acqstate`,`skill`,`petname`) VALUES ('%s','%s','%d','%s','%s','%s','%s');"%(uppetid,updepartment,int(upracevalue),upbloodline,upacqstate,upskill,uppetname)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for("manager"))
    return render_template("updatepet.html")

@app.route("/petchange", methods=['POST','GET'])
def petchang():
    if request.method =='POST':
        uppetid = request.form.get('petid')
        updepartment = request.form.get('department')
        upracevalue = request.form.get('racevalue')
        upbloodline = request.form.get('bloodline')
        upacqstate = request.form.get('acqstate')
        upskill = request.form.get('skill')
        uppetname = request.form.get('petname')
        data = conn_DB11(uppetid)
        if data == 0:
            flash("This pet doesn't exist!", category="error")
        else:
            conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
            cursor = conn.cursor()
            sql = "UPDATE `pet` SET (`petid`,`department`,`racevalue`,`bloodline`,`acqstate`,`skill`,`petname`) VALUES ('%s','%s','%d','%s','%s','%s','%s');"%(uppetid,updepartment,int(upracevalue),upbloodline,upacqstate,upskill,uppetname)
            sql = "UPDATE `pet` SET `department`='%s' WHERE `petid`='%s'"%(updepartment,uppetid)
            cursor.execute(sql)
            conn.commit()
            sql = "UPDATE `pet` SET `racevalue`='%d' WHERE `petid`='%s'"%(int(upracevalue),uppetid)
            cursor.execute(sql)
            conn.commit()
            sql = "UPDATE `pet` SET `bloodline`='%s' WHERE `petid`='%s'"%(upbloodline,uppetid)
            cursor.execute(sql)
            conn.commit()
            sql = "UPDATE `pet` SET `acqstate`='%s' WHERE `petid`='%s'"%(upacqstate,uppetid)
            cursor.execute(sql)
            conn.commit()
            sql = "UPDATE `pet` SET `skill`='%s' WHERE `petid`='%s'"%(upskill,uppetid)
            cursor.execute(sql)
            conn.commit()
            sql = "UPDATE `pet` SET `petname`='%s' WHERE `petid`='%s'"%(uppetname,uppetid)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for("manager"))
    return render_template("petchange.html")

@app.route("/punish", methods=['POST','GET'])
def punish():
    if request.method =='POST':
        punishid = request.form.get('punishid')
        sepunishid = request.form.get('sepunishid')
        data = conn_DB12(punishid)
        if data == 0:
            flash("This player doesn't exist!", category="error")
        else:
            if punishid == sepunishid:
                conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
                cursor = conn.cursor()
                sql = 'DELETE FROM `player` WHERE `id` = "%s"'%(punishid)
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for("manager"))
    return render_template("punish.html")

@app.route("/deletepet", methods=['POST','GET'])
def deletepet():
    if request.method =='POST':
        deleteid = request.form.get('deleteid')
        deletepetname = request.form.get('deletepetname')
        playerid = session['id']
        booldelete = conn_DB8(deleteid, deletepetname)
        print(booldelete)
        print(type(booldelete))
        if booldelete:
            conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
            cursor = conn.cursor()
            sql = 'DELETE FROM `petbag` WHERE `id`="%s" and `petid`="%s"'%(playerid,deleteid)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for("self"))
        else:
            flash("放生宠物失败!", category="error")
    return render_template("deletepet.html")

@app.route("/passwdchange", methods=['POST','GET'])
def passwdchange():
    if request.method =='POST':
        password = request.form.get('password')
        passwordnew = request.form.get('passwordnew')
        passwordnewnew = request.form.get('passwordnewnew')
        playerid = session['id']
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
        cursor = conn.cursor()
        sql = "SELECT `password` FROM `player` WHERE `id`='%s'"%(playerid)
        cursor.execute(sql)
        data=cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        if password != data:
            flash("password error!", category="error")
        else:
            if passwordnew != passwordnewnew:
                flash("Confirm password error!", category="error")
            else:
                conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
                cursor = conn.cursor()
                sql = "UPDATE `player` SET `password`='%s' WHERE `id`='%s'"%(passwordnew,playerid)
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for("login"))
    return render_template("passwdchange.html")

@app.route("/updateequipment", methods=['POST','GET'])
def updateequipment():
    if request.method =='POST':
        upename = request.form.get('ename')
        upetype = request.form.get('etype')
        upactiid = request.form.get('actiid')
        data = conn_DB13(upename)
        if data:
            flash("This equipment has existed!", category="error")
        else:
            conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="lkwg", charset="gb2312")
            cursor = conn.cursor()
            sql = "INSERT INTO `equipment`(`ename`,`etype`,`actiid`) VALUES ('%s','%s','%s');"%(upename,upetype,upactiid)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for("manager"))
    return render_template("updateequipment.html")

@app.route("/playerequipment")
def playerequipment():
    global inquiryid
    inquiryid = session['id']
    equipments = conn_DB14(inquiryid)
    return render_template('playerequipment.html',equipments=equipments)

if __name__ == '__main__':
    app.run(debug=True)