from src import server

server = server.Server("localhost", 3000)


@server.register("hi")
def a():
    return "hello"


@server.register("add")
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


@server.register("multiply")
def multiply(*args):
    product = 1
    for i in args:
        product *= i
    return product


server.run()
