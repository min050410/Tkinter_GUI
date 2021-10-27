from tkinter import *
root = Tk()

count = 0

root.title("conut")
root.geometry("300x200+100+100")
root.resizable(False, False)


def countplus():
    global count
    count += 1
    label.config(text=str(count))

def countminus():
    global count
    if count!=0:
        count -= 1
    label.config(text=str(count))


#레이블 생성
label = Label(root, text="0")
label.pack()

#버튼 생성 
button1 = Button(root, width= 10, text="plus", overrelief="solid", command=countplus)
button1.pack() #pack을 항상 해줘야함


button2 = Button(root, width=10, text="minus", overrelief="solid", command=countminus)
button2.pack()






root.mainloop()