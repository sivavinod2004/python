#sivapriya
#november19
#employ management system

inventory=[
    ("smart phone",20,50000),
    ("mouse",20,150),
    ("head phone",10,500),
    ("keyboard",20,150),
    ("moniter",10,1000)
]
highest_stock_value=0
item_with_highest_stock_value=0
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_price
    print("item name",item_name,",stock_value",stock_value)
    if stock_value> highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print("highest stock value is:",highest_stock_value)
print("item with heighest stock value is",item_with_highest_stock_value)
