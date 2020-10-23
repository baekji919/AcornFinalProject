import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import matplotlib.font_manager as fm

font_name = fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf').get_name()
plt.rc('font', family=font_name)

mpl.rcParams['axes.unicode_minus'] = False

def traffic(name):
    bus_df = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/버스정류장 2020(행정동, cp949).csv', encoding='cp949')
    bus_df['구 행정동'] = bus_df['구'] + ' ' + bus_df['행정동']
    bus_gu_dong = bus_df['구 행정동'].unique()
    bus_cnt = bus_df['구 행정동'].groupby(bus_df['구 행정동']).count().tolist()
    bus_cnt_df = pd.DataFrame()
    bus_cnt_df['구 행정동'] = bus_gu_dong
    bus_cnt_df['버스정류장'] = bus_cnt

    subway_df = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/지하철2020(행정동, cp949).csv', encoding='cp949')
    subway_df['구 행정동'] = subway_df['구'] + ' ' + subway_df['행정동']
    subway_gu_dong = subway_df['구 행정동'].unique()
    subway_cnt = subway_df['구 행정동'].groupby(subway_df['구 행정동']).count().tolist()
    subway_cnt_df = pd.DataFrame()
    subway_cnt_df['구 행정동'] = subway_gu_dong
    subway_cnt_df['지하철'] = subway_cnt

    gu_dong_df = pd.DataFrame(bus_gu_dong, columns=['구 행정동'])
    sub_df = pd.merge(gu_dong_df, subway_cnt_df, how='left', on='구 행정동')
    sub_df['지하철'] = sub_df['지하철'].fillna(0.0)
    sub_df['지하철'] = sub_df['지하철'].astype('int64')

    traffic_data = pd.merge(bus_cnt_df, sub_df, how='left', on='구 행정동').reset_index(drop=True)
    t_data = traffic_data[traffic_data['구 행정동'] == '종로구 종로1.2.3.4가동'][['버스정류장', '지하철']]

    labels = t_data.columns

    colors = ['#FBDBD1', '#EBFAD2', '#B5F7CE', '#B8E1F4', '#BCBCF0', '#FC9CAC']

    plt.title(name + '_교통')
    centre_circle = plt.Circle((0, 0), 0.60, color='white')
    plt.gca().add_artist(centre_circle)
    plt.pie(np.array(t_data).ravel(), labels=labels, colors=colors, autopct='%1.1f%%',
            wedgeprops={'linewidth': 3},
            pctdistance=0.75, shadow=True,startangle=45)
    plt.axis('equal')

    strFile = 'C:/Users/acorn/Flask2/static/images/Bus.png'
    if os.path.isfile(strFile):
        os.remove(strFile)
    plt.savefig(strFile, format='png', dpi=300)

    return name