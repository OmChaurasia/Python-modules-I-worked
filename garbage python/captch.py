import random
import time

list=["1","2","3","4","5","6","7","8","9","0"]
random.shuffle(list)
cap="".join(list[0:6])
print(cap)
t1=time.time()
ucap=(input("enter the captch\n"))
t2=time.time()-t1

if t2>120:
	print("captch expired")
elif cap==ucap:
	print("captch is correct")
else:
	print("captch is not correct")
	