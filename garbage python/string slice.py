str="hello world"
print(len(str))#string ki lenth
print(str[4])#print karo 5va character
print(str[0:5])#0,1,2,3,4 char ko print karo
print(str[0:5:2])#skip one character
print(str[::])#by default zero char skip, pura lega
print(str[0:56])#pura le le ga
print(str[:])#pura le le ga , by default pura
print(str[:5])#by default 0
print(str[0:])#by default pura
print(str[-5:])#piche se 5 char
print(str[-5:-2])#piche se 5 se 3char
print(str[::-1])#reverse string
print(str[::-2])#reverse and skip 2
print(str.count("o"))#count how many stri
print(str.find("ll"))#find from where this began
print(str.upper())#upper & lower case func
print(str.endswith("world"))#boolen function
print(str.replace("wor","ho"))#to replace
print(str.capitalize())#capital first char
print(type(str))#check the datatype of var
print("hello world",end=" ")
print("hello",str)