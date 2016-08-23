#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jeffrey Sun'

from datetime import datetime
import os

def dir_l(pwd = '.'):
    print('           Size    Last Modified Name')
    print('--------------------------------------------')

    for f in os.listdir(pwd):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        flag = '/' if os.path.isdir(f) else ''
        print('%10d %s %s%s' % (fsize,mtime,f,flag))

def find_str(str,path = '.'):
    def print_path(t_path):
        if t_path.find(str) >= 0:
            print(os.path.abspath(t_path))

    for f in os.listdir(path):
        f = os.path.join(path,f)
        print_path(f)
        if os.path.isdir(f):
            find_str(str,f)

if __name__=='__main__':
    dir_l()
    find_str('test')
