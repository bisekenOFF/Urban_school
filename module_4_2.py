

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

# inner_function() - вызов не сработает

test_function() #а такой работать будет