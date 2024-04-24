# Progrram Name 3 QR Code and Barcode genetator and decoding (Qrcode Create)
import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,)
qr.add_data("Md Delowar Hossan, Roll: 602826, Dept: CST, Computer Institute")
qr.make(fit= True)

img = qr.make_image(fill_color = "black", back_color = "White")
img.save("qrcode.png")
