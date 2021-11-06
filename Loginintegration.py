from tkinter import*
from tkinter import ttk
import tkinter as tk
import tempfile
import os
import tkinter.messagebox
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "root",
    database= "POSDatabase"
    )
mycursor = db.cursor()

        #===========================================MySQL Price=================================================
mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567891'")
VBCost = mycursor.fetchone()
for row in VBCost:
    global VBSchCost
    VBSchCost = row;

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567890'")
CarltonCost = mycursor.fetchone()
for row in CarltonCost:
    global CarltonSchCost
    CarltonSchCost = row;

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567889'")
TooheysCost = mycursor.fetchone()
for row in TooheysCost:
    global TooheysSchCost
    TooheysSchCost = row;    

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567888'")
XXXXCost = mycursor.fetchone()
for row in XXXXCost:
    global XXXXSchCost
    XXXXSchCost = row;

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567887'")
FurphyCost = mycursor.fetchone()
for row in FurphyCost:
    global FurphySchCost
    FurphySchCost = row;

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567886'")
KosciuszkoCost = mycursor.fetchone()
for row in KosciuszkoCost:
    global KosciuszkoSchCost
    KosciuszkoSchCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567885'")
BottleOfChampagneCost = mycursor.fetchone()
for row in BottleOfChampagneCost:
    global ChampagneBottleCost
    ChampagneBottleCost = row; 


mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567884'")
BottleOfRoséCost = mycursor.fetchone()
for row in BottleOfRoséCost:
    global RoséBottleCost
    RoséBottleCost = row;    

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567883'")
GlassOfChardonnayCost = mycursor.fetchone()
for row in GlassOfChardonnayCost:
    global ChardonnayGlassCost
    ChardonnayGlassCost = row;    

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567882'")
BottleOfChardonnayCost = mycursor.fetchone()
for row in BottleOfChardonnayCost:
    global ChardonnayBottleCost
    ChardonnayBottleCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567881'")
GlassOfShirazCost = mycursor.fetchone()
for row in GlassOfShirazCost:
    global ShirazGlassCost
    ShirazGlassCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567880'")
BottleOfShirazCost = mycursor.fetchone()
for row in BottleOfShirazCost:
    global ShirazBottleCost
    ShirazBottleCost = row;  

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567879'")
NipOfBundabergCost = mycursor.fetchone()
for row in NipOfBundabergCost:
    global BundabergNipCost
    BundabergNipCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567878'")
NipOfGeorgeDickelCost = mycursor.fetchone()
for row in NipOfGeorgeDickelCost:
    global GeorgeDickelNipCost
    GeorgeDickelNipCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567877'")
NipOfSmirnoffCost = mycursor.fetchone()
for row in NipOfSmirnoffCost:
    global SmirnoffNipCost
    SmirnoffNipCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567876'")
NipOfGoronsCost = mycursor.fetchone()
for row in NipOfGoronsCost:
    global GordonsNipCost
    GordonsNipCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567875'")
NipOfDonJulioBlancoCost = mycursor.fetchone()
for row in NipOfDonJulioBlancoCost:
    global DonJulioBlancoNipCost
    DonJulioBlancoNipCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567874'")
NipOfJohnnieWalkerRedNipCost = mycursor.fetchone()
for row in NipOfJohnnieWalkerRedNipCost:
    global JohnnieWalkerRedNipCost
    JohnnieWalkerRedNipCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567873'")
MargaritaCost = mycursor.fetchone()
for row in MargaritaCost:
    global MargCost
    MargCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567872'")
CosmopolitanCost = mycursor.fetchone()
for row in CosmopolitanCost:
    global CosmoCost
    CosmoCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567871'")
MojitoCost = mycursor.fetchone()
for row in MojitoCost:
    global MojitoCocCost
    MojitoCocCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567870'")
OldFashionedCost = mycursor.fetchone()
for row in OldFashionedCost:
    global OldFashionedCostCocCost
    OldFashionedCocCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567869'")
NegroniCost = mycursor.fetchone()
for row in NegroniCost:
    global NegroniCocCost
    NegroniCocCost = row; 

mycursor.execute("SELECT Product_Per_Unit_Cost FROM Products WHERE Product_ID = '1234567868'")
EspressoMartiniCost = mycursor.fetchone()
for row in EspressoMartiniCost:
    global EspressoCost
    EspressoCost = row; 


#===========================================MySQL Name=================================================
mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567891'")
VBName = mycursor.fetchone()
for row in VBName:
    global VBSchName
    VBSchName = row;

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567890'")
CarltonName = mycursor.fetchone()
for row in CarltonName:
    global CarltonSchName
    CarltonSchName = row;

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567889'")
TooheysName = mycursor.fetchone()
for row in TooheysName:
    global TooheysSchName
    TooheysSchName = row;    

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567888'")
XXXXName = mycursor.fetchone()
for row in XXXXName:
    global XXXXSchName
    XXXXSchName = row;

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567887'")
FurphyName = mycursor.fetchone()
for row in FurphyName:
    global FurphySchName
    FurphySchName = row;

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567886'")
KosciuszkoName = mycursor.fetchone()
for row in KosciuszkoName:
    global KosciuszkoSchName
    KosciuszkoSchName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567885'")
BottleOfChampagneName = mycursor.fetchone()
for row in BottleOfChampagneName:
    global ChampagneBottleName
    ChampagneBottleName = row; 


mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567884'")
BottleOfRoséName = mycursor.fetchone()
for row in BottleOfRoséName:
    global RoséBottleName
    RoséBottleName = row;    

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567883'")
GlassOfChardonnayName = mycursor.fetchone()
for row in GlassOfChardonnayName:
    global ChardonnayGlassName
    ChardonnayGlassName = row;    

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567882'")
BottleOfChardonnayName = mycursor.fetchone()
for row in BottleOfChardonnayName:
    global ChardonnayBottleName
    ChardonnayBottleName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567881'")
GlassOfShirazName = mycursor.fetchone()
for row in GlassOfShirazName:
    global ShirazGlassName
    ShirazGlassName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567880'")
BottleOfShirazName = mycursor.fetchone()
for row in BottleOfShirazName:
    global ShirazBottleName
    ShirazBottleName = row;  

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567879'")
NipOfBundabergName = mycursor.fetchone()
for row in NipOfBundabergName:
    global BundabergNipName
    BundabergNipName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567878'")
NipOfGeorgeDickelName = mycursor.fetchone()
for row in NipOfGeorgeDickelName:
    global GeorgeDickelNipName
    GeorgeDickelNipName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567877'")
NipOfSmirnoffName = mycursor.fetchone()
for row in NipOfSmirnoffName:
    global SmirnoffNipName
    SmirnoffNipName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567876'")
NipOfGoronsName = mycursor.fetchone()
for row in NipOfGoronsName:
    global GordonsNipName
    GordonsNipName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567875'")
NipOfDonJulioBlancoName = mycursor.fetchone()
for row in NipOfDonJulioBlancoName:
    global DonJulioBlancoNipName
    DonJulioBlancoNipName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567874'")
NipOfJohnnieWalkerRedNipName = mycursor.fetchone()
for row in NipOfJohnnieWalkerRedNipName:
    global JohnnieWalkerRedNipName
    JohnnieWalkerRedNipName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567873'")
MargaritaName = mycursor.fetchone()
for row in MargaritaName:
    global MargName
    MargName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567872'")
CosmopolitanName = mycursor.fetchone()
for row in CosmopolitanName:
    global CosmoName
    CosmoName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567871'")
MojitoName = mycursor.fetchone()
for row in MojitoName:
    global MojitoCocName
    MojitoCocName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567870'")
OldFashionedName = mycursor.fetchone()
for row in OldFashionedName:
    global OldFashionedCostCocName
    OldFashionedCocName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567869'")
NegroniName = mycursor.fetchone()
for row in NegroniName:
    global NegroniCocName
    NegroniCocName = row; 

mycursor.execute("SELECT Product_Name FROM Products WHERE Product_ID = '1234567868'")
EspressoMartiniName = mycursor.fetchone()
for row in EspressoMartiniName:
    global EspressoName
    EspressoName = row; 


class POS:

    def __init__(self,root):
        self.root =root
        self.root.title("POSsible")
        self.root.geometry("1150x640+0+0")
        self.root.configure(background='#f8b86f')
        self.input_value = True
        
        self.Item1= PhotoImage(file = "VB.png")
        self.Item2= PhotoImage(file = "carlton.png")
        self.Item3= PhotoImage(file = "Tooheys.png")
        self.Item4= PhotoImage(file = "4x.png") 
        self.Item5= PhotoImage(file = "furphy.png")
        self.Item6= PhotoImage(file = "kosciuszko.png")
        self.Item7= PhotoImage(file = "rose.png")
        self.Item8= PhotoImage(file = "champagne.png")
        self.Item9= PhotoImage(file = "glassOfRed.png")
        self.Item10= PhotoImage(file = "bottleOfRed.png") 
        self.Item11= PhotoImage(file = "glassOfWhite.png")
        self.Item12= PhotoImage(file = "bottleOfWhite.png")
        self.Item13= PhotoImage(file = "bundaberg.png")
        self.Item14= PhotoImage(file = "georgeDickel.png")
        self.Item15= PhotoImage(file = "smirnoff.png")
        self.Item16= PhotoImage(file = "gordons.png")
        self.Item17= PhotoImage(file = "Donjulio.png")
        self.Item18= PhotoImage(file = "JWRed.png")
        self.Item19= PhotoImage(file = "margarita.png")
        self.Item20= PhotoImage(file = "cosmopolitan.png")
        self.Item21= PhotoImage(file = "mojito.png")
        self.Item22= PhotoImage(file = "oldFashioned.png")
        self.Item23= PhotoImage(file = "negroni.png")
        self.Item24= PhotoImage(file = "espresso.png")        


        global operator
        operator=""
        cal = StringVar()
        Change_Input = StringVar()
        Cash_Input = StringVar()
        Tax_Input = StringVar()
        SubTotal_Input = StringVar()
        Total_Input = StringVar()
        Item = StringVar()
        Qty = StringVar()
        Amount = StringVar()
        choice = StringVar()


        def btnClearDisplay():
            global operator
            operator=""
            Change_Input.set("")
            Cash_Input.set("0")
            Tax_Input.set("")
            SubTotal_Input.set("")
            Total_Input.set("")
            for i in self.POS_records.get_children():
                self.POS_records.delete(i)

        def delete():
            ItemCost=0.0
            Tax = 2.5
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
            SubTotal_Input.set(str('$%.2f'%(ItemCost)))
            Tax_Input.set(str('$%.2f'%((ItemCost * Tax)/100)))
            Total_Input.set(str('$%.2f'%((ItemCost) + ((ItemCost * Tax)/100))))
            selected_item = (self.POS_records.selection()[0])
            self.POS_records.delete(selected_item)
            

        def giveChange():
            ItemCost=0.0
            Tax = 2.5            
            CashInput = float(Cash_Input.get())
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
            Change_Input.set(str('$%.2f'%(CashInput-((ItemCost) + ((ItemCost * Tax)/100)))))
            if (Cash_Input.get() == "0"):
                Change_Input.set("")
                Method_of_Pay()

        def iPrint():
            q = self.POS_records.get_selection("Item","Qty","Amount")
           
            filename = tempfile.mktemp(".txt")
            open (filename, "w"). write(q)
            os.startfile(filename, "print")
            

        def iExit():
            iExit= tkinter.messagebox.askyesno("POSsible","Do you want to quit?")
            if iExit > 0:
                root.destroy()
                return

        def Method_of_Pay():
            if (choice.get() == "Cash"):
                self.CostText.focus()
                Cash_Input.set("")
            elif (choice.get()==""):
                Cash_Input.set("0")
                Change_Input.set("")
             
        #=============================================Layout====================================================
        MainFrame =Frame(self.root,bg='#f8b86f')
        MainFrame.grid(padx=8,pady=5)

        ButtonFrame =Frame(MainFrame, bd=5, width=1150, height=160, padx=4,pady=4, bg="#f8b86f", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame =Frame(MainFrame, bd=5,padx=5, width=1150, height=400,bg='#f8b86f',  relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFTCover =LabelFrame(DataFrame, bd=5, width=800, height=300,  relief=RIDGE
                            , bg='#f8b86f', font=('arial', 12,'bold'), text="POSsible",)
        DataFrameLEFTCover.pack(side=LEFT)

        ReceiptFrame =Frame(DataFrameLEFTCover, bd=5, width=200, height=400, pady=5,padx=1, relief=RIDGE)                             
        ReceiptFrame .pack(side=RIGHT,padx=4)
        
        FoodItemFrame =LabelFrame(DataFrame, bd=5, width=450, height=300, padx=5, pady=2, relief=RIDGE
                                   ,bg='#f8b86f', font=('arial', 12,'bold'), text="Drinks",)
        FoodItemFrame.pack(side=RIGHT)

        CalFrame =Frame(ButtonFrame,bd=5,width=432, height=140, relief=RIDGE)
        CalFrame.grid(row = 0, column = 0,padx=5)
        ChangeFrame =Frame(ButtonFrame,bd=5,width=500, height=140,pady=2, relief=RIDGE)
        ChangeFrame.grid(row = 0, column = 1,padx=5)
        RemoveFrame =Frame(ButtonFrame,bd=5,width=400, height=140, pady=4, relief=RIDGE)
        RemoveFrame.grid(row = 0, column = 2,padx=5)

        #========================================BottomLeftButtons===============================================
        self.SubTotalLabel = Label(CalFrame, font=('arial',14, 'bold'),text="Sub Total", bd=5, )
        self.SubTotalLabel.grid(row=0,column=0, sticky =W, padx=5)
        self.SubTotalText = Entry(CalFrame,font=('arial', 14,'bold'), bd=2, width=19,justify = 'left',
                                 textvariable=SubTotal_Input)
        self.SubTotalText.grid(row=0,column=1)       

        self.GSTLabel = Label(CalFrame, font=('arial',14, 'bold'),text="GST", bd=5 )
        self.GSTLabel .grid(row=1,column=0 , sticky =W, padx=5)
        self.GSTText  = Entry(CalFrame,font=('arial', 14,'bold'), bd=2, width=19, textvariable=Tax_Input)
        self.GSTText .grid(row=1,column=1, sticky =W)

        self.TotalLabel = Label(CalFrame, font=('arial',14, 'bold'),text="Total", bd=5 )
        self.TotalLabel.grid(row=2,column=0 , sticky =W, padx=5)
        self.TotalText = Entry(CalFrame,font=('arial', 14,'bold'), bd=2, width=19, textvariable=Total_Input)
        self.TotalText.grid(row=2,column=1, sticky =W)

        #========================================BottomMiddleButtons=============================================
        self.PaymentLabel = Label(ChangeFrame, font=('arial',14, 'bold'),text="Transaction", bd=2, )
        self.PaymentLabel.grid(row=0,column=0, sticky =W, padx=2)
        self.PaymentList=ttk.Combobox(ChangeFrame, width=24 , font=('arial',14,'bold'),state='readonly',
                                 textvariable=choice,justify=RIGHT)
        self.PaymentList['values'] =('','Cash','EFTPOS','MOTO')
        self.PaymentList.current(0)
        self.PaymentList.grid(row=0,column=1)

        self.CostLabel = Label(ChangeFrame, font=('arial',14, 'bold'),text="Payment", bd=5, )
        self.CostLabel.grid(row=1,column=0, sticky =W, padx=2)
        self.CostText = Entry(ChangeFrame,font=('arial', 14,'bold'), bd=2, width=26,textvariable=Cash_Input,justify=RIGHT)
        self.CostText.grid(row=1,column=1)
        self.CostText.insert(0, "0")

        self.ChangeLabel = Label(ChangeFrame, font=('arial',14, 'bold'),text="Change", bd=5 )
        self.ChangeLabel.grid(row=2,column=0 , sticky =W, padx=2)
        self.ChangeText = Entry(ChangeFrame,font=('arial', 14,'bold'),bd=2, textvariable=Change_Input,width=26,justify=RIGHT)
        self.ChangeText.grid(row=2,column=1, sticky =W)

        #======================================BottomRightButtons================================================
        self.PayButton=Button(RemoveFrame, padx=2, font=('arial',15, 'bold'),text="Pay", width =10, height=1,bd=2,
                           command=giveChange)
        self.PayButton.grid(row=0,column=0,padx=4,pady=2)
        
        self.PrintButton=Button(RemoveFrame, padx=2, font=('arial',15, 'bold'),text="Exit", width =10, height=1,bd=2,
                             command = iExit)
        self.PrintButton.grid(row=1,column=1,padx=2, pady=2)
        
        self.ResetButton=Button(RemoveFrame, padx=2, font=('arial',15, 'bold'),text="Reset", width =10, height=1,bd=2,
                               command=btnClearDisplay)
        self.ResetButton.grid(row=1,column=0,padx=2, pady=2)        

        self.RemoveButton=Button(RemoveFrame, padx=2, font=('arial',15, 'bold'),text="Void", width =10,
                                  height=1,bd=2, command=delete)
        self.RemoveButton.grid(row=0,column=1,padx=2, pady=2)
        
        #===========================================ImageButtons================================================        
        def VB():   
            ItemCost = 2.3 
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(VBSchName, "1", VBSchCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.3)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.3)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.3) + ((ItemCost-2.3)* Tax)/100))) 
                

        def Carlton():  
            ItemCost = 1.9
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(CarltonSchName, "1", CarltonSchCost))            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-1.9)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-1.9)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-1.9) + ((ItemCost-1.9)* Tax)/100))) 

        def Tooheys():   
            ItemCost = 1.70
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(TooheysSchName, "1", TooheysSchCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-1.7)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-1.7)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-1.7) + ((ItemCost-1.7)* Tax)/100))) 

        def XXXX():  
            ItemCost = 0.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(XXXXSchName, "1", XXXXSchCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2]) 
                SubTotal_Input.set(str('$%.2f'%(ItemCost-0.90)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-0.90)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-0.90) + ((ItemCost-0.90)* Tax)/100))) 

        def Furphy():   
            ItemCost = 3.95
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(FurphySchName, "1", FurphySchCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-3.95)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-3.95)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-3.95) + ((ItemCost-3.95)* Tax)/100))) 

        def Kosciuszko():  
            ItemCost = 3.75
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(KosciuszkoSchName, "1", KosciuszkoSchCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-3.75)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-3.75)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-3.75) + ((ItemCost-3.75)* Tax)/100))) 

        def Rose():   
            ItemCost = 1.20
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(RoséBottleName, "1", RoséBottleCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-1.20)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-1.20)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-1.20) + ((ItemCost-1.20)* Tax)/100))) 

        def Champagne():  
            ItemCost = 1.10
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(ChampagneBottleName, "1", ChampagneBottleCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-1.10)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-1.10)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-1.10) + ((ItemCost-1.10)* Tax)/100))) 

        def WhiteGlass():   
            ItemCost = 1.20
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(ChardonnayGlassName, "1", ChardonnayGlassCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-1.20)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-1.20)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-1.20) + ((ItemCost-1.20)* Tax)/100))) 

        def WhiteBottle():  
            ItemCost = 2.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(ChardonnayBottleName, "1", ChardonnayBottleCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.90)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.90)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.90) + ((ItemCost-2.90)* Tax)/100))) 

        def RedGlass():   
            ItemCost = 3.20
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(ShirazGlassName, "1", ShirazGlassCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-3.20)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-3.20)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-3.20) + ((ItemCost-3.20)* Tax)/100))) 

        def RedBottle():  
            ItemCost = 1.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(ShirazBottleName, "1", ShirazBottleCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-1.90)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-1.90)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-1.90) + ((ItemCost-1.90)* Tax)/100))) 

        def Bundaberg():   
            ItemCost = 2.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(BundabergNipName, "1", BundabergNipCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.90)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.90)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.90) + ((ItemCost-2.90)* Tax)/100))) 

        def GeorgeDickel():  
            ItemCost = 2.20
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(GeorgeDickelNipName, "1", GeorgeDickelNipCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.20)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.20)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.20) + ((ItemCost-2.20)* Tax)/100))) 

        def Smirnoff():   
            ItemCost = 2.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(SmirnoffNipName, "1", SmirnoffNipCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.90)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.90)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.90) + ((ItemCost-2.90)* Tax)/100))) 

        def Gordons():  
            ItemCost = 2.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(GordonsNipName, "1", GordonsNipCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.90)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.90)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.90) + ((ItemCost-2.90)* Tax)/100))) 

        def DonJulioBlanco():   
            ItemCost = 3.20
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(DonJulioBlancoNipName, "1", DonJulioBlancoNipCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-3.20)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-3.20)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-3.20) + ((ItemCost-3.20)* Tax)/100))) 

        def JohnnieWalkerRed():  
            ItemCost = 1.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(JohnnieWalkerRedNipName, "1", JohnnieWalkerRedNipCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-1.90)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-1.90)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-1.90) + ((ItemCost-1.90)* Tax)/100))) 
 
        def Margarita():   
            ItemCost = 2.10
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(MargName, "1", MargCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.10)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.10)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.10) + ((ItemCost-2.10)* Tax)/100))) 

        def Cosmopolitan():  
            ItemCost = 2.75
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(CosmoName, "1", CosmoCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.75)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.75)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.75) + ((ItemCost-2.75)* Tax)/100))) 

        def Mojito():   
            ItemCost = 1.59
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(MojitoName, "1", MojitoCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-1.59)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-1.59)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-1.59) + ((ItemCost-1.59)* Tax)/100))) 

        def OldFashioned():  
            ItemCost = 2.99
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(OldFashionedCocName, "1", OldFashionedCocCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.99)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.99)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.99) + ((ItemCost-2.99)* Tax)/100))) 

        def Negroni():   
            ItemCost = 3.40
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(NegroniCocName, "1", NegroniCocCost))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-3.40)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-3.40)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-3.40) + ((ItemCost-3.40)* Tax)/100))) 

        def EspressoMartini():  
            ItemCost = 2.89
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=(EspressoName, "1", EspressoCost))
            
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(ItemCost-2.89)))
                Tax_Input.set(str('$%.2f'%(((ItemCost-2.89)* Tax)/100))) 
                Total_Input.set(str('$%.2f'%((ItemCost-2.89) + ((ItemCost-2.89)* Tax)/100))) 

        #======================================Treeview========================================================
        scroll_x=Scrollbar(ReceiptFrame ,orient=HORIZONTAL)
        scroll_y=Scrollbar(ReceiptFrame ,orient=VERTICAL)

        self.POS_records=ttk.Treeview(ReceiptFrame ,height=20,columns=("Item","Qty","Amount"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.POS_records.heading("Item",text="Item")
        self.POS_records.heading("Qty",text="Qty")
        self.POS_records.heading("Amount",text="Amount")

        self.POS_records['show']='headings'
        
        self.POS_records.column("Item", width=120)
        self.POS_records.column("Qty",width=100)
        self.POS_records.column("Amount",width=100)
      
        self.POS_records.pack(fill=BOTH,expand=1)
        self.POS_records.bind("<ButtonRelease-1>")

        #======================================ButtonLayout===================================================
        self.btnVB=Button(FoodItemFrame, padx=2,image= self.Item1, width =104, height=104,bd=2,command=VB)
        self.btnVB.grid(row=0,column=1,padx=4,pady=2)
        
        self.btnCarlton=Button(FoodItemFrame, padx=2,image= self.Item2, width =104, height=104,bd=2,command=Carlton)
        self.btnCarlton.grid(row=0,column=2,padx=2)
        
        self.btnTooheys=Button(FoodItemFrame, padx=2,image  = self.Item3, width =104, height=104,bd=2,command=Tooheys)
        self.btnTooheys.grid(row=0,column=3,padx=2)        

        self.btnXXXX=Button(FoodItemFrame, padx=2,image  = self.Item4, width =104, height=104,bd=2,command=XXXX)
        self.btnXXXX.grid(row=0,column=4,padx=2)

        self.btnFurphy=Button(FoodItemFrame, padx=2,image  = self.Item5, width =104, height=104,bd=2,command=Furphy)
        self.btnFurphy.grid(row=0,column=5,padx=2)

        self.btnKosciuszko=Button(FoodItemFrame, padx=2,image  = self.Item6, width =104, height=104,bd=2,command=Kosciuszko)
        self.btnKosciuszko.grid(row=0,column=6,padx=2)

        self.btnRose=Button(FoodItemFrame, padx=2,image  = self.Item7, width =104, height=104,bd=2,command=Rose)                                     
        self.btnRose.grid(row=1,column=1,padx=4,pady=2)

        self.btnChampagne=Button(FoodItemFrame, padx=2,image  = self.Item8, width =104, height=104,bd=2,command=Champagne)                                     
        self.btnChampagne.grid(row=1,column=2,padx=2)

        self.btnWhiteGlass=Button(FoodItemFrame, padx=2,image  = self.Item9, width =104, height=104,bd=2,command=WhiteGlass)                                     
        self.btnWhiteGlass.grid(row=1,column=3,padx=2)

        self.btnWhiteBottle=Button(FoodItemFrame, padx=2,image  = self.Item10, width =104, height=104,bd=2,command=WhiteBottle)                                     
        self.btnWhiteBottle.grid(row=1,column=4,padx=2)

        self.btnRedGlass=Button(FoodItemFrame, padx=2,image  = self.Item11, width =104, height=104,bd=2,command=RedGlass)                                     
        self.btnRedGlass.grid(row=1,column=5,padx=2)

        self.btnRedBottle=Button(FoodItemFrame, padx=2,image  = self.Item12, width =104, height=104,bd=2,command=RedBottle)                                     
        self.btnRedBottle.grid(row=1,column=6,padx=2)     
      
        self.btnBundaberg=Button(FoodItemFrame, padx=2,image  = self.Item13, width =104, height=104,bd=2,command=Bundaberg)                                     
        self.btnBundaberg.grid(row=2,column=1,padx=4,pady=2)
        
        self.btnGeorgeDickel=Button(FoodItemFrame, padx=2,image  = self.Item14, width =104, height=104,bd=2,command=GeorgeDickel)                                     
        self.btnGeorgeDickel.grid(row=2,column=2,padx=2)
        
        self.btnSmirnoff=Button(FoodItemFrame, padx=2,image  = self.Item15, width =104, height=104,bd=2,command=Smirnoff)                                     
        self.btnSmirnoff.grid(row=2,column=3,padx=2)        

        self.btnGordons=Button(FoodItemFrame, padx=2,image  = self.Item16, width =104, height=104,bd=2,command=Gordons)                                     
        self.btnGordons.grid(row=2,column=4,padx=2) 

        self.btnDonJulioBlanco=Button(FoodItemFrame, padx=2,image  = self.Item17, width =104, height=104,bd=2,command=DonJulioBlanco)                                     
        self.btnDonJulioBlanco.grid(row=2,column=5,padx=2)

        self.btnJohnnieWalkerRed=Button(FoodItemFrame, padx=2,image  = self.Item18, width =104, height=104,bd=2,command=JohnnieWalkerRed)                                     
        self.btnJohnnieWalkerRed.grid(row=2,column=6,padx=2)

        self.btnMargarita=Button(FoodItemFrame,padx=2,image = self.Item19,width =104, height=104,bd=2,command=Margarita)                                     
        self.btnMargarita.grid(row=3,column=1,padx=4,pady=4)
        
        self.btnCosmopolitan=Button(FoodItemFrame, padx=2,image  = self.Item20, width =104, height=104,bd=2,command=Cosmopolitan)                                     
        self.btnCosmopolitan.grid(row=3,column=2,padx=2)
        
        self.btnMojito=Button(FoodItemFrame, padx=2,image  = self.Item21, width =104, height=104,bd=2,command=Mojito)                                     
        self.btnMojito.grid(row=3,column=3,padx=2)
        
        self.btnOldFashioned=Button(FoodItemFrame, padx=2,image  = self.Item22, width =104,height=104,bd=2,command=OldFashioned)                                     
        self.btnOldFashioned.grid(row=3,column=4,padx=2) 

        self.btnNegroni=Button(FoodItemFrame, padx=2,image  = self.Item23, width =104, height=104,bd=2,command=Negroni)                                     
        self.btnNegroni.grid(row=3,column=5,padx=2)

        self.btnEspressoMartini=Button(FoodItemFrame, padx=2,image  = self.Item24, width =104, height=104,bd=2,command=EspressoMartini)                                     
        self.btnEspressoMartini.grid(row=3,column=6,padx=2)

        #==============================================================================================
       
if __name__=='__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()













        


        
