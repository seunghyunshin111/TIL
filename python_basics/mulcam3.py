# 1. lines 불러오기
with open('mulcam2.txt', 'r') as file:
    lines = file.readlines()

# 2. 뒤집기
lines.reverse()

# 3. line 작성하기
with open('mulcam3.txt', 'w') as file:
    file.writelines(lines)

''' #2
with open('mulcam3.txt', 'w') as file:
    for line in lines:
        f.write(line)
'''

