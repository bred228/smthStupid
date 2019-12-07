from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter import messagebox
rightCin=0
def quizCin():
    def finalCin():
        global right
        finalCin = 'Ваш результат: {} из 7'.format(right)
        if rightCin > 7:
            messagebox.showinfo('Ошибка', 'Ошибка при поиске вашей совести! Не жульничайте!')
        finalLbl = Label(cin, text=finalCin,font=('Lucido Console', 13))
        finalLbl.grid(column=0,row=4)
    def t6Cin():
        global right
        rightCin+=1
        questLblCin.configure(text='7)("Один Дома"): как Кевин запомнил и узнал вора?')
        ans1RadCin.configure(text='По зубу',command=t6Cin)
        ans2RadCin.configure(text='По руке',command=f6Cin)
        ans3RadCin.configure(text='По носу',command=f6Cin)
        ans4RadCin.configure(text='По глазу',command=f6Cin)
        finalBtnCin = Button(cin, text='Готово', bg='blue', fg='white', command=finalCin)
        finalBtnCin.grid(column=0,row=3)
    def f6Cin():
        questLblCin.configure(text='7)("Один Дома"): как Кевин запомнил и узнал вора?')
        ans1RadCin.configure(text='По зубу',command=t6Cin)
        ans2RadCin.configure(text='По руке',command=f6Cin)
        ans3RadCin.configure(text='По носу',command=f6Cin),
        ans4RadCin.configure(text='По глазу',command=f6Cin)
        finalBtnCin = Button(cin, text='Готово', bg='blue', fg='white', command=finalCin)
        finalBtnCin.grid(column=0,row=3)
    def t5Cin():
        global right
        rightCin+=1
        questLblCin.configure(text='6)("Один Дома"): сколько детей в семье Кевина?')
        ans1RadCin.configure(command=f6Cin)
        ans2RadCin.configure(command=t6Cin)
        ans3RadCin.configure(command=f6Cin),
        ans4RadCin.configure(command=f6Cin)
    def f5Cin():
        questLblCin.configure(text='6)("Один Дома"): сколько детей в семье Кевина?')
        ans1RadCin.configure(command=f6Cin)
        ans2RadCin.configure(command=t6Cin)
        ans3RadCin.configure(command=f6Cin),
        ans4RadCin.configure(command=f6Cin)
    def t4Cin():
        global right
        rightCin+=1
        questLblCin.configure(text='5)("Ирония Судьбы"): сколько раз Женя приходил к Наде?')
        ans1RadCin.configure(command=f5Cin)
        ans2RadCin.configure(command=f5Cin)
        ans3RadCin.configure(command=t5Cin),
        ans4RadCin.configure(command=f5Cin)
    def f4Cin():
        questLblCin.configure(text='5)("Ирония Судьбы"): сколько раз Женя приходил к Наде?')
        ans1RadCin.configure(command=f5Cin)
        ans2RadCin.configure(command=f5Cin)
        ans3RadCin.configure(command=t5Cin),
        ans4RadCin.configure(command=f5Cin)
    def t3Cin():
        global right
        rightCin+=1
        questLblCin.configure(text='4)("Ирония Судьбы"): сколько раз Ипполит приходил к Наде?')
        ans1RadCin.configure(text='6', command=f4Cin)
        ans2RadCin.configure(text='5', command=t4Cin)
        ans3RadCin.configure(text='4', command=f4Cin),
        ans4RadCin.configure(text='3', command=f4Cin)
    def f3Cin():
        questLblCin.configure(text='4)("Ирония Судьбы"): сколько раз Ипполит приходил к Наде?')
        ans1RadCin.configure(text='6', command=f4Cin)
        ans2RadCin.configure(text='5', command=t4Cin)
        ans3RadCin.configure(text='4', command=f4Cin),
        ans4RadCin.configure(text='3', command=f4Cin)
    def t2Cin():
        global right
        rightCin+=1
        questLblCin.configure(text='3)("Ирония Судьбы"): какой салат любил Женя?')
        ans1RadCin.configure(text='Оливье', command=f3Cin)
        ans2RadCin.configure(text='Винегрет', command=f3Cin)
        ans3RadCin.configure(text='Крабовый', command=t3Cin),
        ans4RadCin.configure(text='Фруктовый', command=f3Cin)
    def f2Cin():
        questLblCin.configure(text='3)("Ирония Судьбы"): какой салат любил Женя?')
        ans1RadCin.configure(text='Оливье', command=f3Cin)
        ans2RadCin.configure(text='Винегрет', command=f3Cin)
        ans3RadCin.configure(text='Крабовый', command=t3Cin),
        ans4RadCin.configure(text='Фруктовый', command=f3Cin)
    def t1Cin():
        global right
        rightCin+=1
        questLblCin.configure(text='2)("Ирония Судьбы"): сколько этажей было в доме?')
        ans1RadCin.configure(text='5', command=f2Cin)
        ans2RadCin.configure(text='7', command=f2Cin)
        ans3RadCin.configure(text='9', command=f2Cin),
        ans4RadCin.configure(text='11', command=t2Cin)
    def f1Cin():
        questLblCin.configure(text='2)("Ирония Судьбы"): сколько этажей было в доме?')
        ans1RadCin.configure(text='5', command=f2Cin)
        ans2RadCin.configure(text='7', command=f2Cin)
        ans3RadCin.configure(text='9', command=f2Cin),
        ans4RadCin.configure(text='11', command=t2Cin)
    cin = ttk.Frame(tab_control)
    tab_control.add(cin, text='Викторина')
    questLblCin = Label(cin, text='1)("Ирония Судьбы"): где жили Надя и Женя?')
    questLblCin.grid(column=0, row=0)
    ans1RadCin = Radiobutton(cin, text='3-я ул.Строителей, дом 25, кв.12', value=11, command=t1Cin)
    ans1RadCin.grid(column=0,row=1)
    ans2RadCin = Radiobutton(cin, text='2-я ул.Строителей, дом 25, кв.12', value=12, command=f1Cin)
    ans2RadCin.grid(column=1,row=1)
    ans3RadCin = Radiobutton(cin, text='3-я ул.Строителей, дом 20, кв.12', value=13, command=f1Cin)
    ans3RadCin.grid(column=0,row=2)
    ans4RadCin = Radiobutton(cin, text='1-я ул.Строителей, дом 5, кв.12', value=14, command=(f1Cin))
    ans4RadCin.grid(column=1,row=2)

window = Tk()
window.title('Без комментариев')
window.geometry('680x380')
tab_control = ttk.Notebook(window)
mm = ttk.Frame(tab_control)
tab_control.add(mm, text='Главное меню')
tab_control.pack(expand=1, fill='both')
cinemaRad = Radiobutton(mm, text='Викторина', value=11, command=quizCin)
cinemaRad.grid(column=0,row=0)

window.mainloop()
