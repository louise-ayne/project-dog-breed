
import urllib.request as urllib2
from bs4 import BeautifulSoup
import glob
import os


dir = './Annotation'

for dirname in os.listdir(dir):
    print(dirname)
    class_id = dirname.split('-')[1]
    print(class_id)
    fichier = open('./AnnotationYOLO/' + dirname + '.txt', "w")
    listoffile = glob.glob('./Annotation//'+dirname+'/*')
    for filename in listoffile:
        with open(filename, 'r') as fp:
            content = fp.read()
            #print(content)
            soup = BeautifulSoup(content, 'html.parser')
            title = soup.annotation.filename.string
            xmin = soup.annotation.object.bndbox.xmin.string
            xmax = soup.annotation.object.bndbox.xmax.string
            ymin = soup.annotation.object.bndbox.ymin.string
            ymax = soup.annotation.object.bndbox.ymax.string

            fichier.write(title+".jpg "+xmin+","+xmax+","+ymin+","+ymax+","+class_id+"\n")
""" print(soup.title.string)
print(soup.a.string)
print(soup.b.string) """