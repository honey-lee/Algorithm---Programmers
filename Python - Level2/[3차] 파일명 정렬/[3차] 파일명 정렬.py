import re

def solution(files):
    #숫자 기준 split
    tmp = [re.split(r"([0-9]+)", s) for s in files]

    sorted_files = sorted(tmp, key = lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in sorted_files]


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

print(solution(files))