import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
# 연예인 bibi(비비) 검색
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=bibi") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# 이제 여기에 코딩을 하면 됩니다!

thumbnails = soup.select('#imgList > div > a > img')
i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'img_homework/{i}.jpg')
    i += 1

driver.quit() # 끝나면 닫아주기