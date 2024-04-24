# Progrram Name 3 QR Code and Barcode genetator and decoding (Qrcode Create)
import qrcode
from PIL import image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,)
qr.add_data("")
