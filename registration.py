from multiprocessing import managers
import random
from re import M, T
from this import d
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tokenize import String
from turtle import width

from numpy import reciprocal


class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

        Date_of_Reg = StringVar()
        Date_of_Reg.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        Mobile_no = StringVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()

        Membership = StringVar()
        Membership.set("0")

        ###################################################################

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno(
                "Member Registration Form", "Tem certeza que deseja sair?")
            if exitbtn > 0:
                root.destroy()
                return

        def resetbtt():
            Firstname.set("")
            Ref.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            Lastname.set("")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")

            Membership.set("0")

            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt("")

        def reeseetbtt():
            reeesetbtt = tkinter.messagebox.askokcancel(
                "Member Registration Form", "Deseja resetar e colocar novo paciente?")
            if reeesetbtt > 0:
                resetbtt()
            elif reeesetbtt <= 0:
                resetbtt()
                detail_labeltxt.delete("1.0", END)
                return

        def reference():
            number = random.randint(1,99999999999)
            random_number = str(number)
            Ref.set(random_number)


        def membership_fees():
            if(var5.get()==1):
                member_membershiptxt.configure(state = NORMAL)
                item = float(1000)
                Membership.set("R$ "+ str(item))
            elif(var5.get() == 0):
                member_membershiptxt.configure(state = DISABLED)
                Membership.set("0")

        def Receipt():
            reference()
            detail_labeltxt.insert(END, "\t" +Date_of_Reg.get()+ "  \t"+ Ref.get()+ "\t\t" + Firstname.get() + "  \t" + Lastname.get()+ "\t\t" + Mobile_no.get() + "  \t\t" + Address.get() + " \t" + Pincode.get() + "  \t" + member_gendercmb.get() + "\t\t"+ Membership.get() + "\n")

        ###################################################################

        title = Label(self.root, text="Member Registration Form", font=(
            "comicsans", 30, "bold"), bd=5, relief=GROOVE, bg="#FF0000", fg="#000000")
        title.pack(side=TOP, fill=X)

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#001a65")
        Manage_Frame.place(x=20, y=100, width=450, height=630)

        detail_frame = Frame(self.root, relief=RIDGE, bg="#001a66")
        detail_frame.place(x=500, y=100, width=820, height=630)

        detail_label = Label(detail_frame, font=("arial", 11, "bold"), pady=10, padx=2, width=95,
                             text="Data \t Ref ID \t Nome    Sobrenome     Número Celular    Endereço      Pincode   Gênero    Membership")

        detail_label.grid(row=0, column=0, columnspan=4, sticky="w")
        detail_labeltxt = Text(detail_frame, width=123,
                               height=34, font=("arial", 10))
        detail_labeltxt.grid(row=1, column=0, columnspan=4)

        ###################################################################

        receiptbtn = Button(detail_frame, padx=15, bd=5, font=(
            "arial", 12, "bold"), bg="#ff9966", width=20, text="Receipt", command=Receipt)
        receiptbtn.grid(row=2, column=0)

        resetbtn = Button(detail_frame, padx=15, bd=5, font=(
            "arial", 12, "bold"), bg="#ff9966", width=20, text="Reset", command=reeseetbtt)
        resetbtn.grid(row=2, column=1)

        exitbtn = Button(detail_frame, padx=15, bd=5, font=(
            "arial", 12, "bold"), bg="#ff9966", width=20, text="Exit", command=exitbtn)
        exitbtn.grid(row=2, column=2)

        ###################################################################

        Cus_title = Label(Manage_Frame, text="Detalhes do Paciente", font=(
            "arial", 20, "bold"), bg="#001a66", fg="white")
        Cus_title.grid(row=0, columnspan=2, pady=5)

        ###################################################################

        member_dateLabel = Label(Manage_Frame, text="Data", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_dateLabel.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        member_dateText = Entry(Manage_Frame, font=(
            "arial", 15, "bold"), textvariable=Date_of_Reg)
        member_dateText.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        member_refLabel = Label(Manage_Frame, text="ID de Referência", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_refLabel.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        member_refText = Entry(Manage_Frame, font=(
            "arial", 15, "bold"), state=DISABLED, text="Ref")
        member_refText.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        member_fnameLabel = Label(Manage_Frame, text="Nome", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_fnameLabel.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        member_fnameText = Entry(Manage_Frame, font=(
            "arial", 15, "bold"), textvariable=Firstname)
        member_fnameText.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        member_lnameLabel = Label(Manage_Frame, text="Sobrenome", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_lnameLabel.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        member_lnameText = Entry(Manage_Frame, font=(
            "arial", 15, "bold"), textvariable=Lastname)
        member_lnameText.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        member_mobileLabel = Label(Manage_Frame, text="Número do Celular", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_mobileLabel.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        member_mobileText = Entry(Manage_Frame, font=(
            "arial", 15, "bold"), textvariable=Mobile_no)
        member_mobileText.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        member_addressLabel = Label(Manage_Frame, text="Endereço", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_addressLabel.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        member_addressText = Entry(Manage_Frame, font=(
            "arial", 15, "bold"), textvariable=Address)
        member_addressText.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        member_pincodeLabel = Label(Manage_Frame, text="Pin Code", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_pincodeLabel.grid(row=7, column=0, pady=5, padx=10, sticky="w")

        member_pincodeText = Entry(Manage_Frame, font=(
            "arial", 15, "bold"), textvariable=Pincode)
        member_pincodeText.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        member_genderLabel = Label(Manage_Frame, text="Gênero", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_genderLabel.grid(row=8, column=0, pady=5, padx=10, sticky="w")

        member_gendercmb = ttk.Combobox(
            Manage_Frame, text=var4, state="readonly", font=("arial", 15, "bold"), width=19)
        member_gendercmb['values'] = (
            "", "Masculino", "Feminino", "Prefiro não dizer", "Outro")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        member_id_proofLabel = Label(Manage_Frame, text="ID Proof", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_id_proofLabel.grid(row=9, column=0, pady=5, padx=10, sticky="w")

        member_id_proofcmb = ttk.Combobox(
            Manage_Frame, text=var3, state="readonly", font=("arial", 15, "bold"), width=19)
        member_id_proofcmb['values'] = (
            "", "CPF", "RG", "Passaporte", "Carteira de Estudante")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        member_memtypeLabel = Label(Manage_Frame, text="Tipo de paciente", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_memtypeLabel.grid(row=10, column=0, pady=5, padx=10, sticky="w")

        member_memtypecmb = ttk.Combobox(
            Manage_Frame, text=var2, state="readonly", font=("arial", 15, "bold"), width=19)
        member_memtypecmb['values'] = (
            "", "Plano de Saúde", "Privado", "SUS", "Outro")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        member_genderLabel = Label(Manage_Frame, text="Pagamento", font=(
            "arial", 15, "bold"), bg="#001a66", fg="white")
        member_genderLabel.grid(row=11, column=0, pady=5, padx=10, sticky="w")

        member_paymentwithcmb = ttk.Combobox(
            Manage_Frame, text=var1, state="readonly", font=("arial", 15, "bold"), width=19)
        member_paymentwithcmb['values'] = (
            "", "Cartão de crédito", "Cartão de Débito", "Dinheiro", "Plano de saúde", "SUS", "Outro")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(
            row=11, column=1, pady=5, padx=10, sticky="w")

        member_membership = Checkbutton(Manage_Frame, text="Membership Fees",
                                        variable=var5, onvalue=1, offvalue=0, font=("arial", 15, "bold"), bg="#001a66",
                                        fg="white", command=membership_fees)
        member_membership.grid(row=12, column=0, sticky="w")
        member_membershiptxt = Entry(Manage_Frame, font=(
            "arial", 15, "bold"), state=DISABLED, justify=RIGHT, textvariable=Membership)
        member_membershiptxt.grid(
            row=12, column=1, pady=5, padx=10, sticky="w")


