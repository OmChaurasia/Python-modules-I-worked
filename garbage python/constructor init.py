class student:
	id=1
	"""
	def __init__(self, aname, amarks):
        self.name = aname
        self.marks = amarks
      
     """
	def detail(self):
		return f"the marks of {self.name} is {self.marks} "
		"""
		self apne app le lega
		
		"""



om=student()
abc=student()
xyz=student()
om.name="om"
abc.name="abc"
xyz.name="xyz"
om.marks=65
abc.marks=56
xyz.marks=45
print(om.detail())#yaha par object apne pass ho jata hai
print(abc.detail())