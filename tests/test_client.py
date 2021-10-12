from src import client
import ast

client = client.Client("localhost", 3000)
client.connect()

while True:
    command = input("command: ").strip()

    if command == "/close":
        client.close()
        break

    args = []
    kwargs = {}

    while True:
        i = input("arg: ").strip()
        if i == "":
            break
        args.append(ast.literal_eval(i))

    while True:
        i = input("kwarg: ").strip()
        if i == "":
            break

        key, value = i.split("=")
        kwargs[ast.literal_eval(key.strip())] = ast.literal_eval(value.strip())

    try:
        result = client.execute(command, *args, **kwargs)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
