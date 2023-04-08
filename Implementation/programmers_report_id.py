def solution(id_list, report, k):
    report = set(list(report))
    a=[]
    b=[]
    c=[]
    reported = [x.split()[1] for x in report]

    for id in id_list:
        if reported.count(id) >= k:
            a.append(id)
            print("k번 이상 리폿당한 id: "+id)

    rar = [x.split() for x in report]
    # rar[] = [['apeach', 'muzi'], ['muzi', 'neo'], ['apeach', 'frodo'], ['muzi', 'frodo'], ['frodo', 'neo'], ['zyordi', 'frodo']]

    for i in range(len(rar)):
        # 만약 리폿당한 사람이 a에 있으면
        if rar[i][1] in a:
            # 리폿한 사람을 b에 넣음
            b.append(rar[i][0])

    for id in id_list:
        #리폿한 사람들에게 몇 번 메일이 갔는지 c에 넣음.
        c.append(b.count(id))

    print(c)

solution(["muzi", "frodo", "apeach", "neo", "zyordi"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi","zyordi frodo"], 2)