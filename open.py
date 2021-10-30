f = open('새파일.txt', 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
# C:\python\새파일.txt 실행한 곳에 하위에 저장되는 것을 볼수 있다.