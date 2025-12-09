id = int(input("Enter the App ID: "))
name = input("Enter Name of the App: ")
version = input("Enter the version of the App: ")
price = float(input("Enter Subscription cost (if not, enter 0): "))
discount = float(input("Enter discount percent: "))

cat = list(map(str.strip, input("Enter the App categories (comma-separated): ").split(',')))

downloads, users = map(int, input("Enter Downloads and Users (space-separated): ").split())

features = set(map(str.strip, input("Enter the features (comma-separated): ").split(',')))
developer_details = {
    'Developer_name': input("Enter developer name: "),
    'Contact': input("Enter developer contact: "),
    'Location': input("Enter developer location: ")
}

print("\n" * 2)

print("1) Using Comma Separation (sep=','):")
print("App ID:", id, "Name:", name, "Price:", price, sep=',')

print("\n2) Using Percentage Formatting (% operator):")
print("App Discount: %.2f%%" % discount)
print("App Version: %s" % version)

print("\n3) Using f-strings (f\"\"):")
print(f"App Name: {name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount}%")
print(f"Categories: {', '.join(cat)}")
print(f"Downloads: {downloads}")
print(f"Users: {users}")
print(f"Features: {', '.join(features)}")

print("\n4) Using .format() method:")
print("Developer Details: Name - {}, Contact - {}, Location - {}".format(
      developer_details['Developer_name'],
      developer_details['Contact'],
      developer_details['Location']
))

print("\nDeveloper Details (line by line):")
for key, value in developer_details.items():
    print("{}: {}".format(key, value))