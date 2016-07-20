import os, sys, time, random, urllib2, requests;
from bs4 import BeautifulSoup;

#create new folder

path = os.getcwd()
new_path = os.path.join(path,u'76xh')
if not os.path.isdir(new_path):
    os.mkdir(new_path)
print path
print new_path

def pic_spider(max_page):
    page = 2
    while (page <= max_page):
        url = "http://www.76xh.com/tupian/index_%s.html" %page;
        source_code = requests.get(url);
        plain_txt = source_code.text;
        soup = BeautifulSoup(plain_txt);
        for link in soup.findAll('a',{'target':'_blank'}):
            href = link.get('href');
            # pic_data(href);
            print href;


def pic_data(pic_url):
    source_code = requests.get(pic_url);
    plain_txt = source_code.text;
    soup = BeautifulSoup(plain_txt);
    for pic_info in soup.findAll('div',{'class':'mixed float_L'}):
        pics = pic_info.find('img');
        link = pics.get('src');
        flink = link ;
        complete_link = 'http://www.76xh.com' + str(flink);
        content = urllib2.urlopen(complete_link).read();

        with open(u'76xh' + '/' + flink[-11:], 'wb') as code:
            code.write(content);




pic_spider(2)
