#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 20, 30, 40, 50, 60, 70, 80]
fig = plt.figure()
ax = fig.addsubplot(111)
ax.plot(x, y, color = 'lightblue', linewidth = 3)
ax.scatter([2, 4, 6], [5, 15, 25], color = 'darkgreen', marker = '^')
ax.set_xlim(1, 6.5)
plt.savefig('foo.png')
plt.show()
