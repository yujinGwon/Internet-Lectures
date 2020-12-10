from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''
with open("kacoding.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        text += line.replace('[뉴진]','').replace('[김나현]','').split(']')[1]

        #if ' : ' in line:
        #    text += line.split(' : ')[1].replace('ㅋ', '').replace('사진\n','').replace('ㅠ','').replace('진짜','').replace('근데','').replace('그래서','').replace('그냥','')\
        #        .replace('존나','').replace('이제','').replace('네네','').replace('뭔가','').replace('그거','').replace('같아요','').replace('지금','')\
        #        .replace('내가','').replace('그래도','')


print(text)

#wc = WordCloud(font_path='C:/Windows/Fonts/NanumGothicExtraBold.ttf', background_color="white", width=600, height=400)
#wc.generate(text)
#wc.to_file("result.png")

# 여기서부터...
#mask = np.array(Image.open('cloud.png'))
#wc = WordCloud(font_path='C:/Windows/Fonts/NanumGothicExtraBold.ttf', background_color="white", mask=mask)
#wc.generate(text)
#wc.to_file("result_masked.png")


#import matplotlib.font_manager as fm

# 이용 가능한 폰트 중 '고딕'만 선별

#for font in fm.fontManager.ttflist:
#    if 'Gothic' in font.name:
#        print(font.name, font.fname)