from lxml import html
import requests
from lxml.cssselect import CSSSelector

url = 'https://developer.ibm.com/announcements/category/data-science/?fa=date%3ADESC&fb='
url_get = requests.get(url)
tree = html.document_fromstring(url_get.content)
print(type(tree))

announcements=[]
articles = tree.cssselect('.developer--card > a.developer--card__block_link')
for article in articles:

    link = article.get('href')
    # atype = article.cssselect('div.developer--card__body > h5')[0].text.strip()
    # adate = article.cssselect('div.developer--card__body > h5 > .developer--card__date')[0].text
    title = article.cssselect('div.developer--card__body > h3.developer--card__title')[0].text_content()
    # excerpt= article.cssselect(' div.developer--card__body > p.developer--card__excerpt')[0].text
    category= article.cssselect('div.developer--card__bottom > p.cpt-byline__categories span')
    #only two available on block: except '+'

    #announcements.append([link,atype,adate,title,excerpt,[category[0].text,category[1].text]])
    announcements.append([link,title,[span.text for span in category if span.text!='+']])

print(announcements)
