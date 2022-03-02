def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_dic = {}
    paused = []

    for id in id_list:
        report_dic[id] = []

    for i in range(len(report)):
        report[i] = list(reversed(report[i].split(" ")))

    for r in report:
        if r[1] not in report_dic[r[0]]:
            report_dic[r[0]].append(r[1])
            if len(report_dic[r[0]]) >= k:
                paused.append(r[0])

    for r in report_dic:
        if r in paused:
            for rr in report_dic[r]:
                answer[id_list.index(rr)] += 1

    return answer