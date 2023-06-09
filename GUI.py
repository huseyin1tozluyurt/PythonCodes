square=[
  [1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1]
]
triangle=[
  [0,0,0,1,0,0,0],
  [0,0,1,0,1,0,0],
  [0,1,0,0,0,1,0],
  [1,1,1,1,1,1,1]
]
tree=[
  [0,0,0,0,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,1,1,1,0,0,0,0,0],
  [0,0,0,0,1,1,1,1,1,0,0,0,0],
  [0,0,0,1,1,1,1,1,1,1,0,0,0],
  [0,0,1,1,1,1,1,1,1,1,1,0,0],
  [0,1,1,1,1,1,1,1,1,1,1,1,0],
  [1,1,1,1,1,1,1,1,1,1,1,1,1],
  [0,0,0,0,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,0,0,0,0,0,0]
]
def sqrfunc():
  for image in square:
    for pixel in image:
      if(pixel==1):
        print("*",end="")
      else:
        print(" ",end="")
    print("")
def trianglefunc():
  for image in triangle:
    for pixel in image:
      if(pixel==1):
        print("*",end="")
      else:
        print(" ",end="")
    print("")
def treefunc():
  for image in tree:
    for pixel in image:
      if(pixel==1):
        print("*",end="")
      else:
        print(" ",end="")
    print("")  
while True:
  decision=str(input("Which image do you want(triangle or square): "))
  if(decision=="Square"):
    sqrfunc()
  if(decision=="Triangle"):
    trianglefunc()
  if(decision=="Close"):
    print("You have closed the programme")
    break
  if(decision=="Tree"):
    treefunc()
