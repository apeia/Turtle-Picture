import turtle 

t = turtle.Turtle()
sc = turtle.Screen()
sc.setup(960,540)
bgcolor = '#060606'

t.hideturtle()
t.speed(0)
sc.bgcolor(bgcolor)
t.color(bgcolor)

def move(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()


def buttonclick(x,y):
  print(x,y)


def bezier2(a,b,c,d,e,f,color='#ffffff'):
  p0 = turtle.Vec2D(a, b)
  p1 = turtle.Vec2D(c, d)
  p2 = turtle.Vec2D(e, f)
  b = lambda z: p1 + (1 - z)**2 * (p0 - p1) + z**2 * (p2 - p1)
  t.color(color)
  t.penup()
  t.goto(p0)
  t.pendown()
  p = 0
  while p <= 1:
      position = b(p)

      t.setheading(t.towards(position))
      t.goto(position)

      p += 0.1


def bezier3(a,b,c,d,e,f,g,h,color='#ffffff'):
  p0 = turtle.Vec2D(a, b)
  p1 = turtle.Vec2D(c, d)
  p2 = turtle.Vec2D(e, f)
  p3 = turtle.Vec2D(g, h)
  b = lambda z: (1-z)**3*p0+3*(1-z)**2*p1+3*(1-z)**2*p2+(z**3)*p3
  t.color(color)
  t.penup()
  t.goto(p0)
  t.pendown()
  p = 0
  while p <= 1:
      position = b(p)

      t.setheading(t.towards(position))
      t.goto(position)

      p += 0.1


#moon
turtle.onscreenclick(buttonclick, 1)

move(0,-275)

t.begin_fill()
t.fillcolor('#afafaf')
t.circle(250,360)
t.end_fill()














# Ground

move(0,-200)
t.seth(0)


t.begin_fill()
t.fillcolor(bgcolor)
t.fd(300)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(300)
t.end_fill()

t.begin_fill()
t.fillcolor('#fbfbfb')
bezier2(-85,209,148,209,243,26,color='#fbfbfb')
t.seth(102)
t.circle(250,97.5)
t.end_fill()

bezier2(-106,201,146,190,248,-8,color='#f9f9f9')
