import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import registration
from registration import Registration
import doctor
from doctor import Doctor
import hospital
from hospital import Hospital


def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()


class windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmay Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text="    Pharmacy Management System  ", font=("arial", 40, "bold"),
                                bd=10, relief="sunken")
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Loginframe1 = Frame(
            self.frame, width=1000, height=300, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(
            self.frame, width=1000, height=100, bd=10, relief="groove")
        self.Loginframe2.grid(row=2, column=0, pady=15)

        self.Loginframe3 = Frame(
            self.frame, width=1000, height=200, bd=10, relief="groove")
        self.Loginframe3.grid(row=6, column=0, pady=5)

        self.button_reg = Button(self.Loginframe3, text="Patitent Registration Window", state=DISABLED, font=(
            "arial", 15, "bold"), command=self.Registration_window)
        self.button_reg.grid(row=0, column=0, padx=10, pady=10)

        self.button_hosp = Button(self.Loginframe3, text="Hospital Management Window", state=DISABLED, font=(
            "arial", 15, "bold"), command=self.Hospital_window)
        self.button_hosp.grid(row=0, column=1, padx=10, pady=10)

        self.button_Doctor_appoint = Button(self.Loginframe3, text="Doctor Management Window", state=DISABLED, font=(
            "arial", 15, "bold"), command=self.Doc_Appoint_window)
        self.button_Doctor_appoint.grid(row=1, column=0, padx=10, pady=10)

        self.button_med_stock = Button(self.Loginframe3, text="Medicine Stock Window", state=DISABLED, font=(
            "arial", 15, "bold"), command=self.Medicine_stock)
        self.button_med_stock.grid(row=1, column=1, padx=10, pady=10)

        self.LabelUsername = Label(
            self.Loginframe1, text="Nome do Usuário", font=("arial", 20, "bold"), bd=3)
        self.LabelUsername.grid(row=0, column=0)

        self.textUsername = Entry(self.Loginframe1, font=(
            "arial", 20, "bold"), bd=3, textvariable=self.Username)
        self.textUsername.grid(row=0, column=1, padx=40, pady=15)

        self.LabelPassword = Label(
            self.Loginframe1, text="Senha", font=("arial", 20, "bold"), bd=3)
        self.LabelPassword.grid(row=1, column=0)

        self.textPassword = Entry(self.Loginframe1, font=(
            "arial", 20, "bold"), show="*", bd=3, textvariable=self.Password)
        self.textPassword.grid(row=1, column=1, padx=40, pady=15)

        self.button_login = Button(
            self.Loginframe2, text="Login", width=20, font=("arial", 18, "bold"),command= self.login_system)
        self.button_login.grid(row=0, column=0, padx=10, pady=10)

        self.button_Reset = Button(
            self.Loginframe2, text="Reset", width=20, font=("arial", 18, "bold"),command=self.reset_button)
        self.button_Reset.grid(row=0, column=3, padx=10, pady=10)

        self.button_Exit = Button(
            self.Loginframe2, text="Exit", width=20, font=("arial", 18, "bold"), command=self.Exit_button)
        self.button_Exit.grid(row=0, column=6, padx=10, pady=10)

    def login_system(self):
        user = self.Username.get()
        word = self.Password.get()

        if(user == str("admin") and (word == str("admin"))):
            self.button_reg.config(state = NORMAL)
            self.button_hosp.config(state=NORMAL)
            self.button_Doctor_appoint.config(state=NORMAL)
            self.button_med_stock.config(state=NORMAL)

        else:
            tkinter.messagebox.askyesno("Pharmacy Manager System", "Senha e/ou usuário incorreto.")
            self.button_reg.config(state = DISABLED)
            self.button_hosp.config(state=DISABLED)
            self.button_Doctor_appoint.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    def reset_button(self):
        self.button_reg.config(state = DISABLED)
        self.button_hosp.config(state=DISABLED)
        self.button_Doctor_appoint.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)

        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def Exit_button(self):
        self.Exit_button = tkinter.messagebox.askyesno("Pharmacy Management System", "Tem certeza que deseja sair?")
        if self.Exit_button > 0:
            self.master.destroy()
            return

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = registration.Registration(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = hospital.Hospital(self.newWindow)

    def Doc_Appoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = doctor.Doctor(self.newWindow)

    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)


class windows5:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == "__main__":
    main()
