import turtle 

#game title
turtle.title(" cool Games ")


#game color 
turtle.bgcolor("dark blue")

#setup
turtle.setup(700,700)

turtle.shape("turtle")

screen=turtle.Screen()

Kellen=turtle.Turtle()




def triangle(length):
  Kellen.fillcolor("gold")
  Kellen.begin_fill()
  x = 0
  while x < 4:
    Kellen.forward(length)
    Kellen.right(120)
    x += 1
  Kellen.end_fill()


def triangle(length):
  Kellen.fillcolor("gold")
  Kellen.begin_fill()
  x = 0
  while x < 4:
    Kellen.forward(length)
    Kellen.right(120)
    x += 1
  Kellen.end_fill()
  



triangle(300)






