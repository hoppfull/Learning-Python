with open("text.txt", "r") as text:
    x = text.read()

print(x)

# with makes sure that the loaded resources are closed almost no matter what. Good practice I think.