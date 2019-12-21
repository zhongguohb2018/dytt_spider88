#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import getpass
import datetime,time
import os,sys,platform

if str(platform.python_version()).startswith("3"):
  from importlib import reload
  reload(sys)
else:
  reload(sys)
  sys.setdefaultencoding('utf8')
  print("init OK!")

import FileOpt as FileOpt
import RegOpt as RegOpt
import NetOpt as NetOpt
import LogOpt as LogOpt
import DataOpt as DataOpt
import SysOpt as SysOpt
import ThreadOpt as ThreadOpt
import ErrOpt as ErrOpt

