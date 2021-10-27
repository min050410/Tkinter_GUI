# tkinter import
from tkinter import *

root = Tk()
def calc(event):
    label.config(text="계산결과:" + str(eval(entry.get())))

root.title("Calculations")
root.geometry("300x200+100+100")
root.resizable(False, False)

#레이블 생성
label = Label(root, text="0")
label.pack()

#entry 생성 - input
entry = Entry(root, width=10)
entry.bind("<Return>", calc)
entry.pack()


#메인 화면 표시
root.mainloop()

