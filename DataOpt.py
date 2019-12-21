#!/usr/bin/python
# -*- coding: utf-8 -*-
#DataOpt.py

import datetime,time

#日期和时间处理
class DataOptBase:
  def __init__(self):
    print("DataOptBase_init")

  def DataOptPrint(self):
    print("DataOptBase")

#取当前日期
  def GetCurDate(self):
    return datetime.date.today()

#把当前日期转化成字符串，返回：“20190328”
  def DateToStr(self):
    return time.strftime("%Y%m%d")

#把字符串转化成日期，参数：“20190328”
  def StrToDate(self, date):
    year_date = date[0:4]
    mon_date = date[4:6]
    day_date = date[6:]
    return datetime.datetime(int(year_date), int(mon_date), int(day_date))

#是否和当前日期匹配，参数：“20190328”
  def isToday(self,date):
    if (self.DateToStr() == date):
      return True
    else:
      return False
