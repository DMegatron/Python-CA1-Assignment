lst = [str(input(f"Enter line no {i + 1}: ")) for i in range (int(input("Enter number of lines: ")))]
print(f"{"\n".join(str(i).upper() for i in lst)}")