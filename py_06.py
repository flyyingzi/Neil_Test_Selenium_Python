__author__ = 'wei'

#coding:utf-8
import urllib
import  time
i = 0
url = [''] * 10
title_name = [''] * 10
url_home = 'http://www.v2ex.com'
con = urllib.urlopen(url_home).read()
topic = con.find(r'item_hot_topic_title')
href = con.find(r'<a href=', topic)
href_end = con.find(r'>', href)
title = con.find(r'</a>', href_end)

while title != -1 and href_end != -1 and href != -1 and topic != -1 and i < 10:
    title_name[i] = con[href_end + 1:title]
    url[i] = url_home + con[(href + 9):(href_end - 1)]
    print title_name[i], url[i]
    topic = con.find(r'item_hot_topic_title', title)
    href = con.find(r'<a href=', topic)
    href_end = con.find(r'>', href)
    title = con.find(r'</a>', href_end)
    i += 1
else:
    print ('find end')
j = 0
while j < i:
    content = urllib.urlopen(url[j]).read()
    open(r'v2ex/'+str(j+1).zfill(2)+'_'+url[j][-6:] + '.html', 'w+').write(content)
    j += 1
    time.sleep(10)
else:
    print ('download complete')







