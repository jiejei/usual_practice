#!/usr/bin/python
#encoding=utf-8
#fun:通过备份日志文件里记录的时间，找出备份时间大于5分钟的数据库名称
#时间匹配格式:"%Y-%m-%d %H:%M:%S"
#ceshi

import datetime,time,commands,os,sys

if len(sys.argv) != 3:
    print "Usage:\t\033[1;32m python %s -f file\033[0m" % sys.argv[0]
    sys.exit(1)

file_name = sys.argv[2]   #记录文件
#文件格式:2018-03-02 08:41:32 - start dump dbname

def dateDifflnSeconds(date1,date2):
    # timedelta = date2 - date1
    # 将字符串格式的时间转换为datetime的格式后，进行减法运算
    timedelta = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    return timedelta.days * 24 * 3600 + timedelta.seconds

file_len = commands.getoutput("wc -l %s | awk '{print $1}'" %file_name)
i = 1

while 1:
    if i > int(file_len):
        sys.exit(1)
    cmd1 = "sed -n '%sp' %s | awk '{print $1,$2}'" % (i,file_name)
    date1 = commands.getoutput(cmd1)
    cmd2= "sed -n '%sp' %s | awk '{print $1,$2}'" % ((i+1),file_name)
    date2 = commands.getoutput(cmd2)
    time_diff = dateDifflnSeconds(date1,date2)
    if time_diff > 300:
        # print "\ntime_diff is %s" % time_diff
        m, s = divmod(time_diff, 60)
        h, m = divmod(m, 60)
        print "\n%02d:%02d:%02d" % (h, m, s)
        os.system("sed -n '%sp' %s | awk '{print $6}'" % (i,file_name))
    i = i + 3
