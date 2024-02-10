import matplotlib.pyplot as plt
plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def algo(x1,y1,x2,y2):
    dx = abs(x2-x1)
    dy  = abs(y2 - y1)
    x = x1
    y = y1

    plt.plot(x1, y1, 'ro', label='Start Point')
    plt.plot(x2, y2, 'go', label='End Point')

    if dx>dy:
        pk = (2*dy) - dx;
        for i in range(dx):
            x=x+1
            if pk<0:
                pk = pk + (2 *dy)
            else:
                y = y + 1
                pk = pk + (2 * dy) - (2 * dx)
            plt.plot(x, y, 'bo')
    else:
        plt.plot(x, y)
        pk = (2 * dx) - dy
        for i in range(dy):
            y = y+1
            if(pk<0):
                pk = pk + (2 * dx)
            else:
                x = x + 1
                pk = pk + (2 * dx) - (2 * dy)
            plt.plot(x, y, 'bo')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def main():
    x1 = int(input("Enter x1 value: "))
    y1 = int(input("Enter y1 value: "))
    x2 = int(input("Enter x2 value: "))
    y2 = int(input("Enter y2 value: "))
    algo(x1,y1,x2,y2)

if __name__ == "__main__":
    main()