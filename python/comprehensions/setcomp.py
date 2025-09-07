chais=[
    "ginger",
    "masala",
    "lemon",
    "kadak",
    "green",
    "ginger",
    "kadak"
]
unique_chai={chai for chai in chais}
print(unique_chai)
other_chai={chai for chai in chais if(len(chai)<6)}
print(other_chai)

chais_ing={
    "Masala chai":["ginger","cardamom","clove"],
    "Elaichi chai":["cardamom","milk"],
    "Spicy chai":["ginger","clove","black pepper"]
}
all_ing={spice for ingredients in chais_ing.values() for spice in ingredients}
print(all_ing)