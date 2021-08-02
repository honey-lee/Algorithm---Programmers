def is_palindrome(str):
    s_len = len(str)

    if s_len <= 1:
        return True

    for i in range(s_len // 2):
        if str[i] == str[s_len - 1]:
            s_len -= 1
        else:
            return False
    return True


def solution(s):
    for i in range(len(s), 0, -1):
        for start in range(0, len(s)):
            new_s = s[start: start + i]

            if is_palindrome(new_s):
                return len(new_s)

            if start + i >= len(s):
                break


print(solution("abacde"))

"""
1 2 3 4 5

1 2 3 4
  2 3 4 5
  
1 2 3
  2 3 4
    3 4 5
    
1 2 
  2 3
    3 4
      4 5
      
1
 2
  3 
   4
    5
"""