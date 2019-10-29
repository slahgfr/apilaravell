
import sys
import cgi
import os, errno ,sys ,glob
import datetime
print (sys.stdout.encoding)
import codecs






fobj = open("/var/www/prog/majcrm/testajout.txt","w+", encoding='utf-8')
for i in range(10):
     fobj.write("cette  ligne %d\r\n" % (i+1))
fobj.close() 
fobj = open("/var/www/prog/majcrm/testajout.txt","a+", encoding='utf-8')
for i in range(5):
     fobj.write("ajout  cette  ligne %d\r\n" % (i+1))
fobj.close() 