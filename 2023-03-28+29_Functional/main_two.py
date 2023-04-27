def outer():
    def inner():
        print("I am function inner()!")

    # Function outer() returns function inner()
    return inner #-------THIS IS MOST IMPORTANT!!!--------


function = outer()
print(function)
# <function outer.<locals>.inner at 0x7f18bc85faf0>
function()
# I am function inner()!

outer()()
# I am function inner()!