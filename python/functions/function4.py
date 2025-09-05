def make_chai():
    return "Here is your chai!"
print(make_chai())

return_value=make_chai()
print(return_value)

def maker():
    return 10,20,30
a,b,_=maker()
print(a,b)