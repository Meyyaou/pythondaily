import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import urllib.parse

url="https://www.amazon.com/Bose-QuietComfort-45-Bluetooth-Canceling-Headphones/dp/B098FKXT8L?th=1"
#to get out of the 503 response
custom_headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6'}
res=requests.get(url, custom_headers)

soup=BeautifulSoup(res.text, 'lxml')

def get_product_info(url):
    title_elem=soup.select_one("#productTitle")
    title=title_elem.text.strip(' ')

    print('title:', title, '\n')
    #rating from an elem with attribut title (inside tag <id ="acrPopover" title="machin">)
    rate_elem=soup.select_one('#acrPopover')
    rate_txt=rate_elem.attrs.get('title')

    rating=rate_txt.replace('out of 5 stars', '')
    print('rating:', rating, '\n')

    #price
    price_elem=soup.select_one('span.a-price').select_one('span.a-offscreen')
    price=price_elem.text
    print('price:', price, '\n')

    #img
    image_elem=soup.select_one('#landingImage')
    image = image_elem.attrs.get('src')
    print("image:", image, '\n')
    #description
    desc_elem=soup.select_one('#feature-bullets')
    desc=desc_elem.text
    print("description:", desc, '\n')
    #reviews 
    rev_elem=soup.select('div.review')
    scraped_rev=[]
    for rev in rev_elem:
        r_author_elem=rev.select_one('span.a-profile-name')
        r_author=r_author_elem.text if r_author_elem else None

        r_rating_elem=rev.select_one('i.review-rating')
        r_rating=r_rating_elem.text.replace('out of 5 stars','') if r_rating_elem else None
        
        r_title_elem=rev.select_one('a.review_title')
        r_title_span_elem=r_title_elem.select_one("span:not([class])") if r_title_elem else None
        r_title= r_title_span_elem.text if r_title_span_elem else None

        r_content_elem=rev.select_one('span.review-text')
        r_content = r_content_elem.text if r_content_elem else None

        r_date_elem = rev.select_one('span.review-date')
        r_date= r_date_elem.text if r_date_elem else None

        r_verif_elem= rev.select_one('span.a-size-mini')
        r_verif= r_verif_elem.text if r_verif_elem else None

        r={
            "author": r_author,
            "rating": r_rating,
            "title": r_title,
            "content": r_content,
            "date": r_date,
            "verified": r_verif
        }

        scraped_rev.append(r)
    #print('reviews: ', scraped_rev, '\n')

#category pages for over-ear-headphones:
def parse_listing(listing_url):
    response=requests.get(listing_url, headers=custom_headers)
    soup_search=BeautifulSoup(response.text, 'lxml')
    link_elem=soup_search.select("[data-asin] h2 a")
    page_data=[]
    for link in link_elem:
        full_url=urllib.parse.urljoin(listing_url, link.attrs.get("href"))
        product_info=get_product_info(full_url)
        page_data.append(product_info)
    next_page_el=soup_search.select_one('a:contains("Next")')
    if next_page_el :
        next_page_url=next_page_el.attrs.get('href')
        next_page_url=urllib.parse.urljoin(listing_url, next_page_url)

    df = pd.DataFrame(page_data)
    df.to_json("headphones.json", orient='records')

get_product_info(url)
