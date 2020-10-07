import pymysql

def connect_database():
    con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
    cursor = con.cursor()
    return con, cursor