lst = [int(input(f"Enter element {i+1}: ")) for i in range(int(input("Enter number of elements: ")))]
key = int(input("Enter element to search: "))
if key in lst:
    print(f"{key} found at index {lst.index(key)}")
else:
    print(f"{key} not found")
