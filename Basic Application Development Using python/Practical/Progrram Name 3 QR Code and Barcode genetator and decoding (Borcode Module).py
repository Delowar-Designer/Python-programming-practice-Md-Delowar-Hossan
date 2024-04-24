# Progrram Name 3 QR Code and Barcode genetator and decoding (Borcode Module)
# Barcode
# Import Ean13 from barcode module
from barcode import EAN13
# Make sure to pass the number as string
number = ('8801773873289')

# Now, lets ccreate an objecct of EAN13
# class and pass the number
my_code = EAN13(number)

# Our barcode is ready. Lets save it.
my_code.save("new_code")


'''from barcode import generate
from barcode.writer import ImageWriter

# Generate EAN-13 barcode image
barcode = generate('ean13', '5901234123457', writer=ImageWriter())
barcode.save('new_code')'''


'''from barcode import EAN13

number = '5901234123457'  # Corrected variable name

my_code = EAN13(number)
my_code.save("new_code")'''

'''from barcode import EAN13

number = '5901234123457'
my_code = EAN13(number)
my_code.save("new_code")'''
