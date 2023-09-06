import json
import os
import sys


path2 = os.path.join(sys.path[0], "id test")
path = os.path.join(sys.path[0], "data test")
name = input("name: ")
id = input("id: ")
num_set = set()
data = {"id":id,"name":name}


with open(path2, "a") as fp:
    with open(path2, "r") as f:
        existing_numbers = f.read().splitlines()
        num_set.update(existing_numbers)
    if id in num_set:
        print("your id alredy exists.")
    else:
        fp.write(id + "\n")
        num_set.add(id)
        with open(path, "a") as fp1:
           json.dump(data, fp1)
           fp1.write("\n")

see = input("Do you want to see someone? [y/n]: ")

if see == "y":
    id1 = input("What is the ID?: ")
    with open(path, "r") as file:
        for line in file:
            item = json.loads(line)
            if item["id"] == id1:
                print(item)
                break
        else:
            print("Person not found")
else:
    print("Goodbye")