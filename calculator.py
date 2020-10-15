try:
    from Tkinter import *
except :
    from tkinter import * 




class Calculator:
    def __init__(self,window):
        self.window = window
        window.title('Python gui calculator')
        # b1 = self.CreateButton('test')
        # b2 = self.CreateButton('test2')
        for i in range(10):
            bi=self.CreateButton(i)
            bi.pack()



    
    def CreateButton(self,text,w=5,h=5):
        # lambda is used because function is called on object creation
        btn = Button(self.window,text=text,width=w,height=h,command = lambda : self.OnClick(text))
        return(btn)

    def OnClick(self,name):
        print('btn pressed',name)


        






#create new window
window = Tk()
my_app = Calculator(window)
window.mainloop()