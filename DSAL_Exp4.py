'''
Madhur Jaripatke
Roll No. 55
SE A Computer
RMDSSOE, Warje, Pune
'''
'''To create ADT that implement the "set" concept.
a. Add (new Element) -Place a value into the set
b. Remove (element) Remove the value
c. Contains (element) Return true if element is in collection
d. Size () Return number of values in collection Iterator () Return an iterator used to loop over collection
e. Intersection of two sets
f. Union of two sets
g. Difference between two sets
h. Subset'''
from SetOperations import Set
def createSet():
	n=int(input("Enter Number of Elements in Set "))
	s=Set(n)
	return s
choice=0
print("Creating Set")
s1=createSet()
print(str(s1))
while choice!=10:
	print("Menu")
	print("1.Add")
	print("2.Remove")
	print("3.Contains")
	print("4.Size")
	print("5.Intersection")
	print("6.Union")
	print("7.Difference")
	print("8.Subset")
	print("9.Proper Subset")
	print("10.Exit")
	choice=int(input("Please Enter Your Choice "))
	if choice==1:
		e=int(input("Enter Number To Add "))
		s1.add(e)
		print(str(s1))
	elif choice==2:
		e=int(input("Enter Number To Remove "))
		s1.remove(e)
		print(str(s1))
	elif choice==3:
		e=int(input("Enter Number to Search "))
		if e in s1:
			print("Number is present in Set")
		else:
			print("Number is not present In Set")
	elif choice==4:
		print("Set contains {} Elements".format(len(s1)))
	elif choice==5:
		print("Create a Set B for Intersection Operation")
		s2=createSet()
		s3=s1.intersect(s2)
		print("Set A="+str(s1))
		print("Set B="+str(s2))
		print("Intersection="+str(s3))
	elif choice==6:
		print("Create a Set B for Union Operation")
		s2=createSet()
		s3=s1.union(s2)
		print("set A="+str(s1))
		print("Set B="+str(s2))
		print("Union="+str(s3))
	elif choice==7:
		print("Create a set B for calculating Set Difference")
		s2=createSet()
		s3=s1.difference(s2)
		print("Set A="+str(s1))
		print("Set B="+str(s2))
		print("Difference="+str(s3))
	elif choice==8:
		print("Create a Set B for checking Subset")
		s2=createSet()
		isSubset=s1.isSubsetOf(s2)
		print("Set A="+str(s1))
		print("Set B="+str(s2))
		if isSubset:
			print("Set B is a Subset of Set A")
		else:
			print("Set B is not a Subset Of set A")
	elif choice==9:
		print("Create A set B for checking Proper Subset")
		s2=createSet()
		isProperSubset=s1.isProperSubset(s2)
		print("Set A="+str(s1))
		print("Set B="+str(s2))
		if isProperSubset:
			print("Set B is a Proper Subset of Set A")
		else:
			print("Set B is not A Proper Subset of Set A")
	elif choice==10:
		break;
	else:
		print("Please Enter A Valid Choice")
