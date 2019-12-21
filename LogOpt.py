#!/usr/bin/python
# -*- coding: utf-8 -*-
#LogOpt.py

from __init__ import *
import DataOpt

#日志类
class LogOptBase(object):
  def __init__(self):
    print("LogOptBase_init...")
    
    #创建日志器，设置其日志级别为DEBUG
    self.user = getpass.getuser()
    self.logger = logging.getLogger(self.user)
    self.logger.setLevel(logging.DEBUG)
    
    #创建一个流处理器handler并设置其日志级别为DEBUG
    self.logHandler = logging.StreamHandler()
    self.logHandler.setLevel(logging.DEBUG)
    
    #创建一个格式器formatter并将其添加到处理器handler
    self.formatter = logging.Formatter('%(asctime)s - %(filename)s - line:%(lineno)d [%(levelname)s] %(message)s')
    self.logHandler.setFormatter(self.formatter)

    #定义日志文件器，显示到屏幕并输出到文档
    #args = ('Log/' + os.path.basename(sys.argv[0]).split(".")[0], 'midnight', 1, 365)
    LPathYmday = sys.path[0] + '\\logs\\' + DataOpt.DataOptBase.DateToStr(datetime)
    print(LPathYmday)
    if not os.path.exists(LPathYmday):
      os.makedirs(LPathYmday)
    LogPath = LPathYmday + '\\' + 'dytt_spider.log'
    self.logHand = logging.FileHandler(LogPath, encoding='utf-8')
    self.logHand.setFormatter(self.formatter)
    self.logHand.setLevel(logging.DEBUG)

    # 为日志器logger添加上面创建的处理器handler
    self.logger.addHandler(self.logHand)
    self.logger.addHandler(self.logHandler)
    
  
  def debug(self, msg):
    self.logger.debug(msg)
  
  def info(self, msg):
    self.logger.info(msg)

  def warn(self, msg):
    self.logger.warning(msg)
    
  def error(self, msg):
    self.logger.error(msg)
  
  def fatal(self, msg):
    self.logger.fatal(msg)
    
  def LogOptPrint(self):
    print("LogOptBase init  Complete...")

# if __name__ == '__main__':
#   mylog = LogOptBase()
#   mylog.debug('I am 测试中文')
#   mylog.info("I am info")
#   mylog.warn("warning")
#   mylog.error("Error")
#   mylog.fatal("this is a fatal")