# auto_self py, go to https://github.com/min050410/auto_self
from tkinter import *
from datetime import datetime
from tkinter.messagebox import *

# 오류
# showerror("오류", "오류가 발생했습니다")

now = datetime.now()


# nowHour
if now.hour//12:
    # print(now.hour)
    ampm = "PM"
    nowhour = str(now.hour % 12)
else:
    ampm = "AM"
    nowhour = str(now.hour)

date = "오늘은", now.year, "년", now.month, "월", now.day, "일", ampm, nowhour, "시", now.minute, "분입니다."

# root desktop gui 생성
root = Tk()

# 변수 설정
sido_var = StringVar()
scname_var = StringVar()
name_var = StringVar()
birth_var = StringVar()
password_var = StringVar()

root.title("self_macro")
root.geometry("450x350+100+100")
root.resizable(1, 1)

# date 표시
label = Label(root, text=date)
label.pack()

label2 = Label(root, text="\n자가진단 데이터 입력!")
label2.pack()

label3 = Label(root, bitmap="info")
label3.pack()

# 함수들
def commit():
    for i in range(5):  # 나중에 업데이트 하면 6으로 수정
        if(entry[i].get()):
            func.append(str(entry[i].get()))  # func에 하나씩 차곡차곡 저장
        else:
            showerror("영민", show[i]+"를 적어주세요")
    
    f = open("saveself.txt", 'w') #txt파일에 접근해서 save 파일을 만든다.
    for i in range(5):
        data = func[i]+" "
        f.write(data)
    else:
        print("정보가 이미 있습니다.")
    f.close()


# 입력을 위한 변수
entry = []
labels = []
func = []
show = ["시 또는 도", "학교 이름", "이름", "주민등록번호 앞자리", "자가진단 비밀번호", "사람 명 수_ 업데이트 중.."]


# 입력
for i in range(6):
    entry.append("버튼 추가")
    labels.append("라벨 추가")

    labels[i] = Label(root, text=show[i])
    labels[i].pack()
    if(i == 5):
        break  # 사람 명수
    entry[i] = Entry(root, width=30, relief="groove", bg="#D3D3D3")
    entry[i].pack()

button1 = Button(root, width=10, text="실행",
                 overrelief="solid", bd=2, command=commit)
button1.pack()

# 여러 사람을 동시에 할 수 있는 기능 추가 soon

root.mainloop()
