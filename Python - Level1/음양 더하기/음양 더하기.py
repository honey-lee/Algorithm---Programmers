def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            ans += absolutes[i]
        else:
            ans += (-absolutes[i])

    return ans



absolutes = [4, 7, 12]
signs = [True, False, True]