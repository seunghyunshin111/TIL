f = open('mulcam.txt', 'w')
for i in range(10):
    f.write(f"This is line {i}. \n")
f.close()

with open('mulcam2.txt', 'w') as f:
    for i in range(10):
        f.write(f"This is line {i}. \n")

'''
with open('mulcam.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
'''

# 개행문자 날리기
with open('mulcam.txt', 'r') as f:
    lines = f.readlines()
    print(lines.strip())
