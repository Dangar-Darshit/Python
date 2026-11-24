def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()