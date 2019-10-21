from pyquery import PyQuery as pq
import re 

if __name__ == '__main__':
    # reading file
    xmlFile = open('sitemap.xml', 'r').read()   

#creating PyQuery object using parser 'xml'
urlXML = pq(xmlFile, parser='xml')

print("Children Length: ",urlXML.children().__len__())

print("First Children: ", urlXML.children().eq(0))
print("Inner Child/First Children: ", urlXML.children().children().eq(0))

dataSet=list()

for url in urlXML.remove_namespaces().children().find('loc:contains("blog")').items():
    dataSet.append(url.text())

print("Length of dataSet: ", len(dataSet))
print(dataSet)


blogXML = re.split(r'\s',urlXML .children().text())
print("Length of blogXML: ",len(blogXML))

#filter(), filters URLs from blogXML that matches string 'blog'
dataSet= list(filter(lambda blogXML:re.findall(r'blog',blogXML),blogXML))
print("Length of dataSet: ",len(dataSet))
print("Blog Urls: ",dataSet)