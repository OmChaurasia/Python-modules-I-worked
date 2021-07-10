class student:
	subject=["maths","hindi","english","science"]
	#yaha par jo variable banta hai vo class variable hota hai 
	#in variable ko object ke dwara bhi use kiya ja sakta hai
	pass
	
ram=student()
shyam=student()
ram.name="Ram"
#object dwara banaye gaye variable ko instance variable kahte hai
ram.rollno=23
shyam.name="Shyam"
shyam.rollno=45
print(ram.name)
print(ram.subject[0])
print(ram.__dict__)
#this will print the dictionary of all instance variable of object