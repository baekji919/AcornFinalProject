import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

import matplotlib.font_manager as fm
font_name =fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf').get_name()
plt.rc('font', family=font_name)

mpl.rcParams['axes.unicode_minus'] = False

def security(name):
    df = pd.read_csv('C:/Users/acorn/Desktop/Project/3. 데이터 전처리 완료/안전/안전_파이차트.csv', encoding='cp949')
    data = df[['cctv 개수', '가로등 개수', '범죄 건수']]

    labels = ['cctv 개수', '가로등 개수', '범죄 건수']
    data = data[1:2]
    colors = ['#FBDBD1', '#EBFAD2', '#B5F7CE']

    plt.title(name + '_안전')
    centre_circle = plt.Circle((0, 0), 0.60, color='white')
    plt.gca().add_artist(centre_circle)
    plt.pie(np.array(data).ravel(), labels=labels, colors=colors, autopct='%1.1f%%',
            wedgeprops={'linewidth': 3},
            pctdistance=0.75, shadow=True, startangle=45)
    plt.axis('equal')

    strFile = 'C:/Users/acorn/Flask2/static/images/Seq.png'
    if os.path.isfile(strFile):
        os.remove(strFile)
    plt.savefig(strFile, format='png', dpi=300)

    return name