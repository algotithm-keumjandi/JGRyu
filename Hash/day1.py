def solution(participant, completion):
    part = dict(map(lambda x : (x[1],x[0]), enumerate(participant)))
    part2 = dict(map(lambda x : (x[0],x[1]), enumerate(participant)))
    comp = dict(map(lambda x : (x[0],x[1]), enumerate(completion)))
    # for v in comp.values():
    #     print(part[v])
        # part[v] = 
        
    # for v in comp.values():
    #     part2.pop(part[v])
    # for i in part2.values():
    #     return i