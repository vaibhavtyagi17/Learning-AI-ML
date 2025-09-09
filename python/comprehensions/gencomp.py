#for saving memory we use generators
daily_sales=[5,10,12,9,5,3,2,1]
total_sales=sum(sale for sale in daily_sales if sale>=5) #41
print(total_sales)
other_sales=(sale for sale in daily_sales if sale>=5)
print(other_sales) #<generator object <genexpr> at 0x104b5e5e0> gets a stream