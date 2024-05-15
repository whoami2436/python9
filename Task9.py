with open ("input.txt", encoding="utf-8", mode="r") as file:
    first = file.readline().upper()
    print("Boyuk herfle: ", first)
    


with open("output.txt", encoding="utf-8", mode="w") as file:
    file.write(first)