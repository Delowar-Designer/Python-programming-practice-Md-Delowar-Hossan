#QR Code Genera in python
import qrcode as qr
img = qr.make("Image/Python programming practice Banner.png")
img.save("Python_qrcode.png")


#formating the qrcode
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=50,
    border=10
)
qr.add_data("https://www.youtube.com/@delowar.designer")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="White")
img.save("QR Youtube Chanale.Png")


"""import qrcode

# Formatting the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data("https://www.youtube.com/@delowar.designer")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="blue")
img.save("Qr.png")
"""