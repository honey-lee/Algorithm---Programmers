bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

#실행시간이 엄청 길게 늘어짐..
#트럭이 다리를 실제로 지나간다고 생각하고 구현해봄
def solution(bridge_length, weight, truck_weights):
    #다리를 만들어주고
    bridge = [0] * bridge_length
    #소요시간
    time = 0

    #다리를 지나가는 트럭이 있는동안은 소요시간을 더하고
    #0번 요소를 없앤다
    while bridge:
        time += 1
        bridge.pop(0)

        #아직 다리로 가야할 트럭들이 있고
        if truck_weights:
            #지금 다리에 있는 트럭의 무게와 아직가지 못한 첫번째 트럭의 무게가
            #다리가 감당할 수 있는 무게이면
            #다리로 트럭을 보낸다
            if len(bridge) <= bridge_length and sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            #아니라면 다리의 뒤에 0을 더해서 이미 있는 트럭이 다 지나가고
            #새로운 트럭이 들어가게 한다
            else:
                bridge.append(0)

    return time

"""
bridge          truck            time
0, 0           7, 4, 5, 6          0
0, 7             4, 5, 6           1
7, 0             4, 5, 6           2
0, 4               5, 6            3
4, 5                 6             4
5, 0                 6             5
0, 6                               6
6, 0                               7
통과                                8
"""


"""
#다리에 트럭이 있는 동안은 시간을 더해줌
#트럭이 움직이니까
while bridge:
    time += 1
    bridge.pop(0)
    if truck_weights:
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
"""


print(solution(bridge_length, weight, truck_weights))


"""
    for i in truck_weight:
        if len(bridge) <= bridge_length and (sum(bridge)+i) <= weight:
            bridge.append(i)
        else:
            wait.append(i)

    while bridge:
        if len(bridge) == 1:
            time += bridge_length
            bridge.pop()
            for i in wait:
                if len(bridge) <= bridge_length and (sum(bridge) + i) <= weight:
                    bridge.append(i)
        else:

"""