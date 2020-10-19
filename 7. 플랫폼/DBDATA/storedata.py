import sqlite3

def store_lat_lng_data():
    con = sqlite3.connect('C:/Users/acorn/Flask2/db.sqlite')
    cur = con.cursor()
    sql = 'SELECT "Y좌표", "X좌표" FROM store'
    cur.execute(sql)

    result = cur.fetchall() # 변수 지정
    lat_list = [] # 위도
    lng_list = [] # 경도

    for i in range(0, len(result)):
        lat_list.append(result[i][0])
        lng_list.append(result[i][1])

    cur.close()
    con.close()

    return [lat_list, lng_list]