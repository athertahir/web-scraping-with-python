from pyquery import PyQuery as pq
import requests

sourceUrl='https://developer.ibm.com/announcements/'
dataSet = list()

def read_url(url):
    """Read given Url , Returns pyquery object for page content"""
    pageSource = requests.get(url).content
    return pq(pageSource)

def get_details(page):
    """read 'page' url and append list of queried items to dataSet"""
    response = read_url(page)

    articles = response.find('.developer--card > a.developer--card__block_link')
    print("\nTotal articles found :", articles.__len__(), ' in Page: ', page)
    for article in articles.items():
        link = article.attr('href')
        articlebody = article.find('div.developer--card__body')
        adate = articlebody.find('h5 > .developer--card__date').text()
        articlebody.find('h5 > .developer--card__date').remove()
        atype = articlebody.find('h5').text().strip()
        title = articlebody.find('h3.developer--card__title').text().encode('utf-8')
        excerpt = articlebody.find('p.developer--card__excerpt').text().encode('utf-8')
        category = article.find('div.developer--card__bottom > p.cpt-byline__categories span')
        if link:
            link = str(link).replace('/announcements/', sourceUrl)
            categories = [span.text for span in category if span.text != '+']
            dataSet.append([link, atype, adate, title, excerpt,",".join(categories)])

if __name__ == '__main__':
    pageUrl = sourceUrl+"category/data-science/?fa=date:DESC&fb="

    pageUrls = [
        sourceUrl+"category/data-science/page/%(page)s?fa=date:DESC&fb=" % {'page': page}
        for page in range(1, 3)]

    for pages in pageUrls:
        get_details(pages)

    print("\nTotal articles collected: ", len(dataSet))
    print(dataSet)
