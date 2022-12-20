#usr/bin/python3
from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To do list")
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-do-list-App',
                font='ariel, 25 bold', width=10,bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                font='ariel, 18 bold', width=10,bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
                font='ariel, 18 bold', width=10,bd=5, bg='orange', fg='black')
        self.lable3.place(x=320, y=54)
        
        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        #=================add task================#

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'w') as file:
                file.write(content)
                file.sec(0)
                file.close()
            self.text.delete(1.0, END)
            
        def delete():
            delete_= self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readline()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                    f.truncate()
                self.main_text.delete(delete_)

                with open('data.txt', 'r') as file:
                    read = file.readlines()
                    for i in read:
                        ready = i.split()
                        self.main_text.insert(END, ready)
                    file.close()

                self.button = Button(self.root, text="Add", font='sarif, 20 bold italic', 
                        width=10,bd=5, bg='orange', fg='black',command=delete)
                self.button.place(x=30, y=280)

    def main():
        root = Tk()
        ui = todo(root)
        root.mainloop()

    if __name__ == "__main__":
        main()
