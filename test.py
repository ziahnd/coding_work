x = int(input("Enter a number"))
print("#" * 20)
print(f"Multiplication table for {x}")
for i in range(1, 11):
    print(f"{x} X {i} = {x * i}")
    i+=1
print("-" * 30)