def outer_function(x):
    def inner_function():
        print(x)
    return inner_function

function1 = outer_function(1)
function2 = outer_function(2)

function1()
function2()

#This is interesting. We can create custom functions with hardcoded elements. Apparently the uses are numerous

#Read more here!
#http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
