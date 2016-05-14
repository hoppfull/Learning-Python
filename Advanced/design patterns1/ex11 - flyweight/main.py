"""Flyweight Design Pattern (Made in Python 3.4.3)

This makes sure that only a minimal amount of instances are stored in
memory. Duplicates simply reference same object. This only seems useful
in very special cases. Cases when objects can't change but are merely a
collection of static and unchanging objects. This could perhaps be
combined with other parts that are not flyweights.

This can be combined with keeping an array with differing properties.
Example:
  Store an array with thousands of positions but only one draw-method.

"intrinsic" state: shared properties
"extrinsic" state: unique properties
"""
import weakref


class Flyweight1:
	# weakref makes sure memory is cleared after all objects with same
	# properties are gone:
	_stack = weakref.WeakValueDictionary()
	
	def __new__(cls, *args):
		obj = Flyweight1._stack.get(str(args), None)
		if not obj:
			print("Created new:", str(args))
			obj = super(Flyweight1, cls).__new__(cls)
			Flyweight1._stack[str(args)] = obj
			obj.value = args[0]
		return obj
	

if __name__ == "__main__": # Client code:
	ob0 = Flyweight1(2)
	ob1 = Flyweight1(2)
	ob2 = Flyweight1(2)
	ob3 = Flyweight1(2)
	ob4 = Flyweight1(3)
	
	del ob0
	
	# print(ob0.value) ## Error!
	print(ob1.value)
	print(ob2.value)
	print(ob3.value)
	print(ob4.value)
	