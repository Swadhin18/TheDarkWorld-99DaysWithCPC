x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
def mynew():
  global x
  x = "fantanstic"
myfunc()
mynew()
print("Python is " + x)
