__author__ = 'wei'

#coding:utf-8
import urllib
import time
import os
from HTMLParser import HTMLParser

def strip_tags(html):
    html = html.strip()
    html = html.strip("\n")
    result = []
    parse = HTMLParser()
    parse.handle_data = result.append
    parse.feed(html)
    parse.close()
    return "".join(result)

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
time_file = time.strftime('%y%m%d-%H%M%S', time.localtime())
folder_full = os.getcwd() + '\\'+'v2ex'+'\\'+time_file+'\\'
os.makedirs(r'%s' % folder_full)
print ('new file complete')

while j < i:
    content = urllib.urlopen(url[j]).read()
    content_start = content.find(r'topic_content">')
    content_end = content.find(r'</div>', content_start)
    content_page = content[(content_start+len('topic_content">')): content_end]
    content_page = strip_tags(content_page)
    open(folder_full+str(j+1).zfill(2)+'_'+url[j][-6:] + '.txt', 'w+').write(content_page)
    print ('%d page(s) download complete' % (j+1))
    j += 1
    time.sleep(7)

else:
    print ('all download complete, there are %d pages' % j)




