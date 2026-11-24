def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
function = outer_function(5)
print(function(4))