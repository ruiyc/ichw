def main():
    import turtle
    import math
    t=turtle.Pen()
    t.hideturtle()
    t.dot("red")
    a=list(range(6))
    b=list(range(6))
    c=list(range(6))
    for i in range(6):
        a[i]=i+1
        b[i]=a[i]*4/5
        c[i]=a[i]*3/5
    pen=list(range(6))
    colors=["blue","orange","green","gray","yellow","purple"]
    for j in range(6):
        pen[j]=turtle.Pen()
        pen[j].color(colors[j])
        pen[j].turtlesize(0.5) 
        pen[j].shape("circle")
        pen[j].penup()
        pen[j].forward(30*(a[j]-c[j]))
        pen[j].pendown()
    for l in range(1000):
        for s in range(6):
            pen[s].goto(30*(a[s]*math.cos(l/(a[s]+10))-c[s]),30*b[s]*math.sin(l/(a[s]+10)))
if __name__ == '__main__':
    main()
