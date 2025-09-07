menu=[
    "Iced lemon tea",
    "Masala Chai",
    "Ginger Chai",
    "Lemon Chai",
    "Kadak Chai",
]
ans=[tea for tea in menu if len(tea)<12]
print(ans)
iced_tea=[tea for tea in menu if "Iced" in tea]
print(iced_tea)