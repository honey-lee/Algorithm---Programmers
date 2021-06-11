def solution(brown, yellow):
    result = []
    hap = brown + yellow
    div = []
    for i in range(1, hap):
        if not hap % i:
            div.append(i)

    result.append(div[len(div)//2])

    if len(div) > len(div)//2 + 1:
        result.append(div[len(div)//2 + 1])
    else:
        result.append(div[len(div) // 2])

    result.sort(reverse=True)

    return result

print(solution(10, 2))

