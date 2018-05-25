import urllib2

url = raw_input("Enter the URL to scan: ")
domain = url[:-4]    # to remove other domains
url = "http://www." + url

while True:
    response = urllib2.urlopen(url)
    if response.code == 200:
        doc = response.read()
        break
#print doc
counter = 0    # Document Counter
subs = set()

while True:
    start = counter + doc[counter:].find('href="http://')
    end = start + doc[start:].find(".com")
    if start - counter == -1:
        break
    temp = doc[start + 13:end + 4]
    #Larger lengths usually return in faulty results
    if temp.find(".com") != -1 and temp.find("."+domain+".") != -1 and end-start <= 40:
        subs.add(temp)
    counter = counter + (end-start) + 5

for url_item in sorted(subs):
    print url_item