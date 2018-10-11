'''Non-data descriptor'''
class LazyProperty(object):
    def __init__(self, func):
        self._func = func
        self.__name__ = func.__name__
        
    def __get__(self, obj, klass):
        print("called the function") #you will get this only the first time you get the property
        result = self._func(obj)
        obj.__dict__[self.__name__] = result
        return result
        
class MyClass(object):
    @LazyProperty
    def x(self):
        return 42

'''data descriptor'''
# this is the rule #1 the highest priority
class MyDescriptor(object):
	def __get__(self, obj, type):
		print(self, obj, type)
	def __set__(self, obj, value):
		print("Got %s" % value)

class MyClass2(object):
	x = MyDescriptor() # attached at class definition
	pass
"""
obj = MyClass2()
obj.x # "will print self, obj, type"
obj.x = 4 # "Got 4"
"""
