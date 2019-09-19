#!/usr/bin/python3
# -*- coding: utf-8 -*-


def my_function(country = "Norway, Sweden, India, Brasil"):
    print("I am from " + country)


my_function()



def my_function(country = "Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
