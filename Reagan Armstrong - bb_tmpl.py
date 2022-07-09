rec_sub_count = 0  # Count the number of recursive calls


# data is a list of tuples (xi, ri)
# mem is a list of length len(data)+1 where mem[j]=opt(j)
def bb_rec(data, mem):
    global rec_sub_count
    rec_sub_count += 1
    if len(data) == 0:
        return 0
    else:
        last_index = (len(data)-1)
        # opt(j-1)
        s1 = 0
        # opt(j-m(j))
        s2 = 0
        if mem[len(data)] != -1:
            s1 = mem[len(data)]
        else:
            s1 = bb_rec(data[0:last_index], mem)
        list_with_j = [x for x in data if (x != data[last_index]
                                           and abs(x[0]-data[last_index][0]) > 5)]
        if mem[len(list_with_j)] != -1:
            s2 = mem[len(list_with_j)]
        else:
            s2 = bb_rec(list_with_j, mem)
        maximum = max(s1, (data[last_index][1]+s2))
        print(
            f"opt({len(data)}) = {maximum}: opt(j-1)={s1}, opt(j-m(j))={s2}, opt(j-m(j))+r={(data[last_index][1]+s2)}")
        if(mem[len(data)] == -1):
            mem[len(data)] = maximum
        # return the maximum revenue for the subproblem
        return maximum


def bb_itr(data):
    c = [0]  # list containing max revenue for each subproblem
    next_opt = []
    ##
    # Code goes here
    ##
    for i in range(len(data)):
        left = (c[i])
        valid_indexes = ([x+1 for x in range(i) if (
            abs(data[x][0]-data[i][0]) > 5)])
        sub_rev = 0
        sub_index = 0
        for x in valid_indexes:
            if c[x] > sub_rev:
                sub_rev = c[x]
                sub_index = x
        right = sub_rev+data[i][1]
        if left > right:
            c.append(left)
            next_opt.append((0, i))
        else:
            c.append(right)
            next_opt.append((1, sub_index))
    return max(c), next_opt


def check_nextOpts(data, nextOpts):
    for i in range(len(nextOpts)):
        print(f"For opt({i+1}):")
        opt = i
        total = 0
        base_hit = False
        while not base_hit:
            if nextOpts[opt][0] == 1:
                print(f"Billboard {opt+1} Placed")
                total += data[opt][1]
            if nextOpts[opt][1] == 0:
                base_hit = True
            else:
                opt = nextOpts[opt][1]-1
        print(f"opt({i+1}) max revenue={total}")


if __name__ == "__main__":
    # pairs are (xi, ri)
    # TESTS

    # data1 = [(6, 5), (7, 6), (12, 5), (14, 3)]
    # print(bb_rec(data1, [0]+[-1 for i in range(len(data1))]))
    # data2 = [(3, 5), (6, 2), (92, 34), (102, 3)]
    # print(bb_rec(data2, [0]+[-1 for i in range(len(data2))]))
    # data3 = [(45, 56), (46, 23), (55, 12), (70, 67)]
    # print(bb_rec(data3, [0]+[-1 for i in range(len(data3))]))
    # data4 = [(11, 12), (14, 9), (19, 15), (25, 4)]
    # print(bb_rec(data4, [0]+[-1 for i in range(len(data4))]))

    # DATA USED IN TABLE
    data = [(6, 5), (7, 6), (12, 5), (14, 3), (17, 8),
            (24, 2), (38, 10), (40, 1), (44, 3), (50, 7)]
    # print(f"Opt({len(data)}) = ", bb_rec(
    #     data, [0]+[-1 for i in range(len(data))]))
    maximum, nextopt = bb_itr(data)
    print(f"max (iterative solution):  {maximum}")
    print(f"data: {data}")
    print(f"nextopts: {nextopt}")
    print(f"opts full generated with tester function:")
    check_nextOpts(data, nextopt)
    # print("rec_sub_count:", rec_sub_count)
