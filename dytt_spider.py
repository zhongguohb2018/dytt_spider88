#!/usr/bin/python
# -*- coding: utf-8 -*-
#dytt_spider.py

from __init__ import *



##电影天堂爬虫程序:
#1.爬取电影天堂首页每日最新资源
#2.写本地文件并上报数据库作为索引库

def dytt_spider_main():
  #文件操作
  FileOptBase = FileOpt.FileOptBase()
  FileOptBase.FileOptPrint()
  #正则操作
  RegOptBase = RegOpt.RegOptBase()
  RegOptBase.RegOptPrint()
  #网络操作
  NetOptBase = NetOpt.NetOptBase()
  NetOptBase.NetOptPrint()
  #日志操作
  LogOB = LogOpt.LogOptBase()
  LogOB.debug(sys.argv[0][-15:-1])
  LogOB.LogOptPrint()
  
  #日期和时间
  DataOptBase = DataOpt.DataOptBase()
  DataOptBase.DataOptPrint()
  DataOptBase.isToday(20190411)

  #系统资源管理
  SysOptBase = SysOpt.SysOptBase()
  SysOptBase.SysOptPrint()
  #多线程
  ThreadOptBase = ThreadOpt.ThreadOptBase()
  ThreadOptBase.ThreadOptPrint()
  #异常处理
  ErrOptBase = ErrOpt.ErrOptBase()
  ErrOptBase.ErrOptPrint()





if __name__ == '__main__':
  dytt_spider_main()