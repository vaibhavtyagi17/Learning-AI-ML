tea_prices_inr={
    "Iced lemon tea": 100,
    "Masala Chai": 80,
    "Ginger Chai": 90,
    "Lemon Chai": 70,
    "Kadak Chai": 60
}
to_dollar={tea:price/80 for tea,price in tea_prices_inr.items()}
print(to_dollar)