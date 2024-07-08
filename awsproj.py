# import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

today = datetime.date.today()

print(today)    

# connecting to website

URL = "https://www.amazon.in/Bacca-Bucci-HUNTER-outdoor-Trekking/dp/B097N9NSVH/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=a4AU9&content-id=amzn1.sym.120dbce3-1ee8-4441-9b7e-775b1c676a73%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=120dbce3-1ee8-4441-9b7e-775b1c676a73&pf_rd_r=SBYMDFAK7A2DJ724Z6KY&pd_rd_wg=veTFT&pd_rd_r=3859be7b-5eca-407c-b17b-047bcf66f492&pd_rd_i=B097NBPV24&th=1&psc=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" , "Accept Encoding": "gzip, deflate", "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT" : "1", "Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers= headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

title = soup2.find(id='productTitle').get_text()
price = soup2.find(class_ ='a-price-whole').get_text()
rating = soup2.find(class_ = 'a-size-base a-color-base').get_text()
title=title.strip()
price = price.strip()

print(title)
print(price)
#print(type(price))        #to check data type of price


#storing data in csv file

import csv

header = ['Title', 'Price', 'Date', 'Rating']
data = [title, price, today, rating]

#convert data type to list
type(data)
#print(type(data))                                   #verify change of data type


import pandas as pd

df = pd.read_csv(r'C:\Users\aksha\AmazonWebScrapeDataset.csv')
print(df)

#appending data to csv file
with open('AmazonWebScrapeDataset.csv', 'a+', newline='', encoding= 'UTF8') as f:          #change w to a+ to append data
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    
    

def check_price():
    URL = "https://www.amazon.in/Bacca-Bucci-HUNTER-outdoor-Trekking/dp/B097N9NSVH/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=a4AU9&content-id=amzn1.sym.120dbce3-1ee8-4441-9b7e-775b1c676a73%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=120dbce3-1ee8-4441-9b7e-775b1c676a73&pf_rd_r=SBYMDFAK7A2DJ724Z6KY&pd_rd_wg=veTFT&pd_rd_r=3859be7b-5eca-407c-b17b-047bcf66f492&pd_rd_i=B097NBPV24&th=1&psc=1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" , "Accept Encoding": "gzip, deflate", "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT" : "1", "Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers= headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(class_ ='a-price-whole').get_text()
    rating = soup2.find(class_ = 'a-size-base a-color-base').get_text()
    title = title.strip()
    
    import datetime
    today = datetime.date.today()
    
    import csv
    header = ['Title', 'Price', 'Date', 'Rating']
    data = [title, price, today, rating]
    
    with open('AmazonWebScrapeDataset.csv', 'a+', newline='', encoding= 'UTF8') as f: 
        writer = csv.writer(f)
        writer.writerow(data)

while(True):
    check_price()
    time.sleep(5)        


import pandas as pd

df = pd.read_csv(r'C:\Users\aksha\AmazonWebScrapeDataset.csv')
print(df)        