#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# muse
names = ['Honoka_Kosaka', 'Umi_Sonoda', 'Kotori_Minami', 'Hanayo_Koizumi', 'Rin_Hoshizora', 'Maki_Nishikino', 'Nico_Yazawa', 'Eli_Ayase', 'Nozomi_Tojo']
# aqours
names.extend(['Chika_Takami', 'Riko_Sakurauchi', 'You_Watanabe', 'Ruby Kurosawa', 'Yoshiko_Tsushima', 'Hanamaru_Kunikida', 'Dia_Kurosawa', 'Kanan_Matsuura', 'Mari_Ohara'])
# nijigasaki
names.extend(['Ayumu_Uehara', 'Ai_Miyashita', 'Setsuna_Yuki', 'Kasumi_Nakasu', 'Shizuku_Osaka', 'Rina_Tennoji', 'Emma_Verde', 'Kanata_Konoe', 'Karin_Asaka'])

for name in names:
    url = "https://love-live.fandom.com/wiki/" + name
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
    driver.get(url)
    xpath_sizes = '/html/body/div[3]/div[7]/div/div[1]/article/div[1]/div[1]/div[1]/div/aside/section[1]/div[6]/div'
    xpath_height = '/html/body/div[3]/div[7]/div/div[1]/article/div[1]/div[1]/div[1]/div/aside/section[1]/div[5]/div'
    
    error = True
    while(error):
        error = False
        try:
            text_sizes = driver.find_element_by_xpath(xpath_sizes).text
            text_height = driver.find_element_by_xpath(xpath_height).text
        except Exception:
            error = True

    print(name, ",", text_height.split()[0], ",", ",".join([x.strip().split()[1] for x in text_sizes.split(",")]), sep='')

