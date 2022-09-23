import re
import requests
from bs4 import BeautifulSoup
import bs4

def main():
    keyword = input("키워드를 입력해주세요 : ")

    # for i in range(0, 4000, 10):
    for i in range(0, 10, 10):
        res = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&pd=4&query={keyword}&start={i}")

        soup = BeautifulSoup(res.content, 'html.parser')
        newsLinks = soup.select("div.group_news ul.list_news li a.news_tit[href]")

        for newsLink in newsLinks:
            newsURL = newsLink['href']

            # print(newsLink)
            # print(newsURL)

            if(newsURL == '#'): continue

            partRes = requests.get(newsURL)
            newsSoup = BeautifulSoup(partRes.content, 'html.parser')

            title = newsSoup.find("title")
            if(type(title) == bs4.element.Tag): 
                print("")
                print(title.get_text())

if __name__ == '__main__':
    main()