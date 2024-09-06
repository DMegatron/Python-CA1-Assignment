lst = [int(input(f"Enter element no {i+1}: ")) for i in range(int(input("Enter number of elements: ")))]
print(f"Average = {sum(lst)/len(lst)}")