#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pylab
my_list=[]
for counter in range(10):
    my_list.append(counter*2)
print my_list
print len(my_list)

#now plot the list

pylab.plot(my_list)
pylab.show()
