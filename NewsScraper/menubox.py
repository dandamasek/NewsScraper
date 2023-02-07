from email import message
import tkinter as tk
from tkinter import Variable, messagebox
from bs4 import BeautifulSoup
import requests
import re

from data import Data
from web import Web

class MyGUI(Data):
    
    def __init__(self):
        #later do dynamic not like this
      
        self.root = tk.Tk()
        #self.root.geometry("700x400")
        self.root.title("Finding articles")

        self.label = tk.Label(self.root, text="Keywords for finding:",font=('Arial',14))
        self.label.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root,height=3,font=('Arial',10))
        self.textbox.pack(padx=10, pady=10)

        #variables for checkbox media selection
        self.useNewsBBC = tk.IntVar()
        self.useNewsHN = tk.IntVar()
        self.useNewsCNN = tk.IntVar()
        self.useNewsSEZNAM = tk.IntVar()
        self.useNewsFOX = tk.IntVar()
        self.useNewsFRANCE24 = tk.IntVar()
        self.useNewsREUTERS = tk.IntVar()

        
       # self.check.pack(padx=10,pady=10)

       #checkbuttons grid for adds articles from news to txt file
        self.checkframe = tk.Frame(self.root)
        self.checkframe.columnconfigure(0, weight=1)

        self.chc1 = tk.Checkbutton(self.checkframe, text="BBC" , font=('Arial',12),command = self.addNewsBBC, variable = self.useNewsBBC)
        self.chc1.grid(row=0,column=0, sticky=tk.N)

        self.chc2 = tk.Checkbutton(self.checkframe, text="HN" , font=('Arial',12), command = self.addNewsHN, variable = self.useNewsHN)
        self.chc2.grid(row=0,column=1, sticky=tk.W)

        self.chc3 = tk.Checkbutton(self.checkframe, text="CNN" , font=('Arial',12), command = self.addNewsCNN, variable = self.useNewsCNN)
        self.chc3.grid(row=0,column=2, sticky=tk.W)

        self.chc4 = tk.Checkbutton(self.checkframe, text="SEZNAM" , font=('Arial',12), command = self.addNewsSEZNAM, variable = self.useNewsSEZNAM)
        self.chc4.grid(row=0,column=3, sticky=tk.W)

        self.chc5 = tk.Checkbutton(self.checkframe, text="FOX" , font=('Arial',12), command = self.addNewsFOX, variable = self.useNewsFOX)
        self.chc5.grid(row=0,column=4, sticky=tk.W)

        self.chc6 = tk.Checkbutton(self.checkframe, text="FRANCE24" , font=('Arial',12),command = self.addNewsFRANCE24, variable = self.useNewsFRANCE24)
        self.chc6.grid(row=0,column=5, sticky=tk.W)

        self.chc7 = tk.Checkbutton(self.checkframe, text="REUTERS" , font=('Arial',12),command = self.addNewsREUTERS, variable=self.useNewsREUTERS)
        self.chc7.grid(row=0,column=6, sticky=tk.W)

        self.checkframe.pack(fill='y')

        #buttons grid
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)

        self.btn1 = tk.Button(self.buttonframe, text="Show matched articles" , font=('Arial',12),command = self.news_scraper_trigger)
        self.btn1.grid(row=0,column=0, sticky=tk.W+tk.E)
        
        self.btn2 = tk.Button(self.buttonframe, text="Save all articles to excel" , font=('Arial',12),command = self.SaveToExcel_trigger)
        self.btn2.grid(row=0,column=1, sticky=tk.W+tk.E)
        self.buttonframe.pack(fill='y')

        self.label2 = tk.Label(self.root, text="Matching articles by keywords will by displayed in console",font=('Arial',14))
        self.label2.pack(padx=30,pady=10)


        self.root.protocol("WM_DELETE_WINDOW",self.on_closing)

        self.news_label = tk.Label(self.root, text='')
        self.news_label.pack(pady=10)

        self.root.mainloop()

    #update of keywords in textbox
    def KeywordsFromBox(self): 
        
        self.keywords = []
        text = self.textbox.get('1.0',tk.END).split(",")
        for txt in text:
            if txt.find('\n') != -1:
                txt = txt.split('\n')
                self.keywords.append(txt[0])
            else:
                self.keywords.append(txt)

    def SaveToExcel_trigger(self):
        self.saveToExcel()

    def deleteNoNeedNews(self,nameOfNews):
        f = open(self.txt_save_data,"r")
        lines = f.readlines()
        f.close()
           
        #delete all lines without full information
        f = open(self.txt_save_data,"w")
        for line in lines:
            va_line = line.split('|-|')
            #lenght of data and second is real url
            if len(va_line) >= 4 and va_line[1].find("https:") != -1:
                if va_line[0] != nameOfNews: 
                    f.write(line)

        f.close()

    def addNewsBBC(self):
        #self.KeywordsFromBox()
        if self.useNewsBBC.get() == 1:
            request = requests.get('https://www.bbc.com/news', headers=self.headers)
            html = request.content
            soup = BeautifulSoup(html,'html.parser')
            webPart = ['news','future','sport','travel','worklife','travel/article']
            class_ins = class_='gs-c-promo-body'
        
            bbc = Web('BBC','https://www.bbc.com/news','div',class_ins,webPart,'="/','https://www.bbc.com/','</h3>','',soup)
            self.addNewsToData(bbc)
            bbc.uploadData()

        else:
            self.deleteNoNeedNews('BBC ')

    #all addNews{name} are just for manually adding
    def addNewsHN(self):
        if self.useNewsHN.get() ==1:
            request = requests.get('https://hn.cz/', headers=self.headers)
            html = request.content
            soup = BeautifulSoup(html,'html.parser')
            webPart = ['byznys','zpravy','nazory','tech','reality','investice','procne','archiv','domaci','hn','vikend','zahranicni','podcasty']
            class_ins = class_='article-title'

            hn = Web('HN','https://hn.cz/','h3',class_ins,webPart,'="//','https://','</a>','',soup)
            self.addNewsToData(hn)
            hn.uploadData()
        else:
            self.deleteNoNeedNews('HN ')

    def addNewsCNN(self):
        if self.useNewsCNN.get() == 1:
            request = requests.get('https://edition.cnn.com/world', headers=self.headers)
            html = request.content
            soup = BeautifulSoup(html,'html.parser')
            webPart = ['europe','world','sport','travel','india','china','united-kingdom','australia','business','health','tech','features','poticics','style','videos','more','2023','2022']
            class_ins = class_='container__link'

            cnn = Web('CNN','https://edition.cnn.com/world','a',class_ins,webPart,'="/','https://edition.cnn.com/','<div class="container__headline container_lead-plus-headlines__headline" data-editable="headline','"\n|</div>"',soup)
            self.addNewsToData(cnn)
            cnn.uploadData()
        else:
            self.deleteNoNeedNews('CNN ')

    def addNewsSEZNAM(self):
        if self.useNewsSEZNAM.get() == 1:
            request = requests.get('https://www.seznamzpravy.cz/sekce/domaci-13', headers=self.headers)
            html = request.content
            soup = BeautifulSoup(html,'html.parser')
            webPart = ['https://www.seznam','https://www.novinky','https://www.sport','https://www.sekce','https://www.tag','https://www.stream','https://www.garaz','https://www.prozeny']
            class_ins = class_='e_J g_dF'

            seznam = Web('SEZNAM','https://www.seznamzpravy.cz/sekce/domaci-13','a',class_ins,webPart,'="','','</a>','',soup)
            self.addNewsToData(seznam)
            seznam.uploadData()
        else:
            self.deleteNoNeedNews('SEZNAM ')

    def addNewsFOX(self):
        if self.useNewsFOX.get() == 1:
            request = requests.get('https://www.foxnews.com/', headers=self.headers)
            html = request.content
            soup = BeautifulSoup(html,'html.parser')
            webPart = ['//www.foxnews.com','https://www.foxnews.com','//www.foxbusiness.com','https://www.foxbusiness.com','https://video.foxnews.com','//www.foxweather']
            class_ins = class_='title'

            fox = Web('FOX','https://www.foxnews.com/','h2',class_ins,webPart,'="','https:','</a>','',soup)
            self.addNewsToData(fox)
            fox.uploadData()
        else:
            self.deleteNoNeedNews('FOX ')

    def addNewsFRANCE24(self):
        if self.useNewsFRANCE24.get() == 1:
            request = requests.get('https://www.france24.com/en/live-news/', headers=self.headers)
            html = request.content
            soup = BeautifulSoup(html,'html.parser')
            webPart = ['en']
            class_ins = class_='m-item-list-article'

            france24 = Web('FRANCE24','https://www.france24.com/en/live-news/','div',class_ins,webPart,'="/','https://www.france24.com/','</p>','',soup)
            self.addNewsToData(france24)
            france24.uploadData()
        else:
            self.deleteNoNeedNews('FRANCE24 ')

    def addNewsREUTERS(self):
        if self.useNewsREUTERS.get() == 1:
            request = requests.get('https://www.reuters.com/', headers=self.headers)
            html = request.content
            soup = BeautifulSoup(html,'html.parser')
            webPart = ['world','technology','http://www.technology','legal','markets','lifestyle','business','sports','https://www.reuters.com/world']
            class_ins = class_='text__text__1FZLe'

            reuters1 = Web('REUTERS','https://www.reuters.com/','a',class_ins,webPart,'="/','https://www.reuters.com/','</a>','',soup)
            self.addNewsToData(reuters1)
            reuters1.uploadData()

            reuters2 = Web('REUTERS','https://www.reuters.com/','a',class_ins,webPart,'="/','https://www.reuters.com/','</span><span','',soup)
            self.addNewsToData(reuters2)
            reuters2.uploadData()
        else:
            self.deleteNoNeedNews('REUTERS ')


    def news_scraper_trigger(self):
        self.KeywordsFromBox()
        self.cleanData()
        self.updateData()
        self.news_scraper()

    def on_closing(self):
        if messagebox.askyesno(title="Alert",message = "Are you sure?"):
            self.root.destroy()

