#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

my_birthdate = datetime.date(1979,3,12)
my_birthtime = datetime.time(6,0)
my_birthday = datetime.datetime.combine(my_birthdate, my_birthtime)
now = datetime.datetime.now()

time_passed = now - my_birthday
how_many_seconds = time_passed.total_seconds()
print (how_many_seconds)
