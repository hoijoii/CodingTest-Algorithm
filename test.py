

def func():
    a = 10

    def prac():
      nonlocal a
      a+=10
      print(a)

    prac()



func()