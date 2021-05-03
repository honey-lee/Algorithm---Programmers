def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    phone = {
        1: 'L', 4: 'L', 7: 'L',
        3: 'R', 6: 'R', 9: 'R',
        2: 'M', 5: 'M', 8: 'M', 0: 'M',
    }

    for number in numbers:
        if phone[number] == 'M':
            pointer = [3, 1] if number == 0 else [number // 3, 1]

            l = abs(pointer[0] -  left[0]) + abs(pointer[1] - left[1])
            r = abs(pointer[0] -  right[0]) + abs(pointer[1] - right[1])

            if l < r:
                left = pointer
                answer += 'L'
            elif l > r:
                right = pointer
                answer += 'R'
            elif l == r:
                if hand == 'left':
                    left = pointer
                    answer += 'L'
                else:
                    right = pointer
                    answer += 'R'
        elif phone[number] == 'L':
            answer += 'L'
            left = [number//3, 0]
        elif phone[number] == 'R':
            answer += 'R'
            right = [(number - 1)//3, 2]

    return answer




