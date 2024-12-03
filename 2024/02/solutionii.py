
first_array = []
second_array = []
safe_reports = 0

def is_safe(arr) -> bool:
    increasing = True if int(arr[0]) < int(arr[1]) else False
    increased = False
    for i in range(0, len(arr) - 1):
        level_a = int(arr[i])
        level_b = int(arr[i + 1])
        if level_a < level_b:
            increased = True
        else:
            increased = False

        # print(f"{increasing}, {increased}")
        if increasing != increased:
            print(line)
            print('UNSAFE: rule #1')
            return False

        diff = abs(level_a - level_b)
        # print(diff)
        if not(diff > 0 and diff < 4):
            print(line)
            print(f"({level_a} - {level_b}) = {diff}")
            print('UNSAFE: rule #2')
            return False

    return True


with open("sample.in") as file:
    for line in file:
        levels = line.strip().split(" ")

        if is_safe(levels):
            safe_reports += 1
        else:
            unsafe_flag = 0
            for i in range(len(levels)):
                copy_levels = levels.copy()
                copy_levels.pop(i)
                print(copy_levels)
                if is_safe(copy_levels):
                    safe_reports += 1
                    break

                # safe_reports += 1

    print(f"safe = {safe_reports}")
