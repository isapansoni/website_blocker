#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 10:46:12 2017

@author: sapansoni
"""

import time 
from datetime import datetime as dt

host_temp="hosts"
hostfile = r"/etc/hosts"    #r is used to avoid special charecter
redirect= "127.0.0.1"
website_list=["facebook.com","www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):    
        print ("Working hours")
        with open(host_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " + website+"\n")
    else:
        with open (host_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()        
        print("fun hours")
    time.sleep(5)
    
