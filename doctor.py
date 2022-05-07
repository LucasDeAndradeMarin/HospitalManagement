import time
import random
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Doctor():
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        DrID = StringVar()
        DrName = StringVar()
        Date_of_birth = StringVar()
        Spes = StringVar()
        GovtPri = StringVar()
        Surgeries = StringVar()
        Experiences = StringVar()
        Nurses = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        Apptime = StringVar()
        PtAge = StringVar()
        PatienteAddress = StringVar()
        PtMobile = StringVar()
        Disease = StringVar()
        Case = StringVar()
        BenefitCard = StringVar()

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Doctor Management System", "Tem certeza que deseja sair?")
            if exitbtn >0:
                root.destroy()
            return

        def resetfunc():
            DrID.set("")
            DrName.set("")
            Date_of_birth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatienteAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            return

        def deletefunc():

            DrID.set("")
            DrName.set("")
            Date_of_birth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatienteAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPresciption.delete("1.0", END)
            TextPresciptionData.delete("1.0",END)
            return

        def Patient_Id():
            ranumber = random.randint(10000,999999)
            randonumber = str(ranumber)
            DrID.set(randonumber)
            return

        def prescriptiondatafunc():
            Patient_Id()
            TextPresciptionData.insert(END,Date_of_Registration.get()+"\t"+DrID.get()+"\t"+DrName.get()+"\t\t"+Date_of_birth.get()+"\t\t"+Spes.get()+"\t\t"
                                       +GovtPri.get()+"\t\t"+Surgeries.get()+"\t\t"+Experiences.get()+"\t\t"+Nurses.get()+"\t"+DrMobile.get()+"\t\t"+
                                       PtName.get()+"\t\t"+Case.get()+"\t\t"+PtAge.get()+"\n")
            return

        def prescriptionfunc():
            Patient_Id()
            TextPresciption.insert(END, "Data: \t\t"+Date_of_Registration.get()+"\n")
            TextPresciption.insert(END, "Nome do Paciente: \t\t"+ PtName.get()+"\n")
            TextPresciption.insert(END, "Horário da Consulta: \t\t"+Apptime.get()+"\n")
            TextPresciption.insert(END,"Idade: \t\t"+PtAge.get()+"\n")
            TextPresciption.insert(END,"Endereço: \t\t"+PatienteAddress.get()+"\n")
            TextPresciption.insert(END,"Doença: \t\t"+ Disease.get()+"\n")
            TextPresciption.insert(END,"Caso: \t\t"+Case.get()+"\n")
            TextPresciption.insert(END,"Cartão de Benfeitor: \t\t"+BenefitCard.get()+"\n")
            TextPresciption.insert(END,"Encontrar Doutor(a): \t\t"+DrName.get()+"\n")
            TextPresciption.insert(END,"Telefone do Doutor(a): \t\t"+DrMobile.get()+"\n")
            return



        title = Label(self.root, text="Doctor Management System", font=("comicsans",42,"bold"), bd=5,relief=GROOVE, bg="#b7d8d6",fg="black")
        title.pack(side=TOP,fill=X)

        Manage_Frame = Frame(self.root, width=1510, height=400, bd=5,relief=RIDGE, bg="#789e9e")
        Manage_Frame.place(x=10,y=80)


        Buttons_Frame = Frame(self.root, width=1510, height=55, bd=4,relief=RIDGE, bg="#eef3db")
        Buttons_Frame.place(x=10,y=460)

        Data_Frame = Frame(self.root, width=1510, height=270, bd=4,relief=RIDGE, bg="#eef3db")
        Data_Frame.place(x=10,y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame,width=1050, text="Informações Gerais", font=("arial",20,"italic bold"), height=390,bd=7,pady=1, relief=RIDGE,bg="#789e9e")
        Data_FrameLeft.pack(side=LEFT)

        Data_Framedata = LabelFrame(Data_Frame,width=1050, text="Informações do Médico", font=("arial",12,"italic bold"), height=390,bd=7, relief=RIDGE,bg="#b7d8d6")
        Data_Framedata.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame,width=1050, text="Informações do Paciente", font=("arial",12,"italic bold"), height=390,bd=7, relief=RIDGE,bg="#789e9e")
        Data_FrameRight.pack(side=RIGHT)


        DrIDLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "ID do Médico", bg="#789e9e")
        DrIDLabel.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        DrIDtxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width=27,state=DISABLED,textvariable=DrID)
        DrIDtxt.grid(row=0,column=1,padx=10,pady=5,sticky=E)


        DrNameLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Nome do Médico", bg="#789e9e")
        DrNameLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        DrNametxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width=27,textvariable=DrName)
        DrNametxt.grid(row=1,column=1,padx=10,pady=5,sticky=E)


        Date_of_birthLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Nascimento", bg="#789e9e")
        Date_of_birthLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        Date_of_birthtxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width=27,textvariable=Date_of_birth)
        Date_of_birthtxt.grid(row=2,column=1,padx=10,pady=5,sticky=E)


        SpesLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Especialização", bg="#789e9e")
        SpesLabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        Spestxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width=27,textvariable=Spes)
        Spestxt.grid(row=3,column=1,padx=10,pady=5,sticky=E)


        GovtPriLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Público/Privado", bg="#789e9e")
        GovtPriLabel.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        GovtPricmb = ttk.Combobox(Data_FrameLeft, textvariable = GovtPri, width=25, state="readonly",font=("arial",12,"bold"))
        GovtPricmb['values']=("","Público", "Privado")
        GovtPricmb.current(0)
        GovtPricmb.grid(row=4,column=1,padx=10,pady=5,sticky=E)

        SurgeriesLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Cirurgias", bg="#789e9e")
        SurgeriesLabel.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        Surgeriestxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width=27,textvariable=Surgeries)
        Surgeriestxt.grid(row=5,column=1,padx=10,pady=5,sticky=E)

        ExperiencesLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Experiência", bg="#789e9e")
        ExperiencesLabel.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        Experiencestxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width=27,textvariable=Experiences)
        Experiencestxt.grid(row=6,column=1,padx=10,pady=5,sticky=E)


        NursesLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Enfermeiras(os)", bg="#789e9e")
        NursesLabel.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        Nursestxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width=27,textvariable=Nurses)
        Nursestxt.grid(row=7,column=1,padx=10,pady=5,sticky=E)


        DrMobileLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Telefone do Médico", bg="#789e9e")
        DrMobileLabel.grid(row=8,column=0,padx=10,pady=5,sticky=W)
        DrMobiletxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width=27,textvariable=DrMobile)
        DrMobiletxt.grid(row=8,column=1,padx=10,pady=5,sticky=E)



        DateLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Data", padx=2,bg="#789e9e")
        DateLabel.grid(row=0, column = 2, padx=10, pady=5,sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width = 27, textvariable = Date_of_Registration)
        Datetxt.grid(row=0,column=3, padx=10,pady=5, sticky=E)

        PtNameLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Nome do Paciente", padx=2,bg="#789e9e")
        PtNameLabel.grid(row=1, column = 2, padx=10, pady=5,sticky=W)
        PtNametxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width = 27, textvariable = PtName)
        PtNametxt.grid(row=1,column=3, padx=10,pady=5, sticky=E)

        ApptimeLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Horário da Consulta", padx=2,bg="#789e9e")
        ApptimeLabel.grid(row=2, column = 2, padx=10, pady=5,sticky=W)
        Apptimetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width = 27, textvariable = Apptime)
        Apptimetxt.grid(row=2,column=3, padx=10,pady=5, sticky=E)

        PtAgeLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Idade do Paciente", padx=2,bg="#789e9e")
        PtAgeLabel.grid(row=3, column = 2, padx=10, pady=5,sticky=W)
        PtAgetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width = 27, textvariable = PtAge)
        PtAgetxt.grid(row=3,column=3, padx=10,pady=5, sticky=E)


        PatienteAddresslabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Endereço do Paciente", padx=2,bg="#789e9e")
        PatienteAddresslabel.grid(row=4, column = 2, padx=10, pady=5,sticky=W)
        PatienteAddresstxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width = 27, textvariable = PatienteAddress)
        PatienteAddresstxt.grid(row=4,column=3, padx=10,pady=5, sticky=E)


        PtMobileLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Celular do Paciente", padx=2,bg="#789e9e")
        PtMobileLabel.grid(row=5, column = 2, padx=10, pady=5,sticky=W)
        PtMobiletxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width = 27, textvariable = PtMobile)
        PtMobiletxt.grid(row=5,column=3, padx=10,pady=5, sticky=E)

        DiseaseLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Doença do Paciente", padx=2,bg="#789e9e")
        DiseaseLabel.grid(row=6, column = 2, padx=10, pady=5,sticky=W)
        Diseasetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width = 27, textvariable = Disease)
        Diseasetxt.grid(row=6,column=3, padx=10,pady=5, sticky=E)


        CaseLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Caso", bg="#789e9e")
        CaseLabel.grid(row=7,column=2,padx=10,pady=5,sticky=W)
        Casecmb = ttk.Combobox(Data_FrameLeft, textvariable = Case, width=25, state="readonly",font=("arial",12,"bold"))
        Casecmb['values']=("","Caso Novo", "Caso Antigo", "Caso Recorrente")
        Casecmb.current(0)
        Casecmb.grid(row=7,column=3,padx=10,pady=5,sticky=E)



        BenefitCardLabel = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20,text= "Benefit Card", bg="#789e9e")
        BenefitCardLabel.grid(row=8,column=2,padx=10,pady=5,sticky=W)
        BenefitCardcmb = ttk.Combobox(Data_FrameLeft, textvariable = BenefitCard, width=25, state="readonly",font=("arial",12,"bold"))
        BenefitCardcmb['values']=("","SUS", "Seguro de Vida", "Privado")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row=8,column=3,padx=10,pady=5,sticky=E)

################################################## TEXT PRESCRIPTION ###########################################

        TextPresciption = Text(Data_FrameRight, font=("arial",12,"bold"),width=55,height=17,padx=3,pady=5)
        TextPresciption.grid(row=0,column=0)
        TextPresciptionData = Text(Data_Framedata,font=("arial",12,"bold"),width=203,height=12)
        TextPresciptionData.grid(row=1,column=0)

        Prescbtn = Button(Buttons_Frame, text="Info do Paciente", bg="#fe615a", activebackground="#cc6686",font=("arial",15,"bold"), width=22, command=prescriptionfunc)
        Prescbtn.grid(row=0,column=0,padx=15)

        DoctorDetailbtn = Button(Buttons_Frame, text="Info. do Médico", bg="#fe615a", activebackground="#cc6686",font=("arial",15,"bold"), width=22, command=prescriptiondatafunc)
        DoctorDetailbtn.grid(row=0,column=1,padx=15)

        Resetbtn = Button(Buttons_Frame, text="Resetar", bg="#fe615a", activebackground="#cc6686",font=("arial",15,"bold"), width=22, command=resetfunc)
        Resetbtn.grid(row=0,column=2,padx=15)

        Deletebtn = Button(Buttons_Frame, text="Deletar", bg="#fe615a", activebackground="#cc6686",font=("arial",15,"bold"), width=22, command=deletefunc)
        Deletebtn.grid(row=0,column=3,padx=15)

        Exitbtn = Button(Buttons_Frame, text="Exit", bg="#fe615a", activebackground="#cc6686",font=("arial",15,"bold"), width=22, command=exitbtn)
        Exitbtn.grid(row=0,column=4,padx=15)

        Prescriptiondatarow = Label(Data_Framedata, bg="white",font=("arial",12,"bold"),text="Data\tID do Dr.\tNome do Dr.\tNascimento\tEspecialização\tPúblico/Privado\tCirurgias\tExperiência\tEnfermeiras(os)\tTelefone do Dr.\tNome do Paciente\tCaso\tIdade do Paciente")
        Prescriptiondatarow.grid(row=0,column=0,sticky=W)


if __name__ == "__main__":
    root = Tk()
    app = Doctor(root)
    root.mainloop()