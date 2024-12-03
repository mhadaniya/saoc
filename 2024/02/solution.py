
first_array = []
second_array = []
safe_reports = 0

with open("sample.in") as file:
    for line in file:
        levels = line.strip().split(" ")
        increasing = True if int(levels[0]) < int(levels[1]) else False
        increased = False
        for i in range(0, len(levels) - 1):
            level_a = int(levels[i])
            level_b = int(levels[i + 1])
            if level_a < level_b:
                increased = True
            else:
                increased = False

            print(f"{increasing}, {increased}")
            if increasing != increased:
                print(line)
                print('UNSAFE: rule #1')
                break

            diff = abs(level_a - level_b)
            # print(diff)
            if not(diff > 0 and diff < 4):
                print(line)
                print(f"({level_a} - {level_b}) = {diff}")
                print('UNSAFE: rule #2')
                break

            if i == len(levels) - 2:
                safe_reports += 1
                print(line)
                print("SAFE")

            # print(f"(a,b): {level_a}, {level_b}")

        print('===================')
    print(f"safe = {safe_reports}")


    # print(sum(diff))
