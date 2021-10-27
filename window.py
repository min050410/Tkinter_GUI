from tkinter import *

root = Tk()  # 가장 상위레벨의 윈도 창을 생성

root.title("autoself")
root.geometry("300x200+100+100")  # 너비 높이 x y
root.resizable(False, False)  # 상하 좌우
# true 인 경우 윈도우 창의 크기 조절 가능

label = Label(root, text="hello World", width=100,
              height=50, fg="red", relief="solid",
              bitmap="info", compound="top")

label.pack()  # 레이블을 화면에 배치
root.mainloop()  # 윈도우 창을 윈도우가 종료될 때까지 실행

