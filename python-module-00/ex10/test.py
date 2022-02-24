from loading import ft_progress
from time import sleep
import time 

listy = range(1,3333,1)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
