#!/usr/bin/python
# -*-coding:utf-8 -*-
import subprocess

var='-la'
#subprocess.call('ls',shell=True)
output=subprocess.Popen('ls '+var,shell=True)

