class Apex:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}


def get_out(dict_of_final, length):
    with open("out.txt", 'w') as file:
        for i in dict_of_final:
            for k in dict_of_final[i]:
                file.write(str(k) + " ")
            file.write("0\n")
        file.write(str(length))


def sort_by_number(a):
    return int(a[1])


def get_neighbors(string):
    dict_distance = {}
    mass = string.split()
    mass.pop()
    apex = mass[::2]
    distance = mass[1::2]
    for i in range(len(apex)):
        dict_distance[apex[i]] = distance[i]
    return dict_distance


def main():
    apex_list = []
    with open("in.txt") as f:
        apex_count = f.readline()
        for x in range(int(apex_count)):
            a = Apex(x + 1)
            a.neighbors = get_neighbors(f.readline())
            apex_list.append(a)

    dict_of_all = {}
    dict_of_all_sort = {}
    value_list_check = []
    for i in apex_list:
        for k in i.neighbors.keys():
            dict_of_all[str(i.name) + "-" + k] = i.neighbors[k]
    for key, value in sorted(dict_of_all.items(), key=sort_by_number):
        q = key.split("-")
        a = q[0]
        b = q[1]
        if str(b + "-" + a) in dict_of_all_sort:
            continue
        else:
            dict_of_all_sort[key] = value
            value_list_check.append(value)

    dict_of_sets = {}
    for i in range(int(apex_count)):
        dict_of_sets[i + 1] = [apex_list[i].name]

    dict_of_answer = {}
    full_length = 0
    for i in dict_of_all_sort:
        distance = int(dict_of_all_sort[i])
        qw = i.split("-")
        a = int(qw[0])
        b = int(qw[1])
        if dict_of_sets[a] == dict_of_sets[b]:
            continue
        else:
            for k in dict_of_sets[b]:
                dict_of_sets[a].append(k)
            dict_of_sets[b].clear()
            for k in dict_of_sets[a]:
                dict_of_sets[k] = dict_of_sets[a]
            dict_of_answer[i] = distance
            full_length += distance

    dict_of_answer_2 = {}
    list_of_keys = list(dict_of_answer.keys())
    list_of_keys.sort()
    for i in list_of_keys:
        dict_of_answer_2[i] = dict_of_answer[i]

    for i in range(int(apex_count)):
        dict_of_sets[i + 1] = []
    for i in dict_of_answer_2:
        distance = dict_of_answer_2[i]
        qwe = i.split("-")
        a = int(qwe[0])
        b = int(qwe[1])
        dict_of_sets[b].append(a)
        dict_of_sets[b].append(distance)
        dict_of_sets[a].append(b)
        dict_of_sets[a].append(distance)

    get_out(dict_of_sets, full_length)


main()
