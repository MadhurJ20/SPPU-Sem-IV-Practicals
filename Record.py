'''
Madhur Jaripatke
Roll No. 55
SE A Computer
RMDSSOE, Warje, Pune
'''
class Record:
	def __init__(self):
		self.name=None
		self.number=None
	def get_name(self):
		return self.name
	def get_number(self):
		return self.number
	def set_name(self,name):
		self.name=name
	def set_number(self,number):
		self.number=number
	def __str__(self):
		record='Name: '+str(self.get_name())+'\t'+'Number: '+str(self.get_number())
		return record
