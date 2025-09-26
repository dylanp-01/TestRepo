y: int = 30
x: int = 40

class layer:
  
    data = []

    def __init__(self, y: int, x: int, fill: str = ""):
        newlayer = []
        for i in range(y):
            row = []
            for j in range(x):
                row.append(fill)
            newlayer.append(row)
        self.data = newlayer

    def __str__(self, deliminator: str = "\n"):
        string = ""
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                string += self.data[y][x]
            string += deliminator
        return string

    def changepixel(self, y: int, x: int, to: str):
        self.data[y][x] = to

screen = layer(y, x, "#")
print(screen)

screen.changepixel(3, 3, ".")
print("changed 3, 3 to .")

print(screen)
