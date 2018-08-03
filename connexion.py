import pymysql


def connexion():
    conn = pymysql.connect(host="localhost",
                                   user="root", password="",
                                   database="news")
    cursor = conn.cursor()
    cursor.execute("SELECT titre, description FROM News ")
    rows = cursor.fetchall()
    conn.close()
    return rows