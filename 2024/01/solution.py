
first_array = []
second_array = []
with open("example.in") as file:
    for line in file:
        a, b = line.strip().split("   ")
        first_array.append(int(a))
        second_array.append(int(b))

    first_array.sort()
    second_array.sort()
    diff = [abs(a - b) for a,b in zip(first_array, second_array)]

    print(sum(diff))
