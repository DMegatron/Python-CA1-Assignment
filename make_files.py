import os

folder_path = "C:\\Users\\souja\\OneDrive\\Desktop\\Python CA1 Assignment"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for i in range(1, 35):
    file_name = f"{i}.py"
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, 'w') as file:
        file.write("")

print("Files created successfully!")
