def appearence(a, arr):
    return arr.count(a)

first_array = []
second_array = []
with open("example.in") as file:
    for line in file:
        a, b = line.strip().split("   ")
        first_array.append(int(a))
        second_array.append(int(b))

    similarity_score = dict()
    for a in first_array:
        if a in second_array and a in similarity_score:
            times = similarity_score[a]['times']
            similarity_score[a]['times'] = times + 1
        else:
            similarity_score[a] = {'score': a * appearence(a, second_array), 'times': 1}


    summup = [(value['times'] * value['score']) for (_, value) in similarity_score.items()]

    print(sum(summup))
