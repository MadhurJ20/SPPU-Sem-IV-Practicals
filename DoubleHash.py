'''
Madhur Jaripatke
Roll No. 55
SE A Computer
RMDSSOE, Warje, Pune
'''
class doubleHashTable:
	def __init__(self):
		self.size=int(input("Enter size of contact book "))
		self.table = list(None for i in range(self.size))
		self.num=5
		self.elementcount=0
		self.comparisons=0
	
	def isFull(self):
		if (self.elementcount==self.size):
			return True
		else:
			return False
	
	def display(self):
		print('\n')
		for i in range(self.size):
			print('Hash Value ',str(i)+'\t\t',str(self.table[i]))
		print('\nThe total number of contacts are ',self.elementcount,'\n\n')
	
	def hashfun1(self,element):
		return element % self.size
	
	def hashfun2(self,element):
		return self.num-(element % self.num)
	
	def doubleHashing(self,record,position):
		isFound=False
		limit=self.size
		i=1
		while (i<=limit):
			newPosition=(self.hashfun1(record.get_number()))+i*self.hashfun2(record.get_number())%self.size
			if (self.table[newPosition]==None):
				isFound=True
				break
			else:
				i+=1
		return isFound,newPosition
	
	def insert(self,record):
		if self.isFull()==True:
			print('Table full')
			return False
		isStored=False
		position=self.hashfun1(record.get_number())
		if self.table[position]==None:
			self.table[position]=record
			print('Phone number of',record.get_name(),'is at Hash Value ',str(position))
			isStored=True
			self.elementcount+=1
		else:
			print('Collision encountered for %s\'s number at position %s.\nFinding new position.'%(record.get_name(),str(position)))
			while not isStored:
				isStored,position=self.doubleHashing(record,position)
				if isStored:
					self.table[position]=record
					self.elementcount+=1
					print("Phone number of " + record.get_name() + " is at position " + str(position))
				else:
					print('Error in storing data')
					break
		return isStored
	
	def search(self,record):
		isFound = False
		position = self.hashfun1(record.get_number())
		self.comparisons += 1
		if(self.table[position] != None):
			if(self.table[position].get_name() == record.get_name()):
				print("Phone number found at position {}".format(position) + " and total comparisons are " + str(1))
				return position
			else:
				limit = self.size
				i = 1
				newPosition = position
				while i <= limit:
					position = (self.hashfun1(record.get_number()) + i*self.hashfun2(record.get_number())) % self.size
					self.comparisons += 1
					if(self.table[position] != None):
						if self.table[position].get_name() == record.get_name():
							isFound = True
							break
						elif self.table[position].get_name() == None:
							isFound = False
							break
					else:
						i+=1
				if isFound:
					print("Phone number found at position {}".format(position) + " and total comparisons are " + str(i+1))
				else:
					print("Record not Found")
			return isFound
