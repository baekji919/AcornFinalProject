import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

import matplotlib.font_manager as fm
font_name =fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf').get_name()
plt.rc('font', family=font_name)

mpl.rcParams['axes.unicode_minus'] = False

def public(name):
    movie = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/서울특별시 영화상영관 인허가 정보 2020(행정동, cp949).csv',
                        encoding='cp949')
    dep = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/백화점 2020(행정동, cp949).csv', encoding='cp949')
    hosp = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/서울특별시 병원 인허가 정보 2020(행정동, cp949).csv', encoding='cp949')
    bogun = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/보건소(행정동, cp949).csv', encoding='cp949')

    n1 = movie[movie['구 행정동'].str.contains(name)].count().values[0]

    n2 = dep[dep['구 행정동'].str.contains(name)].count().values[0]

    n3 = hosp[hosp['구 행정동'].str.contains(name)].count().values[0]

    n4 = bogun[bogun['구 행정동'].str.contains(name)].count().values[0]

    data = [n1, n2, n3, n4]

    df = pd.DataFrame({'영화관': n1, '백화점': n2, '병원': n3, '보건소': n4},
                      columns=['영화관', '백화점', '병원', '보건소'], index=['갯수'])

    labels = df.columns
    data = df[0:1]
    # colors = ['#ff9999','#bbddff','#99ffbb','#ffcc99','#ffb3e6']
    colors = ['#FBDBD1', '#EBFAD2', '#B5F7CE', '#B8E1F4', '#BCBCF0', '#FC9CAC']
    # explode = (0.05, 0, 0, 0, 0)
    plt.title(name + '_문화.공공시설')
    centre_circle = plt.Circle((0, 0), 0.60, color='white')
    plt.gca().add_artist(centre_circle)
    plt.pie(np.array(data).ravel(), labels=labels, colors=colors, autopct='%1.1f%%',
            wedgeprops={'linewidth': 3},
            pctdistance=0.75, shadow=True, startangle=45)
    plt.axis('equal')

    strFile = 'C:/Users/acorn/Flask2/static/images/Pub.png'
    if os.path.isfile(strFile):
        os.remove(strFile)
    plt.savefig(strFile, format='png', dpi=300)

    return name