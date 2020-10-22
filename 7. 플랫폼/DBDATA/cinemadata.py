import sqlite3

def cinema_lat_lng_data():
    con = sqlite3.connect('C:/Users/acorn/Flask2/db.sqlite')
    cur = con.cursor()
    sql = 'SELECT "위도", "경도" FROM cinema where "상세영업상태명" = "영업중";'
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