import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Hospital():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

#######################################################################
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmbTabletNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssueDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvide = StringVar()
        Medication = StringVar()
        PatientID = StringVar()
        PatientNHnumber = StringVar()
        PatientName = StringVar()
        Date_of_birth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospital Management System", "Tem certeza que quer sair?")
            if exitbtn > 0:
                root.destroy()
                return

        def deletebtn():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvide.set("")
            Medication.set("")
            PatientID.set("")
            PatientNHnumber.set("")
            PatientName.set("")
            Date_of_birth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescipion.delete("1.0", END)
            TextPrescipionData.delete("1.0", END)
            return


        def resetbtn():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvide.set("")
            Medication.set("")
            PatientID.set("")
            PatientNHnumber.set("")
            PatientName.set("")
            Date_of_birth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescipion.delete("1.0", END)
            return

        def Reference_numfunc():
            ranumber = random.randint(10000,999999)
            randonumber = str(ranumber)
            Ref.set(randonumber)


        def prescriptiondatafunc():
            Reference_numfunc()
            TextPrescipionData.insert(END, Date_of_Registration.get()+"\t\t"+Ref.get()+"\t"+PatientName.get()+"\t\t"+Date_of_birth.get()+"\t\t"+NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t"+Number_of_Tablets.get()+"\t\t"+IssueDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+StorageAdvide.get()+"\t"+PatientID.get()+"\n")
            return

        def prescriptionfunc():
            Reference_numfunc()
            TextPrescipion.insert(END,"ID do Paciente: \t\t"+PatientID.get()+"\n")
            TextPrescipion.insert(END,"Nome do Paciente: \t\t"+PatientName.get()+"\n")
            TextPrescipion.insert(END,"Comprimido: \t\t"+cmbTabletNames.get()+"\n")
            TextPrescipion.insert(END,"Qtd. de Comprimidos: \t\t"+Number_of_Tablets.get()+"\n")
            TextPrescipion.insert(END,"Dose Diária: \t\t"+DailyDose.get()+"\n")
            TextPrescipion.insert(END,"Data de Emissão: \t\t"+IssueDate.get()+"\n")
            TextPrescipion.insert(END,"Validade: \t\t"+ExpiryDate.get()+"\n")
            TextPrescipion.insert(END,"Armazenamento: \t\t"+StorageAdvide.get()+"\n")
            TextPrescipion.insert(END,"Mais Informações: \t\t"+MoreInformation.get()+"\n")
            return

#######################################################################

        title = Label(self.root, text = "Hospital Management System", font=("comicsans", 42, "bold"), bd=5, relief=GROOVE,bg="#2eb8b8", fg="black")
        title.pack(side=TOP, fill=X)

#######################################################################
        Manage_Frame = Frame(self.root, width=1350, height=400,bd=5, relief=RIDGE, bg="#0099cc")
        Manage_Frame.place(x=10,y=80)

        Button_Frame = Frame(self.root, width=1925,height=55, bd=4, relief=RIDGE, bg="#328695")
        Button_Frame.place(x=10,y=460)

        Data_Frame = LabelFrame(self.root, width=1700, height = 270,bd=4,relief=RIDGE,bg="#266e73")
        Data_Frame.place(x=10,y=510)

#######################################################################
        Data_FrameLeft = LabelFrame(Manage_Frame, width =1050,text = "Informações Gerais", font=("arial",20,"italic bold"), height=390,bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width =1500,text = "Prescrições", font=("arial",15,"italic bold"), height=390,bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameRight.pack(side=RIGHT)

        Data_Framedata = LabelFrame(Data_Frame,width=1050, text="Informações Prescricionais", font=("arial",12,"italic bold"),height=390,bd=4,relief=RIDGE,bg="#3eb7bb")
        Data_Framedata.pack(side=LEFT)

#######################################################################

        DateLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Data",padx=2,bg="#0099cc")
        DateLabel.grid(row=0,column=0,padx=10,pady=5,sticky= W)
        Datetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=Date_of_Registration)
        Datetxt.grid(row=0,column=1,padx=10,pady=5,sticky=E)

############################## REF ###########################
        RefLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Reference Number",padx=2,bg="#0099cc")
        RefLabel.grid(row=1,column=0,padx=10,pady=5,sticky= W)
        Reftxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,state=DISABLED ,textvariable=Ref)
        Reftxt.grid(row=1,column=1,padx=10,pady=5,sticky=E)

######################################## PATIENT ID ###########################################
        PatientIDLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="ID do Paciente",padx=2,bg="#0099cc")
        PatientIDLabel.grid(row=2,column=0,padx=10,pady=5,sticky= W)
        PatitentIDtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=PatientID)
        PatitentIDtxt.grid(row=2,column=1,padx=10,pady=5,sticky=E)


######################################### PATITENT NAME #########################
        PatientNameLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Nome do Paciente",padx=2,bg="#0099cc")
        PatientNameLabel.grid(row=3,column=0,padx=10,pady=5,sticky= W)
        PatitentNametxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=PatientName)
        PatitentNametxt.grid(row=3,column=1,padx=10,pady=5,sticky=E)


######################################### DATE OF BIRTH #########################
        Date_of_birthLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Nascimento",padx=2,bg="#0099cc")
        Date_of_birthLabel.grid(row=4,column=0,padx=10,pady=5,sticky= W)
        Date_of_birthtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=Date_of_birth)
        Date_of_birthtxt.grid(row=4,column=1,padx=10,pady=5,sticky=E)


#################################### ADDRESS #######################################
        AddressLabel = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Endereço", padx=2, bg="#0099cc")
        AddressLabel.grid(row=5, column=0, padx=10, pady=5, sticky= W)
        Addresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable= PatientAddress)
        Addresstxt.grid(row=5, column=1, padx=10, pady=5, sticky= E)


########################### NHS NUMBER ####################################
        NHSnumberLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="NHS Number",padx=2,bg="#0099cc")
        NHSnumberLabel.grid(row=6,column=0,padx=10,pady=5,sticky= W)
        NHSnumbertxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=NHSnumber)
        NHSnumbertxt.grid(row=6,column=1,padx=10,pady=5,sticky=E)

########################### TABLET NAME
        TabletLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Comprimidos",padx=2,bg="#0099cc")
        TabletLabel.grid(row=7,column=0,padx=10,pady=5,sticky= W)
        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable=cmbTabletNames, width=25,state="readonly",font=("arial",12,"bold"))
        Tabletcmb['values'] = ("", "Paracetamol","Dipirona", "Dramim", "Soro Fisiológico", "Placebo")
        Tabletcmb.current(0)
        Tabletcmb.grid(row=7,column=1,padx=10,pady=5)

########################### NUMBER OS TABLETS #############################
        Number_of_TabletsLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Qtd. de Comprimidos",padx=2,bg="#0099cc")
        Number_of_TabletsLabel.grid(row=8,column=0,padx=10,pady=5,sticky= W)
        Number_of_Tabletstxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=Number_of_Tablets)
        Number_of_Tabletstxt.grid(row=8,column=1,padx=10,pady=5,sticky=E)


############################################################################
        HospitalCodeLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Código Hospitalar",padx=2,bg="#0099cc")
        HospitalCodeLabel.grid(row=0,column=2,padx=10,pady=5,sticky= W)
        HospitalCodetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=HospitalCode)
        HospitalCodetxt.grid(row=0,column=3,padx=10,pady=5,sticky=E)

############################# STORAGE ADVIDECE ################################
        StorageAdvideLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Armazenamento",padx=2,bg="#0099cc")
        StorageAdvideLabel.grid(row=1,column=2,padx=10,pady=5,sticky= W)
        StorageAdvidecmb = ttk.Combobox(Data_FrameLeft, textvariable=StorageAdvide, width=23, state="readonly", font=("arial",12,"bold"))
        StorageAdvidecmb['values'] = ("", "Longe do Sol", "Em temperatura Ambiente", "Refrigeradores", "Tanto faz")
        StorageAdvidecmb.current(0)
        StorageAdvidecmb.grid(row=1, column=3, padx=10,pady=5, sticky=E)


################################## LOT NUMBER OF MEDICINE ###########################
        Lot_noLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Número do Lote",padx=2,bg="#0099cc")
        Lot_noLabel.grid(row=2,column=2,padx=10,pady=5,sticky= W)
        Lot_notxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=Lot)
        Lot_notxt.grid(row=2,column=3,padx=10,pady=5,sticky=E)

##################################### ISSUED DATE #####################################
        IssueDateLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Data de emissão",padx=2,bg="#0099cc")
        IssueDateLabel.grid(row=3,column=2,padx=10,pady=5,sticky= W)
        IssueDatetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=IssueDate)
        IssueDatetxt.grid(row=3,column=3,padx=10,pady=5,sticky=E)

################################### EXPIRY ###################################
        ExpiryDateLabel = Label(Data_FrameLeft, font =("arial",12,"bold"),width=20, text="Validade",padx=2,bg="#0099cc")
        ExpiryDateLabel.grid(row=4,column=2,padx=10,pady=5,sticky= W)
        ExpiryDatetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=4,column=3,padx=10,pady=5,sticky=E)

############################## DAILY DOSE ########################
        DailyDoseLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Dose Diária",padx=2,bg="#0099cc")
        DailyDoseLabel.grid(row=5,column=2,padx=10,pady=5,sticky= W)
        DailyDosetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=DailyDose)
        DailyDosetxt.grid(row=5,column=3,padx=10,pady=5,sticky=E)

#################################### SIDE EFFECTS ####################################
        SideEffectsLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Efeitos Colaterais",padx=2,bg="#0099cc")
        SideEffectsLabel.grid(row=6,column=2,padx=10,pady=5,sticky= W)
        SideEffectstxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=SideEffects)
        SideEffectstxt.grid(row=6,column=3,padx=10,pady=5,sticky=E)


################################ MORE INFORMATION #####################
        MoreInformationLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Mais Informações",padx=2,bg="#0099cc")
        MoreInformationLabel.grid(row=7,column=2,padx=10,pady=5,sticky= W)
        MoreInformationtxt= Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=MoreInformation)
        MoreInformationtxt.grid(row=7,column=3,padx=10,pady=5,sticky=E)

########################## MEDICATION (YES / NO)
        MedicationLabel = Label(Data_FrameLeft, font=("arial",12,"bold"),width=20, text="Medicações",padx=2,bg="#0099cc")
        MedicationLabel.grid(row=8,column=2,padx=10,pady=5,sticky= W)
        Medicationtxt= Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=Medication)
        Medicationtxt.grid(row=8,column=3,padx=10,pady=5,sticky=E)



##################################### TEXT FIELD FOR THE PRESCRIPTION #####################################
        TextPrescipion = Text(Data_FrameRight, font=("arial",12,"bold"), width=55, height= 17, padx=3, pady=5)
        TextPrescipion.grid(row=0,column=0)


        #################################### TEXT FOR PRESCRIPTION DATA #################
        TextPrescipionData = Text(Data_Framedata, font=("arial",12,"bold"), width=203,height=12)
        TextPrescipionData.grid(row=1, column=0)

        ############################### BUTTONS ##########################
        Prescriptionbtn = Button(Button_Frame, text="Prescrição", bg="#ffaab0", activebackground="#fcceb2", font =("arial",15, "bold"), width=22, command=prescriptionfunc)
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        Receiptbtn = Button(Button_Frame, text="Receita", bg="#ffaab0", activebackground="#fcceb2", font =("arial",15, "bold"), width=22, command=prescriptiondatafunc)
        Receiptbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Button_Frame, text="Resetar", bg="#ffaab0", activebackground="#fcceb2", font =("arial",15, "bold"), width=22, command=resetbtn)
        Resetbtn.grid(row=0, column=2, padx=15)

        Exitbtn = Button(Button_Frame, text="Exit", bg="#ffaab0", activebackground="#fcceb2", font =("arial",15, "bold"), width=22, command=exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)

        Deletebtn = Button(Button_Frame, text="Deletar", bg="#ffaab0", activebackground="#fcceb2", font =("arial",15, "bold"), width=22, command= deletebtn)
        Deletebtn.grid(row=0, column=3, padx=15)


        prescriptiondatarow = Label(Data_Framedata, bg = "white", font=("arial", 12, "bold"),
                                    text="Data\tID de Referência\tNome\t  Nascimento\tNúmero NHS\tComprimido\tQtd. de Comprimidos\tData de emissão\tValidade\tDose Diária\tArmazenamento\tID do Paciente")
        prescriptiondatarow.grid(row=0, column=0, sticky= W)

if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()

