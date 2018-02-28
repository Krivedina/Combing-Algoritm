class Apex:
    def __init__(self, name):
        self.name = name
        self.color = 0
        self.neighbors = []


def get_n():
    with open("out.txt", 'w') as file:
        file.write("N")


def get_y(first, second):
    with open("out.txt", 'w') as file:
        file.write("Y\n%s\n0\n%s" % (first, second))


def main():
    with open("in.txt") as file:
        t = {}
        size = file.readline()
        for k in range(int(size)):
            line = file.readline()
            t[k] = line.split()
    apex = []
    for x in range(int(size)):
        connect_list = []
        for value in range(int(size)):
            if int(t[x][value]) != 0:
                connect_list.append(value+1)
        a = Apex(x+1)
        a.neighbors = connect_list
        apex.append(a)

    for i in apex:
        if i.color == 0:
            i.color = 1
        for n in i.neighbors:
            n = apex[n-1]
            if n.color == 0:
                if i.color == 1:
                    n.color = 2
                else:
                    n.color = 1
            elif n.color == i.color:
                    get_n()
                    exit()
            else:
                pass
    first_line = ""
    second_line = ""
    for k in apex:
        if k.color == 1:
            first_line += str(k.name) + " "

        else:
            second_line += str(k.name) + " "

    get_y(first_line, second_line)


if __name__ == '__main__':
    main()
