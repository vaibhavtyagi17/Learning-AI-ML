from pydantic import BaseModel
class Product(BaseModel):
    id:int
    name:str
    price:float
    is_stock:bool=True
product_one=Product(id=1,name="Laptop",price=999.99,in_stock=True)
print(product_one)