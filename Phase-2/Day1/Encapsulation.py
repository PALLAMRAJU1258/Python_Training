"""
1)class variable can be accessed inside the method using keyword self
2)instance variable can be access out side the class using obj_name.var_name
3)variable inside method are having local scope so we can't use outside the
class
Encapulation:
It provide data security
1)public
2)private
3)protected

"""
class happy:
    a=100
    def method(self):
        b=12
        print(self.a)
        print(b,end="\n\n")
obj=happy()
print(obj.a)
obj.method()


#protected 
"""
protected  syntax: _variable
protected can't access outside the class however can be accessed by derived
class of that class
"""
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Encap function-accessing protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c,end="\n\n")

#private
"""
private syntax: __variable
"""
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("Encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)
#will throw error
#bcs a is private, can't be accessed outside class
        
    
