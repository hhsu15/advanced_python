# the property can be really be written as 
# property is using descriptor protocal
class Foo():
	def getter(self):
		print("accessing the attribute")
		return 30

	def setter(self, value):
		print("setting the attribute")
		raise AttributeError("Cannot set value")

	attribute1 = property(getter, setter)

foo = Foo()
print(foo.attribute1)
print('--------------------')

# Descriptor protocal
class OneDigitNumericValue:
	def __init__(self):
		self.value = 0

	def __get__(self, obj, type=None):
		print("getting obj..", obj)  # obj of Foo
		return self.value
	
	def __set__(self, obj, value):
		if value > 9 or value < 0 or int(value) != value:
			raise AttributeError("value is invalid")
		self.value = value

class Foo:
	number = OneDigitNumericValue()

foo = Foo()
foo2 = Foo()

foo.number = 3
print(foo.number) # 3
print(foo2.number) # this will also be 3!
print('-------hmmm not ideal------')

# better solution
class OneDigitNumericValue:
	def __set_name__(self, owner, name): # magic method
		print("---name---", name) # name will be the variable namein string
		self.name = name
		print("---owner---", owner)  # will give you class Foo

	def __get__(self, obj, type=None):
		return obj.__dict__.get(self.name) or 0

	def __set__(self, obj, value):
		obj.__dict__[self.name] = value

class Foo():
	number = OneDigitNumericValue()

foo = Foo()
foo2 = Foo()
foo.number = 5
print(foo.number)
print(foo2.number)
print('-----much better----')
# lazy properties
import time

class LazyProperty:
	def __init__(self, function):
		self.function = function
		self.name = function.__name__

	def __get__(self, obj, type=None):
		# the way this works if the first time it will use the Non-data descriptor and call this method.
		# we then set the attribute with the function name
		# the second time it gets called it will use the obj.<name> to get the data rather than calling this method again
		# if you use data descriptor this will not work because it takes highest precedence
		obj.__dict__[self.name] = self.function(obj) # set the attribute 
		return obj.__dict__[self.name]

class DeepThought:
	@LazyProperty
	def meaning_of_life(self):
		print("thinking....")
		time.sleep(5)
		return 87

my_deep_thought = DeepThought()
print(my_deep_thought.meaning_of_life)
print(my_deep_thought.meaning_of_life)
print(my_deep_thought.meaning_of_life)
print("------that was lazy-----")

class EvenNumber:
	def __set_name__(self, owner, name):
		self.name = name
	
	def __get__(self, obj, type=None):
		return obj.__dict__[self.name]
	
	def __set__(self, obj, value):
		obj.__dict__[self.name] = (value if value % 2 == 0 else 0)

class Values:
	value1 = EvenNumber()
	value2 = EvenNumber()
	value3 = EvenNumber()
	value4 = EvenNumber()
	value5 = EvenNumber()

from operator import attrgetter
my_val = Values()
my_val.value1 = 5
my_val.value2 = 4
my_val.value3 = 10

print(attrgetter('value1', 'value2', 'value3')(my_val))
