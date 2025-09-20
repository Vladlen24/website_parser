import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from dataclasses import dataclass
from pprint import pprint


main_page = "https://habr.com/ru/articles/top/daily"

@dataclass
class ArticlesData:
    title: str
    views: str


def get_url_html(url: str) -> str:
    res = requests.get(
        url, 
        headers={
            "User-Agent": UserAgent().google,
        }
    )
    return res.text 


def get_soup(html_text: str) -> BeautifulSoup:
    return BeautifulSoup(html_text, "lxml")

def get_all_habr_posts(soup: BeautifulSoup) -> list[ArticlesData]:
    posts_data = []
    all_articles_soup = soup.find_all("article", class_="tm-articles-list__item")
    for article_soup in all_articles_soup:
        article_title: str = article_soup.find("a", class_="tm-title__link").find("span").text
        print(f"{article_title=}")  
        article_views = article_soup.find("span", class_="tm-icon-counter__value").text
        print(f"{article_views= }")
        posts_data.append(ArticlesData(
            title=article_title,
            views=article_views,
        ))
    return posts_data
 

def main():
    html = get_url_html(main_page)
    soup = get_soup(html)
    # print(soup)
    posts = get_all_habr_posts(soup)
    pprint(posts)
    

if __name__ == "__main__":
    main() 