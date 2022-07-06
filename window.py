from tkinter import *
import cv2, json, datetime
import sys
import string, requests, tkinter


ALPHA = string.ascii_letters


oggi = datetime.datetime.now().strftime("%d/%m/%Y")


print(oggi)



a = datetime.datetime.strptime(oggi, "%d/%m/%Y")
b = datetime.datetime.strptime("12/07/2022", "%d/%m/%Y")


if a > b:
        print("ciao")
        sys.exit()


def refresh(val):
        l = json.loads(open(f"./bambini/{val}/{val}.json","r").read())
        nome = l["nome"]
        pagamento = l["pagato"]     
        giorni = l["giorni"]
        allergie = l["allergie"]
        recapito = l["recapito"]
        squadra = l["squadra"]
        anno = l["anno"]
        mensa = l["mensag"]
        canvas.itemconfig(lab_nome, text=nome)
        canvas.itemconfig(lab_pagamento, text=pagamento)
        canvas.itemconfig(lab_recapito, text=recapito)
        canvas.itemconfig(lab_squadra, text=squadra)
        canvas.itemconfig(lab_anno, text=anno)
        canvas.itemconfig(lab_mensa, text=mensa)

def aggiungi_pagamento(scanned):
    with open(f"./Bambini/{scanned}/{scanned}.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["pagato"] = "Si"

    with open(f"./Bambini/{scanned}/{scanned}.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)
    
    refresh(scanned)
    b2["state"] = DISABLED







def aggiungi_data(scanned):
    print(scanned)
    with open(f"./Bambini/{scanned}/{scanned}.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["giorni"].append(oggi)

    with open(f"./Bambini/{scanned}/{scanned}.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)


    refresh(scanned)
    b1["state"] = DISABLED



def aggiungi_mensa(scanned):
    with open(f"./Bambini/{scanned}/{scanned}.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["mensag"] = "Si"

    with open(f"./Bambini/{scanned}/{scanned}.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)
    
    refresh(scanned)
    b3["state"] = DISABLED


def btn_clicked():
        b0["state"] = DISABLED
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN
        while True:
            _, frame = cap.read()
            cv2.imshow('my webcam', frame)
            det=cv2.QRCodeDetector()
            val, pts, st_code=det.detectAndDecode(frame)
            if val.startswith(tuple(ALPHA)):
                print((val))
                btn_clicked.SCANNED = val
                break 
            if cv2.waitKey(1) == 27: 
                break  # esc to quit
        cv2.destroyAllWindows()
        b0["state"] = NORMAL

        l = json.loads(open(f"./bambini/{val}/{val}.json","r").read())
        nome = l["nome"]
        pagamento = l["pagato"]     
        giorni = l["giorni"]
        allergie = l["allergie"]
        recapito = l["recapito"]
        squadra = l["squadra"]
        anno = l["anno"]
        mensa = l["mensag"]
        canvas.itemconfig(lab_nome, text=nome)
        canvas.itemconfig(lab_pagamento, text=pagamento)
        canvas.itemconfig(lab_recapito, text=recapito)
        canvas.itemconfig(lab_squadra, text=squadra)
        canvas.itemconfig(lab_anno, text=anno)
        canvas.itemconfig(lab_mensa, text=mensa)
        print(oggi)
        if giorni[-1] != oggi:
            b1["state"] = NORMAL

        if pagamento != "Si":
            b2["state"] = NORMAL
        
        if  mensa != "Si":
            b3["state"] = NORMAL



        






        
def btn_clicked2():
    canvas.itemconfig(lab_nome, text="PALLE")



window = Tk()

window.geometry("1158x746")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 746,
    width = 1158,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    569.0, 400.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 459, y = 108,
    width = 287,
    height = 53)


#PRESENZA
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: aggiungi_data(btn_clicked.SCANNED),
    relief = "flat")

b1.place(
    x = 611, y = 559,
    width = 171,
    height = 58)



#PAGAMENTO
img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: aggiungi_pagamento(btn_clicked.SCANNED),
    relief = "flat")


b2.place(
    x = 429, y = 559,
    width = 171,
    height = 58)


#mensa
img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: aggiungi_mensa(btn_clicked.SCANNED),
    relief = "flat")

b3.place(
    x = 520, y = 632,
    width = 171,
    height = 58)

canvas.create_text(
    351.0, 233.5,
    text = "Nome: ",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))




#nome
lab_nome = canvas.create_text(
    722.5, 233.5,
    text = "scannerizza per  mostrare",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))


#anno
lab_anno = canvas.create_text(
    722.5, 287.5,
    text = "scannerizza per  mostare",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))


#squadra
lab_squadra = canvas.create_text(
    722.5, 341.5,
    text = "scannerizza per  mostrare",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))

#recapito
lab_recapito = canvas.create_text(
    722.5, 395.5,
    text = "scannerizza per  mostrare",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))


#pagamento
lab_pagamento = canvas.create_text(
    722.5, 449.5,
    text = "scannerizza per  mostrare",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))

#mensa
lab_mensa = canvas.create_text(
    720.5, 503.5,
    text = "scannerizza per  mostrare",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))



canvas.create_text(
    346.0, 287.5,
    text = "Anno:",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))

canvas.create_text(
    364.5, 341.5,
    text = "Squadra:",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))

canvas.create_text(
    367.0, 395.5,
    text = "Recapito:",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))

canvas.create_text(
    383.0, 449.5,
    text = "Pagamento:",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))



canvas.create_text(
    352.0, 503.5,
    text = "Mensa:",
    fill = "#000000",
    font = ("RobotoRoman-SemiBold", int(28.0)))



b1["state"] = DISABLED
b2["state"] = DISABLED
b3["state"] = DISABLED



window.resizable(False, False)
window.mainloop()
