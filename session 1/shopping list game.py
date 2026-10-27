#shopping list game

#array with all the items and respective prices
items_n_prices = [["water",1.00],["apple juice",3.99],["umbrella",2.59],["paracetamol",7.99],["bread",5.99],["strawberry jam",5.79]]

#extra variables
sum = 0
count = 0
pricey_meter = 0

print("Hi! Welcome to the store. Here are our items: ")

#for loop in order to list each item and price
for i in items_n_prices:
    print(i[0],"at",i[1])  #printing each item and their price next to eachother on each line
    sum = sum + i[1]        #used to add the price total for each item
    if i[1] > pricey_meter:
        pricey_meter = i[1]
        count = count + 1   # if statement to checks each item's value and stores it in "pricey_meter" when its more than the previous
    else:
        pricey_meter = pricey_meter
    priciest = items_n_prices[count]   # << count is used to track where most expensive item is positioned in the list/array

#printing total cost
print("your total is:",round(sum,2))    

#printing the most expensive item
print("the most expensive item is:",priciest[0],"at",priciest[1],".")
