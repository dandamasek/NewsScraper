from ast import keyword
from urllib import response
from menubox import MyGUI
import requests
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
from rake_nltk import Rake
import nltk
import urllib3
from newspaper import Article
from textblob import TextBlob

#NUTN0 ZMENIT HEAD!!!!

#Change  "Mozilla/5.0" to your broswer {Mozzilla/5.0}
MyGUI.headers = {'User-agent': 'Mozzilla/5.0'}

#change what name of files u want
MyGUI.excel_save_data = "NewsData.xlsx"
MyGUI.txt_save_data = "NewsData.txt"



MyGUI()




#s = HTMLSession()
#url = 'https://www.foxnews.com/us/faa-abruptly-cancels-national-defense-airspace-lake-michigan-reporting-potential-contact'
##url = 'https://www.novinky.cz/clanek/ekonomika-vice-nez-milionu-domacnosti-energie-vyrazne-zlevni-40422773?utm_campaign=abtest203_personalizovany_layout_varCC&utm_medium=z-boxiku&utm_source=www.seznam.cz'
##url = 'https://edition.cnn.com/2023/02/11/middleeast/turkey-syria-earthquake-recovery-intl'
##url = 'https://www.seznamzpravy.cz/tag/krkonose-5707'
#url = 'https://zahranicni.hn.cz/c1-67170240-necham-si-plat-europoslance-a-zvladnu-oboji-rika-budouci-namestek-prazskeho-primatora-pro-kulturu-pospisil'
#url='https://www.bbc.com/sport/skateboarding/64618204'

#artice = Article(url)

#artice.download()
#artice.parse()
#artice.nlp()

#article_text = artice.text
##print(artice.text)

#r = Rake()
#r.extract_keywords_from_text(article_text)
#keywords_text = r.get_ranked_phrases_with_scores()
##print(keywords_text)
#for key in keywords_text:
#    print(key[1],"\n")

#print("\n")
#print(len(keywords_text))


