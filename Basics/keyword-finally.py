def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Yo! No division by zero, man!")
    else:
        print("%r over %r equals %r" % (x, y, result))
    finally:
        del x, y
        print("final cleanup finished")
        
#finally is a clause that runs a piece of code at the end of a try-except-clause wether an exception was thrown or not