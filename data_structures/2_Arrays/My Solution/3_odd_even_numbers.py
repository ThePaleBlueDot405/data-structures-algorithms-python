max = int(input("Enter a max number: "))

odd_numbers = []

for i in range(1, max + 1):
    if i % 2 != 0:
        odd_numbers.append(i)

print(odd_numbers)
