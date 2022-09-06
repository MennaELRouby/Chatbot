from tkinter import *
import tkinter

def ButtonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def ButtonClear():
    global operator
    operator=""
    input_value.set("") 

def ButtonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""       

main = Tk()
main.title("calculator")
main.minsize(350,350)

ColorPalette_trquoiseOrange= "lightskyblue1	#B0E2FF", "turquoiseblue	#00C78C" , "cadmiumorange	#FF6103" , "cadmiumyellow	#4A707A"
ColorPalette_MintGreens= "lightest #D7E7D9", "a little darker #B6CEC8" , "darker #82B6AA", "darker #4A707A" , "darkest #1E443D"


operator=''

input_value = StringVar()
display_nums = Entry (main,font=("arial",25,"bold"),fg="#4A707A", textvariable=input_value ,bd=1,insertwidth=9,bg="#CFF0FF", justify=RIGHT, width=24)

button_border = tkinter.Frame(main, highlightbackground = "black", highlightthickness = 2, bd=0)

display_nums.grid(columnspan=4, rowspan=1, pady=20)
#row number 1 contains (7,8,9,+)

button_7= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="7",command=lambda: ButtonClick(7))
button_7.grid(row=1,column=0, padx=10, pady=10)

button_8= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="8",command=lambda: ButtonClick(8))
button_8.grid(row=1,column=1, padx=10, pady=10)

button_9= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="9",command=lambda: ButtonClick(9))
button_9.grid(row=1,column=2, padx=10, pady=10)

button_add= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="+",command=lambda: ButtonClick("+"))
button_add.grid(row=1,column=3, padx=10, pady=10)

#row number 2 containes(4,5,6,-)

button_4= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="4",command=lambda: ButtonClick(4))
button_4.grid(row=2,column=0, padx=10, pady=10)

button_5= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="5",command=lambda: ButtonClick(5))
button_5.grid(row=2,column=1, padx=10, pady=10)

button_6= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="6",command=lambda: ButtonClick(6))
button_6.grid(row=2,column=2, padx=10, pady=10)

button_sub= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="-",command=lambda: ButtonClick("-"))
button_sub.grid(row=2,column=3, padx=10, pady=10)

#row number 3 contains (1,2,3,*)

button_1= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="1",command=lambda: ButtonClick(1))
button_1.grid(row=3,column=0, padx=10, pady=10)

button_2= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="2",command=lambda: ButtonClick(2))
button_2.grid(row=3,column=1, padx=10, pady=10)

button_3= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="3",command=lambda: ButtonClick(3))
button_3.grid(row=3,column=2, padx=10, pady=10)

button_mult= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="x",command=lambda: ButtonClick("*"))
button_mult.grid(row=3,column=3, padx=10, pady=10)

#row number 4 contains (0,C,=,/)

button_0= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="0",command=lambda: ButtonClick(0))
button_0.grid(row=4,column=0, padx=10, pady=10)

button_C= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="C", command= ButtonClear)
button_C.grid(row=4,column=1, padx=10, pady=10)

button_equal= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="=", command= ButtonEqual)
button_equal.grid(row=4,column=2, padx=10, pady=10)

button_div= Button (main,padx=25,bd=1,fg="#4A707A",font=("arial",25,"bold"),text="/",command=lambda: ButtonClick("/"))
button_div.grid(row=4,column=3, padx=10, pady=10)

main.mainloop()