# scope resolution = local -> enclosed -> global -> built-in

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()