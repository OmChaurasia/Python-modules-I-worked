def dec(function):
	def temp():
		print("hello world")
		function()
		print("thank you")
	return temp
@dec
def myfunc():
	print("I am om")
myfunc()