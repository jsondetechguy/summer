add = lambda x,y: x + y
sub = lambda x,y: x - y
div = lambda x,y: x / y
mul = lambda x,y: x * y
x = input("what is x")
y = input("what is y")
act = input("plus, min, div, mul? (p, m, d, m)")

if act == "p":
    print(add(int(x), int(y)))
elif act == "m":
    print(sub(int(x), int(y)))
elif act == "d":
    print(div(int(x), int(y)))
elif act == "m":
    print(mul(int(x), int(y)))
else:
    print("bro what you talking about")