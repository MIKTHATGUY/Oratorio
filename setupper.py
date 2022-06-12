import openpyxl, json, os, qrcode
from PIL import Image, ImageDraw, ImageFont

W, H = (300,200)
font = ImageFont.truetype("Poppins-Regular.ttf", 30)




wb = openpyxl.load_workbook(r'Cartel1.xlsx')
sheet = wb.active
x1 = sheet['A1'].value




with open("test.json", "r") as jsonFile:
    data = json.load(jsonFile)

righe = len(sheet['A'])

for i in range(1, righe):
    f = data
    nome = sheet[f'A{str(i)}'].value
    numero = sheet[f'B{str(i)}'].value
    anno = sheet[f'C{str(i)}'].value
    squadra = sheet[f"D{str(i)}"].value

    f["nome"] = str(nome)
    f["recapito"] = str(numero)
    f["anno"] = "a"+str(anno)
    f["squadra"] = str(squadra)
    print(f"{nome}:{squadra}")
    nommm= str(nome).split("(")[0][:-1]
    try:
        os.mkdir(f"./Bambini/{nommm}")
    except:
        pass
    with open(f"./Bambini/{nommm}/{nommm}.json", "w+") as file:
        file.write(json.dumps(f, indent=4))

for item in os.listdir("./Bambini/"):
    print(item)
    l = qrcode.make(item)
    l.save(f"./Bambini/{item}/{item} QR.png")
    print(f"QR creato per {item}")

    file = f"./Bambini/{item}/{item} QR.png"
    name = item
    msg= name
    with open(f"./Bambini/{item}/{item}.json", "r") as jsonFile:
        data = json.load(jsonFile)
        msg2 = data["squadra"]

    print(msg)
    im = Image.open(file)
    W,H = im.size
    print('width: ', W)
    print('height:', H)
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(msg, font=font)
    draw.text(((W-w)/2,w/8-w/16-w/18), msg, fill="black", font=font)
    w, h = draw.textsize(msg2, font=font)
    draw.text(((W-w)/2, (H-h)-(h/4)), msg2, fill="black", font=font)
    im.save(f"./.sfranga/{item} QR2.png", "PNG")
