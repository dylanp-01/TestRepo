y: int = 30
x: int = 40

def newlayer(y: int, x: int, fill: str = ""):
    layer = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(fill)
        layer.append(row)
    return layer

def printlayer(layer, deliminator: str = "\n"):
    string = ""
    for y in range(len(layer)):
        for x in range(len(layer[y])):
            string += layer[y][x]
        string += deliminator

    print(layer)

screen = newlayer(y, x, "#")
printlayer(screen)
