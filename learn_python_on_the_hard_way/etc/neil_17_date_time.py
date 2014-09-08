#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 05
"""

# 引自：http://www.w3cschool.cc/python/python-date-time.html


"""
# 17.1 时间和日期
转换日期格式是一个常见的例行琐事。Python有一个time and calendar模组可以帮忙。
"""


"""
# 17.2 什么是时间元组
很多Python函数用一个元组装起来的9组数字处理时间:
0	4位数年	2008
1	月	1 到 12
2	日	1到31
3	小时	0到23
4	分钟
5	秒	0到61 (60或61 是闰秒)
6	一周的第几日	0到6 (0是周一)
7	一年的第几日	1到366 (儒略历)
8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜
"""
"""
也就是struct_time元组。这种结构具有如下属性：
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	1 到 366(儒略历)
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
"""


"""
# 17.3 获取当前时间
从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
"""
import time
print "---------17.3-start---------"
localtime = time.localtime(time.time())
print "浮点数的时间：", time.time()
print "Local current time :", localtime
print "---------17.3-end---------"


"""
# 17.4 获取格式化的时间
你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
"""
print "---------17.4-start---------"
localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime
print time.strftime('%y%m%d-%H%M%S', time.localtime(time.time()))
print "---------17.4-end---------"


"""
# 17.5 获取某月日历
Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
"""
import calendar

print "---------17.5-start---------"
cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal
print "---------17.5-end---------"


"""
# 17.6 Time模块
Time模块包含了以下内置函数，既有时间处理相的，也有转换时间格式的：

time.altzone
返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。

time.asctime([tupletime])
接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。

time.clock( )
用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。

time.ctime([secs])
作用相当于asctime(localtime(secs))，未给参数相当于asctime()
接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0

time.localtime([secs])
接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。

time.mktime(tupletime)
接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。

time.sleep(secs)
推迟调用线程的运行，secs指秒数。

time.strftime(fmt[,tupletime])
接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。

time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
根据fmt的格式把一个时间字符串解析为时间元组。

time.time( )
返回当前时间的时间戳（1970纪元后经过的浮点秒数）。

time.tzset()
根据环境变量TZ重新初始化时间相关设置。

******重要的*******
time.timezone
属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。

time.tzname
属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。
"""


"""
# 17.7 日历（Calendar）模块

calendar.calendar(year,w=2,l=1,c=6)
返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。

calendar.firstweekday( )
返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。

calendar.isleap(year)
是闰年返回True，否则为false。

calendar.leapdays(y1,y2)
返回在Y1，Y2两年之间的闰年总数。

calendar.month(year,month,w=2,l=1)
返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。

calendar.monthcalendar(year,month)
返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。

calendar.monthrange(year,month)
返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。

calendar.prcal(year,w=2,l=1,c=6)
相当于 print calendar.calendar(year,w,l,c).

calendar.prmonth(year,month,w=2,l=1)
相当于 print calendar.calendar（year，w，l，c）。

calendar.setfirstweekday(weekday)
设置每周的起始日期码。0（星期一）到6（星期日）。

calendar.timegm(tupletime)
和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。

calendar.weekday(year,month,day)
返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
"""





