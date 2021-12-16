# State:阶段，即工件有几道工序，Job:工件数，Machine['type':list],对应各阶段的并行机数量
def Generate():
    PT = [[[31, 19, 23, 13, 33]], [[41, 55, 42, 22, 5]], [[25, 3, 27, 14, 57]], [[30, 34, 6, 13, 19]]]
    return PT


Job = 5
State = 4
Machine = [1, 1, 1, 1]

PT = Generate()
