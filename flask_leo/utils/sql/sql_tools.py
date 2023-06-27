# 引入decimal模块
import pymysql

# ---------连接--------------

# connect_jk = pymysql.connect(host='',
#                           user='',
#                           password='',
#                           db='',
#                           charset='utf8')

user_list = ['user','user_logs','user_wx','user_dy','user_dy']
jk_list = ['jok_pod','jok_conis']

def getCur(table_name):
    return getConnect(table_name).cursor()


def getConnect(table_name):
    # if table_name in user_list:
    #     return connect_user
    # elif table_name in jk_list:
    #     return connect_jk
    return connect_user

def run_sql(table_name,sql):
    cur = getCur(table_name)
    cur.execute(sql)
    return cur.fetchall()

def run_sql_one(table_name,sql):
    cur = getCur(table_name)
    cur.execute(sql)
    return cur.fetchone()

def create_table(table_name, auto_id, auto_one, dtf):
    create_sql = 'CREATE TABLE ' + table_name + " ("
    for i in range(len(dtf)):
        if i == 0 and auto_id:
            create_sql += " id INT AUTO_INCREMENT PRIMARY KEY, "
        if i == 0 and auto_one:
            create_sql += dtf[i] + "  VARCHAR(255) not null primary key  "
        else:
            if i == 0:
                create_sql += "  " + dtf[i] + " VARCHAR(255) "
            else:
                create_sql += " , " + dtf[i] + " VARCHAR(255) "
    create_sql += ")"
    getCur(table_name).execute(create_sql)


def create_table_auto_id(table_name, dtf):
    create_table(table_name, 1, 0, dtf)


def create_table_auto_one(table_name, dtf):
    create_table(table_name, 0, 1, dtf)


def create_table_no_auto(table_name, dtf):
    create_table(table_name, 0, 0, dtf)


def install_table_str(table_name, para, dtf):
    cur = getCur(table_name)
    install_sql = 'INSERT INTO ' + table_name
    names = '( '
    paras = ') VALUES ( '
    for i in range(len(para)):
        if i == 0:
            names += dtf[i]
            paras += '%s'
        else:
            names += ' , ' + dtf[i]
            paras += ' , %s'
    install_sql += names + paras + ');'
    cur.execute(install_sql,para)

def install_table_(table_name, values, para , is_commit = 1):
    cur = getCur(table_name)
    install_sql = 'INSERT INTO ' + table_name
    names = '( '
    values_ = ') VALUES ( '
    for i in range(len(values)):
        parasv = values[i]
        if parasv:
            if i > 0:
                names += ' , '
                values_ += ' , '
            names += para[i]
            if isinstance(parasv, int):
                values_ += str(parasv)
            elif isinstance(parasv, float):
                values_ += str(parasv)
            else:
                values_ += '"' + str(parasv) + '"'
    install_sql += names + values_ + ');'
    cur.execute(install_sql)
    if is_commit:
        getConnect(table_name).commit()
    return cur

def install_table_no_id(table_name, values, para):
    install_table_(table_name,values, para)

def install_table(table_name, values, para, is_commit = 1):
   return install_table_(table_name, values, para,is_commit).lastrowid

def update_table(table_name, set, update):
    cur = getCur(table_name)
    update_sql = 'update ' + table_name + ' set ' + sql_map_str(set) + ' where ' +  sql_map_str(update)
    cur.execute(update_sql)
    getConnect(table_name).commit()

def install_tables(table_name, values, para):
    print("准备新增数据")
    install_tables_no_commit(table_name, values, para)
    getConnect(table_name).commit()
    print("新增数据成功")


def install_tables_no_commit(table_name, values, para):
    for i in range(len(values)):
        install_table(table_name, values[i], para,0)

def sql_table_page(table_name, values, para, page = 0 , number = 20):
    limit_param = f'limit {number * page}, {number}'
    return sql_table_(table_name,c_sql_text(table_name, values, para) + " " + limit_param)

def sql_table_all(table_name, values, para):
    return sql_table_(table_name,c_sql_text(table_name, values, para))

def sql_table_one(table_name, values, para):
    return sql_table_(table_name, c_sql_text(table_name, values, para),1)


def c_sql_text(table_name, values, para):
    install_sql = 'select * from  ' + table_name + ' where '
    for i in range(len(para)):
        value_ = sql_string_type(values[i])
        if value_ != None:
            if i == 0:
                install_sql += para[i] + " = " + value_
            else:
                install_sql += " and " + para[i] + " = " + value_
    return install_sql

def sql_table_(table_name, sql , is_one = 0 ):
    cur = getCur(table_name)
    cur.execute(sql)
    if is_one == 1:
        re_1 = cur.fetchone()
        if re_1:
            result = dict(zip([k[0] for k in cur.description], re_1))
            cur.close()
            return result
        else:
            return None
    re_1 = cur.fetchall()
    result = [dict(zip([k[0] for k in cur.description], row)) for row in re_1]
    cur.close()
    return result

def sql_map_str(map,sp=',',eq='='):
    string = ''
    for k,v in map.items():
        if string != '':
            string += sp
        string += k + eq + sql_string_type(v)
    return  string

def sql_string_type(string):
    if isinstance(string, int):
        return str(string)
    else:
        return '"' + str(string) + '"'

def executeCommit(self,sql=''):
    """执行数据库sql语句，针对更新,删除,事务等操作失败时回滚
    """
    try:
        self.cur.execute(sql)
        self.con.commit()
    except pymysql.Error as e:
        self.con.rollback()
        error = 'MySQL execute failed! ERROR (%s): %s' %(e.args[0],e.args[1])
        print("error:", error)
        return error

def close(self):
    if not  self.con:
        self.con.close()
    else:
        print("DataBase doesn't connect,close connectiong error;please check the db config.")


def del_table_(table_name, values, para):
    cur = getCur(table_name)
    install_sql = 'delete from ' + table_name + ' where '
    for i in range(len(para)):
        parasv = sql_string_type(values[i])
        if parasv:
            if i == 0:
                install_sql += para[i] + " = " + parasv
            else:
                install_sql += " and " + para[i] + " = " + parasv
    cur.execute(install_sql)
    getConnect(table_name).commit()
    return cur
