#!/usr/bin/python
print ("Content-type: text/html\n\n")
# -*- coding:Utf-8 -*-
import sys

import  sqlalchemy
import pymysql
import pymysql.cursors
import datetime
print (sys.stdout.encoding)
import codecs
#import cStringIO
import pandas as pd
import numpy as np
import pprint 
import json
import ast
from pandas import read_csv
import pymysql.cursors
from sqlalchemy import create_engine
import csv
from sqlalchemy import create_engine
from sqlalchemy import inspect
from pandas.io.json import json_normalize
from pandas import read_csv
import types
import json
#import cgi
import csv
from datetime import datetime
from icalendar import Calendar, Event
#import cgitb
from datetime import date, datetime
import base64
from bs4 import BeautifulSoup
import cgitb
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#from email.MIMEMultipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#cgitb.enable()
import os



cursorcrmb = dbcrmb.cursor()
cursorcrm = dbcrm.connect()


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return str(obj)
			
			
mondict={ "<br />\n": "<br />", "\n": ""}
def replace_all(text, mondict):
    for i, j in mondict.iteritems():
        text = text.replace(i, j)
    return text
sqlpressedb = """\
         
            
            SELECT  
                vtiger_contactdetails.contactid,
                vtiger_contactdetails.contact_no,
                vtiger_contactdetails.accountid,
                vtiger_presse.presseid
            FROM `vtiger_contactdetails`
                INNER JOIN vtiger_presse ON  vtiger_presse.cf_accounts_id = vtiger_contactdetails.accountid
		
	
"""

resultpressedb=cursorcrm.execute(sqlpressedb)
#resultcalendrierb=cursorcrmb.execute(sqlcrmpcalendrier)

resultpresse = resultpressedb.fetchall()

#field_names.remove('Continent')

datacrm = pd.read_sql(sqlpressedb, dbcrm)

dfmdrel=pd.read_excel("/var/www/prog/majcrm/rel_presse_contact.xlsx",encoding='sys.getfilesystemencoding()')





datacrm.replace(regex=True, to_replace =['Ã¡'], value='á' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã€'], value='À' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¤'], value='ä' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã„'], value='Ä' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã£'], value='ã' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¥'], value='å' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã…'], value='Å' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¦'], value='æ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã†'], value='Æ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã§'], value='ç' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã‡'], value='Ç' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã©'], value='é' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã‰'], value='É' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¨'], value='è' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ãˆ'], value='È' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ãª'], value='ê' , inplace=True) 
datacrm.replace(regex=True, to_replace =['ÃŠ'], value='Ê' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã«'], value='ë' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã‹'], value='Ë' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã-­­'], value='í' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã'], value='Í' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¬'], value='ì' , inplace=True) 
datacrm.replace(regex=True, to_replace =['ÃŒ'], value='Ì' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã®'], value='î' , inplace=True) 
datacrm.replace(regex=True, to_replace =['ÃŽ'], value='Î' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¯'], value='ï' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã'], value='Ï' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã±'], value='ñ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã‘'], value='Ñ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã³'], value='ó' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã“'], value='Ó' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã²'], value='ò' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã’'], value='Ò' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã´'], value='ô' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Í´'], value='ô' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã”'], value='Ô' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¶'], value='ö' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã–'], value='Ö' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ãµ'], value='õ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã•'], value='Õ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¸'], value='ø' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã˜'], value='Ø' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Å“'], value='œ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Å’'], value='Œ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['ÃŸ'], value='ß' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ãº'], value='ú' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ãš'], value='Ú' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¹'], value='ù' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã™'], value='Ù' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã»'], value='û' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã›'], value='Û' , inplace=True) 
#datacrm.replace(regex=True, to_replace =['Ã¼'], value='ü' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Í¼'], value='ü' , inplace=True)
datacrm.replace(regex=True, to_replace =['Ãœ'], value='Ü' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â‚¬'], value='€' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€™'], value='’' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€š'], value='‚' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Æ’'], value='ƒ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€ž'], value='„' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€¦'], value='…' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€¡'], value='‡' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ë†'], value='ˆ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€°'], value='‰' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Å'], value='Š' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€¹'], value='‹' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Å½'], value='Ž' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€˜'], value='‘' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€œ'], value='“' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€¢'], value='•' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€“'], value='–' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€”'], value='—' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ëœ'], value='˜' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â„¢'], value='™' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Å¡'], value='š' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€º'], value='›' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Å¾'], value='ž' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Å¸'], value='Ÿ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¡'], value='¡' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¢'], value='¢' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â£'], value='£' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¤'], value='¤' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¥'], value='¥' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¦'], value='¦' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â§'], value='§' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¨'], value='¨' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â©'], value='©' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Âª'], value='ª' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â«'], value='«' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¬'], value='¬' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â®'], value='®' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¯'], value='¯' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â°'], value='°' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â±'], value='±' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â²'], value='²' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â³'], value='³' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â´'], value='´' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Âµ'], value='µ' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¶'], value='¶' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â·'], value='·' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¸'], value='¸' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¹'], value='¹' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Âº'], value='º' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â»'], value='»' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¼'], value='¼' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â½'], value='½' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¾'], value='¾' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Â¿'], value='¿' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã '], value='à' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€'], value='†' , inplace=True) 
datacrm.replace(regex=True, to_replace =['â€'], value='”' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã'], value='Á' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã¢'], value='â' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ã‚'], value='Â' , inplace=True) 
datacrm.replace(regex=True, to_replace =['Ãƒ'], value='Ã' , inplace=True) 
datacrm.replace(regex=True, to_replace =[''], value='' , inplace=True)
datacrm.replace(regex=True, to_replace =['Í¯'], value='ï' , inplace=True)
datacrm.replace(regex=True, to_replace =["\n"], value='' , inplace=True)
datacrm.replace('\n','<br />',inplace=True, regex=True)

writer = pd.ExcelWriter('/var/www/prog/majcrm/outputiliste.xlsx', engine='xlsxwriter')
#print ([column[0] for column in resultscrm])
#print (cursorcrm.description)
datacrm.to_excel(writer,'p')

#worksheet = writer.sheets['pressedb']
writer.save()


datacrm.to_csv('/var/www/prog/majcrm/outputical.csv',index=False,sep=',', date_format='%Y%m%d',quoting=csv.QUOTE_ALL,encoding="UTF-8-SIG", escapechar='\\')

intersec= pd.merge(datacrm, dfmdrel, how='inner', on=['contact_no'])

intersec = intersec.drop('Nom compte', 1)
intersec['module']='Presse'
intersec['relmodule']='Contacts'
intersec = intersec[['presseid', 'module', 'contactid', 'relmodule']]
intersec.rename(columns={'presseid': 'crmid', 'contactid': 'relcrmid'}, inplace=True)
writer = pd.ExcelWriter('/var/www/prog/majcrm/outputinter.xlsx', engine='xlsxwriter')
intersec.to_excel(writer,'p')
writer.save()
#intersec = intersec.drop('contact_no', 1)
#intersec = intersec.drop('accountname', 1)
writer = pd.ExcelWriter('/var/www/prog/majcrm/outputinteraimporter.xlsx', engine='xlsxwriter')
intersec.to_excel(writer,'p')
writer.save()
intersec.to_csv('/var/www/prog/majcrm/outputaimporter.csv',index=False,sep=',', date_format='%Y%m%d',quoting=csv.QUOTE_ALL,encoding="UTF-8-SIG", escapechar='\\')