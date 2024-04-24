#  Progrram Name 3 QR Code and Barcode genetator and decoding (Qrcode Decodeing and Writde)
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('qrcode.png')
result = decode(img)
for i in result:
    print(i.data.decode("utf-8"))
