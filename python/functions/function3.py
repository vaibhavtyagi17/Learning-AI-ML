def make_chai(tea,milk,sugar):
    print("Making your tea with",tea,milk,sugar)
make_chai("Assam", "whole milk", "2 spoons") #positional
make_chai(tea="Assam",sugar="low",milk="skimmed milk") #keywords
def special_chai(*ingredients,**extras): #* for variable-length argument lists ** for keyword arguments
    print("Ingredients",ingredients)
    print("Extras",extras)
special_chai("whole milk","cardamom",spices="chai masala",sweetness="medium")
def chai_order(order=[]):
    order.append("Masala")
    print(order)
chai_order()
chai_order()