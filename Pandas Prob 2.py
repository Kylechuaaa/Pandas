import pandas as pd

P2a = data.iloc[[0,1,2,3,4],[0,2,4,6,8,10]]
P2b = data.ix[0]
P2c = data.iloc[[23],[0,2,10]]
P2d = data.iloc[[1,28,18],[0,2,10]]

print ('A:\n', P2a)
print ('\n B: \n', P2b)
print ('\n C: \n', P2c)
print ('\n D: \n',P2d)