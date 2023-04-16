from tkinter import *
from customtkinter import *

#--------Main window--------
app=CTk()
width= app.winfo_screenwidth()               
height= app.winfo_screenheight() 
# app.resizable(width=FALSE, height=FALSE)
app.geometry("%dx%d" %(width,height))
app.title("App")

#--------Functions--------
def year1():
    s_year_frame.grid_forget()
    f_year_frame.grid_propagate(0)
    f_year_frame.grid(row=0,column=1)    



def year2():
    f_year_frame.grid_forget()
    s_year_frame.grid_propagate(0)
    s_year_frame.grid(row=0,column=1)







frame1=CTkFrame(app,width=185,height=height)
frame1.grid(row=0,column=0,padx=5,pady=5)
frame1.grid_propagate(0)

year_var=IntVar()
year_var.set(1)

f_year_button=CTkRadioButton(frame1,text="1st Year",height=10,width=10,value=1,variable=year_var,command=year1)
f_year_button.grid(padx=10,pady=10)

s_year_buton=CTkRadioButton(frame1,text="2nd Year",height=10,width=10,value=2,variable=year_var,command=year2)
s_year_buton.grid(padx=10,pady=10)





#--------First Year Frame--------
f_year_frame=CTkScrollableFrame(app,width=1150,height=height-80)
f_year_frame.grid(row=0,column=1,sticky="N")
f_year_frame.grid_propagate()
# f_label=CTkLabel(f_year_frame,text='1st year')
# f_label.grid()


#--------Frame content--------
reg_no_label = CTkLabel(f_year_frame, text="Registration Number")
reg_no_label.grid(padx=500,pady=5,sticky="E")
reg_no_entry = CTkEntry(f_year_frame)
reg_no_entry.grid(padx=500,pady=5)



name_var=StringVar()

name_label = CTkLabel(f_year_frame, text="Name")
name_label.grid(padx=500,pady=10)
name_entry =CTkEntry(f_year_frame)
name_entry.grid(padx=500,pady=10)


gender_var = StringVar()
gender = CTkLabel(f_year_frame, text="Gender")
gender.grid(padx=500,pady=10)

male_radiobtn = CTkRadioButton(f_year_frame, text="Male", variable=gender_var, value="M")
male_radiobtn.grid(padx=500,pady=10)
female_radiobtn = CTkRadioButton(f_year_frame, text="Female", variable=gender_var, value="F")
female_radiobtn.grid(padx=500,pady=10)
other_radiobtn =CTkRadioButton(f_year_frame, text="Other", variable=gender_var, value="O")
other_radiobtn.grid(padx=500,pady=10)

mo_var = BooleanVar()
py_var = BooleanVar()
engg_var = BooleanVar()
program = CTkLabel(f_year_frame, text="Program")
program.grid(padx=500,pady=10)
mo_btn = CTkCheckBox(f_year_frame, text="MO", variable=mo_var)
mo_btn.grid(padx=500,pady=10)
py_btn = CTkCheckBox(f_year_frame, text="PY", variable=py_var)
py_btn.grid(padx=500,pady=10)
engg_btn = CTkCheckBox(f_year_frame, text="ENGG", variable=engg_var)
engg_btn.grid(padx=500,pady=10)


#--------GEN/CSP--------
gen_csp_var= StringVar()
gen_csp_label = CTkLabel(f_year_frame, text="GEN/CSP:")
gen_csp_label.grid(padx=500,pady=10)

gen_radiobtn = CTkRadioButton(f_year_frame, text="GEN",variable=gen_csp_var, value="GEN")
gen_radiobtn.grid(padx=500,pady=10)

csp_radiobtn = CTkRadioButton(f_year_frame,text="CSP", variable=gen_csp_var, value="CSP")
csp_radiobtn.grid(padx=500,pady=10)



#--------SC/ST/OBC--------
sc_st_obc_var= StringVar()
gen_csp_label = CTkLabel(f_year_frame, text="GEN/CSP:")
gen_csp_label.grid(padx=500,pady=10)

sc_radiobtn = CTkRadioButton(f_year_frame, text="SC",variable=sc_st_obc_var, value="SC")
sc_radiobtn.grid(padx=500,pady=10)

st_radiobtn = CTkRadioButton(f_year_frame,text="ST", variable=sc_st_obc_var, value="ST")
st_radiobtn.grid(padx=500,pady=10)

obc_radiobtn = CTkRadioButton(f_year_frame,text="OBC", variable=sc_st_obc_var, value="OBC")
obc_radiobtn.grid(padx=500,pady=10)



#--------First Year Frame Ends------











s_year_frame=CTkFrame(app,width=1165,height=height)
s_label=CTkLabel(s_year_frame,text='2nd year')
s_year_frame.grid_propagate(0)
s_label.grid()

app.mainloop()
