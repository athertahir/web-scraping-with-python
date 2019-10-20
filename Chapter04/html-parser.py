from pyquery import PyQuery as pq

if __name__ == '__main__':
    # reading file
    xmlFile = open('sitemap.xml', 'r').read()   

# creating PyQuery object using parser 'html'
urlHTML = pq(xmlFile, parser='html')

print("Children Length: ",urlHTML.children().__len__())
print("First Children: ",urlHTML.children().eq(0))
print("Inner Child/First Children: ",urlHTML.children().children().eq(0))

dataSet=list()
for url in urlHTML.children().find('loc:contains("blog")').items():
    dataSet.append(url.text())

print("Length of dataSet: ", len(dataSet))
print(dataSet)