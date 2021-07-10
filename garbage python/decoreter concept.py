def function(func1):
	def func2():
		print("executing")
		func1()
		print("executed")
	return func2()

@function#decorater concept
def add():
	print("hello world")
