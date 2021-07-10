things=["apple","mango","banana",56]
print(things)#to print pura
print(things[1])#to print specific
num=[2,3,2,5,6]
num.sort()#sort karne ke liye
num.reverse()#reverse karne ke liye
print(num)
"""
list me slice usi tarah hota hai jaise string me hota tha
slice karne par original change nahi hota keval print ho jata hai
sort aur reverse original list ko change kar deta hai
list lenth ke liye len esme bhi use hota hai
maximum and minimum bhi find kar sakte hai
append se number add kar sakte hai list me
we can make empty list and add using append
insert se bhi add kar sakte hai
insert me phala index aur dusara value hota hai
pop ka use last element ko remove karta hai
romve specific value ko remove karta hai
mutable can change 
unmutable can not change ex tapal
tapal me []ki jagah () ka use karte hai
"""
print(num[0:5])
print(len(num))
print(max(num))
print(min(num))
num.append(7)
num.insert(1,55)
num.remove(5)
num.pop()
num[1]=45
print(num)
tp=(5,6,7)
print(tp)
a=5
b=6
a,b=b,a
"""
temp var banaye bhina value ko change karna
"""
print(a,b)