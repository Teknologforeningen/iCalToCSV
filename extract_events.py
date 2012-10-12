#!/usr/bin/python
# coding=UTF-8
import sys, re, codecs


print "Extracting events from file:", sys.argv[1]

calendar = codecs.open(sys.argv[1], 'r', 'utf-8')

text = u""
for line in calendar:
    text += line

text = text.replace('\n', '')

match=re.compile('SUMMARY:(.*?)LOCATION:(.*?)DESCRIPTION;(.*?)DTSTART:(\d*?)T').findall(text)



f = open('events.csv', 'w+')

for item, location, crap, date in match:
    date = date[0:4]+"-"+date[4:6]+"-"+date[6:]
    line = date+"\t"+item+"\t"+location+"\n" 
    f.write(line.encode('utf-8'))

f.close()
