import requests
import re


class Web:
    url_link = 'https://www.bbc.com/news'
    f_class_html = 'div'
    s_class_html = class_='gs-c-promo-body'
    webPart = ['news','future','sport']
    f_url_find = '="/'
    s_url_find = 'https://www.bbc.com/'
    f_headline_find = '</h3>'
    s_headline_find = ''

    txt_save_data = "NewsData.txt"
    excel_save_data = "NewsData.xlsx"

    def __init__(self, name_of_news, url_link, f_class_html, s_class_html, webPart, f_url_find, s_url_find, f_headline_find,s_headline_find,soup):
        self.name_of_news = name_of_news
        self.url_link = url_link
        self.f_class_html = f_class_html
        self.s_class_html = s_class_html
        self.webPart = webPart
        self.f_url_find = f_url_find
        self.s_url_find = s_url_find
        self.f_headline_find = f_headline_find
        self.s_headline_find = s_headline_find
        self.soup = soup
    

    def uploadData(self):

        news_list = []
        odkaz = str("")
        self.urls_list = []
        self.headlines_list = []
        news_file = open(self.txt_save_data,'a+')
        next_nonempty_string = bool(0)

        for l in self.soup.findAll(self.f_class_html , self.s_class_html):
 
           pomtext = str("")
       
           for slovoVHtml in str(l):
                pomtext += str(slovoVHtml)

           urlOdkaz = re.split(r'href|">',pomtext)
           next_word_headline = bool(0)

           news_file.write("\n")
           news_file.write(self.name_of_news+' |-| ')
           headline_after_noneline = 0

           if news_file == "":
               print("mezera")

           for url in urlOdkaz:
                #print(url)

                #finding url by parts of web
                for webParts in self.webPart:
                    new_url = url
                    if url.find(self.f_url_find+webParts) != -1:
                       new_url = re.split(webParts,new_url)

                       #webPart could contain same information as s_url_find duplicity of url
                       if webParts.find(self.s_url_find) != -1:
                            news_file.write(webParts+new_url[1]+" |-| ")  
                       else:
                            news_file.write(self.s_url_find+webParts+new_url[1]+" |-| ")  
                       #print(url,"\n")
                       
                headline_after_noneline = 0

                #this if only specifcly if headline is not in the url str
                if next_nonempty_string == 1:
                     after_url = url
                     pre_url = url
                     pre_url = re.split(self.s_headline_find,after_url)

                     after_url = re.split("\n",after_url)
                     after_str = str(after_url[1])
                     after_str = after_str.strip()
                     

                     news_file.write(str(after_str)+" |-| ")
                     next_nonempty_string = 0
                     headline_after_noneline = 1
                

                #finding headline
                if url.find(self.f_headline_find) != -1 and headline_after_noneline == 0: 
                    #cnn has headline on other prom url
                    if url.find('') != -1 and self.s_headline_find != "":
                        next_nonempty_string = 1
                    else:
                        #spliting url from endl and /span
                        pre_url = url
                        pre_url = re.split(self.f_headline_find,pre_url)
                        pre_url_updated = re.split('\n',pre_url[0])

                        #delete </span> from headline
                        if pre_url_updated[0].find('</span>') != -1:
                            pre_url_updated2 = re.split('</span>',pre_url_updated[0])
                            pre_url_updated[0] = pre_url_updated2[1]

                        #delete <span> from headline
                        if pre_url_updated[0].find('<span>') != -1:
                            pre_url_updated2 = re.split('<span>',pre_url_updated[0])
                            pre_url_updated[0] = pre_url_updated2[1]

                        #no empty
                        if pre_url_updated[0] != "":
                            #Neèitelný znak
                            try:
                                news_file.write(pre_url_updated[0]+" |-| ")
                            except:
                                news_file.write("ERROR-CHAR"+" |-| ")



    
        




