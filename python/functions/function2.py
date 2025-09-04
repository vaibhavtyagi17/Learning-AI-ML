def update_order():
    chai_type="Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type="Adrak"
    kitchen()
    print(chai_type)

update_order()  # This will print "Adrak"

chai_order="Irani"
def update1():
    global chai_order
    chai_order="Masala"
    print(chai_order)
print(chai_order)  # This will print "Irani"
update1()  # This will print "Masala"
print(chai_order)  # This will print "Masala"