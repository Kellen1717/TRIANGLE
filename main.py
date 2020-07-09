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
  Kellen.begin_fill()
  x = 0
  
  while x < 20000000:
    Kellen.forward(length)
    Kellen.right(120)
    Kellen.forward(length)
    Kellen.right(120) 
    Kellen.forward(length)
    Kellen.color('red', 'yellow')
    Kellen.fillcolor()
    
    
    Kellen.right(20)
    x += 1
    Kellen.forward(length)
    Kellen.right(120)
    Kellen.forward(length)
    Kellen.right(120) 
    Kellen.forward(length)
    Kellen.color('purple', 'yellow')
    
    Kellen.right(20)
    x += 1
    Kellen.forward(length)
    Kellen.right(120)
    Kellen.forward(length)
    Kellen.right(120) 
    Kellen.forward(length)
    Kellen.color('green')
    
    Kellen.right(20)
    x += 1
    Kellen.forward(length)
    Kellen.right(120)
    Kellen.forward(length)
    Kellen.right(120) 
    Kellen.forward(length)
    Kellen.color('orange', 'yellow')
    
    Kellen.right(20)
    x += 1
    Kellen.forward(length)
    Kellen.right(120)
    Kellen.forward(length)
    Kellen.right(120) 
    Kellen.forward(length)
    Kellen.color('hot pink', 'yellow')
    
    
    Kellen.right(20)
    x += 1
    Kellen.forward(length)
    Kellen.right(120)
    Kellen.forward(length)
    Kellen.right(120) 
    Kellen.forward(length)
    Kellen.color('blue', 'yellow')
    
    Kellen.right(20)
    x += 1
    Kellen.forward(length)
    Kellen.right(120)
    Kellen.forward(length)
    Kellen.right(120) 
    Kellen.forward(length)
    Kellen.color('yellow', 'yellow')
    
    Kellen.right(5)
    x += 1








    
  Kellen.end_fill()
  
triangle(200)





