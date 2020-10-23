import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import matplotlib.font_manager as fm

font_name = fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf').get_name()
plt.rc('font', family=font_name)

mpl.rcParams['axes.unicode_minus'] = False

def convin(name):
    conv = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/편의점 2020(행정동, cp949).csv', encoding='cp949')
    food = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/음식점 2020(행정동, cp949).csv', encoding='cp949')
    cof = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/카페 2020(행정동, cp949).csv', encoding='cp949')
    dess = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/제과제빵 2020(행정동, cp949).csv', encoding='cp949')

    n1 = conv[conv['구 행정동'].str.contains(name)].count().values[0]

    n2 = food[food['구 행정동'].str.contains(name)].count().values[0]

    n3 = cof[cof['구 행정동'].str.contains(name)].count().values[0]

    n4 = dess[dess['구 행정동'].str.contains(name)].count().values[0]

    data = [n1, n2, n3, n4]

    df = pd.DataFrame({'편의점': n1, '음식점': n2, '카페': n3, '제과제빵': n4},
                      columns=['편의점', '음식점', '카페', '제과제빵'], index=['갯수'])

    labels = df.columns
    data = df[0:1]
    colors = ['#FBDBD1', '#EBFAD2', '#B5F7CE', '#B8E1F4', '#BCBCF0', '#FC9CAC']

    plt.title(name + '_편의시설')
    centre_circle = plt.Circle((0, 0), 0.60, color='white')
    plt.gca().add_artist(centre_circle)
    plt.pie(np.array(data).ravel(), labels=labels, colors=colors, autopct='%1.1f%%',
            wedgeprops={'linewidth': 3},
            pctdistance=0.75, shadow=True, startangle=45)
    plt.axis('equal')

    strFile = 'C:/Users/acorn/Flask2/static/images/Conv.png'
    if os.path.isfile(strFile):
        os.remove(strFile)
    plt.savefig(strFile, format='png', dpi=300)

    return name