print("----------Welcome to Zepto Store----------")
print("Here are the available items:")

data = {
    1:['Fruits Combo',120],
    2:['Vegetables Combo',100],
    3:['Milk (1 Litre)',50],
    4:['Bread',35],
    5:['Eggs (12 pcs)',70],
    6:['Cooking Oil (1L)',130],
    7:['Atta (1kg)',55],
    8:['Rice (1kg)',60],
    9:['Sugar (1kg)',45],
    10:['Snacks Pack',99]
}

print(f"{'index':<10}{'Item':<20}{'Price (₹)'}")

for index, item in data.items():
    print(f"{index:<10}{item[0]:<20}{item[1]}")

indexs = list(map(int, input("Enter the index numbers of items you want to buy (comma-separated): ").split(",")))

print("\n-------Bill Details-------")

total = 0
print(f"{'product':<20}{'price'}")

for i in indexs:
    if i in data:
        name = data[i][0]
        price = data[i][1]
        print(f"{name:<20}{price}")
        total += price
    else:
        print("Invalid index:", i)

print(f"\nTotal Amount: ₹{total}")
