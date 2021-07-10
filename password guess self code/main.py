import math
password="gh"
guess_password =""
guess_array= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']',';',':','<','>','/','?']
checklength=1
for array in guess_array:
    guess_password=array
    for i in guess_array:
        guess_password=guess_password+i
        if guess_password==password:
            print(guess_password)
        break
    if guess_password==password:
        print(guess_password)
        break
