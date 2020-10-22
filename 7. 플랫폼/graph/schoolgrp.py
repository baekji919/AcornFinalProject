import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def school(name):
    df = pd.read_csv('C:/Users/acorn/Desktop/Project/8. 행정동 데이터/학교 2020(행정동, cp949).csv', encoding='cp949')
    df1 = df[df['행정동'].str.contains(name)]
    df1 = df1.groupby('학교종류').count().T

    df2 = df1.reset_index(drop=True)[0:1]

    labels = df2.columns
    data = df2[0:1]

    colors = ['#FBDBD1', '#EBFAD2', '#B5F7CE', '#B8E1F4', '#BCBCF0', '#FC9CAC']

    plt.title(name + '_Edu')
    centre_circle = plt.Circle((0, 0), 0.60, color='white')
    plt.gca().add_artist(centre_circle)
    plt.pie(np.array(data).ravel(), labels=labels, colors=colors, autopct='%1.1f%%',
            wedgeprops={'linewidth': 3},
            pctdistance=0.75, startangle=45)
    plt.axis('equal')

    return plt