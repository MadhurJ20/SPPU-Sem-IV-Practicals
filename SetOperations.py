'''
Madhur Jaripatke
Roll No. 55
SE A Computer
RMDSSOE, Warje, Pune
'''
class Set :
    def __init__( self, initElementsCount ):
        self._s = []
        for i in range(initElementsCount) :
            e = int(input("Enter Element {}: ".format(i+1)))
            self.add(e)
    def get_set(self):
        return self._s
    def __str__(self):
        string = "\n{ "
        for i in range(len(self.get_set())):
            string = string + str(self.get_set()[i])
            if i != len(self.get_set())-1:
                string = string + " , "
        string = string + " }\n"
        return string
    def __len__( self ):
        return len( self._s )
    def __contains__( self, e ):
        return e in self._s
    def isEmpty( self ):
        return len(self._s) == 0
    def add( self, e ):                  
        if e not in self :
            self._s.append( e )
    def remove( self, e ):
        if e in self.get_set():
            self.get_set().remove(e)
    def __eq__( self, setB ):                 
        if len( self ) != len( setB ) :
            return False
        else :
            return self.isSubsetOf( setB )
    def isSubsetOf( self, setB ):           
     for e in setB.get_set() :
         if e not in self.get_set() :
             return False
     return True
    def isProperSubset( self, setB ):
        if self.isSubsetOf(setB) and not setB.isSubsetOf(self):
            return True
        return False
    def union( self, setB ):                 
     newSet = self  
     for e in setB :
         if e not in self.get_set() :
             newSet.add(e)
     return newSet
    def intersect( self, setB ):
        newSet = Set(0)
        for i in range(len(self.get_set())) :
            for j in range(len(setB.get_set())) :
                if self.get_set()[i] == setB.get_set()[j] :
                    newSet.add(self.get_set()[i])
        return newSet
    def difference( self, setB ):
        newSet = Set(0)
        for e in self.get_set() :
            if e not in setB.get_set():
                newSet.add(e)
        return newSet
    def __iter__( self ):
        return iter(self._s)
