#!/usr/bin/python
# -*- coding: utf-8 -*

print ("Content-type: text/html\n\n")

import sys
from itertools import zip_longest
import cgi
import os, errno ,sys ,glob
import pprint 
import json
import ast
import csv


print("---------------------------------------")
#print(dfmdcsv2)
dictinter=set(dfmdcsv1['Nom compte']).intersection(set(dfmdcsv2['Nom compte']))
#print(dictinter)
dfmdinter2 =pd.merge(dfmdcsv1nc, dfmdcsv2nc, how='inner')
print(dfmdinter2)
print("---------------------------------------")
print(dfmdcsv1nc)
print("---------------------------------------")
print(dfmdcsv2nc)



f = open('FuzzyMatch2.csv', 'wt')
writer = csv.writer(f, lineterminator = '\n')




file1 = csv.DictReader(open(file1_loc, 'r'))
file2 = csv.DictReader(open(file2_loc, 'r'))

for row in file1:
    for l1, l2 in zip_longest(file1, file2):
        if all((l1, l2)):
            partial_ratio = fuzz.token_sort_ratio(str(l1['Nom compte']), str(l2['Nom compte']))       

        a = [l1,l2,partial_ratio]
        writer.writerow(a)

f.close()

