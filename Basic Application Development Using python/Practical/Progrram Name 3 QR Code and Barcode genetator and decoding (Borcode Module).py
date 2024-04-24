# Progrram Name 3 QR Code and Barcode genetator and decoding (Borcode Module)
# Barcode
# Import Ean13 from barcode module
from barcode import EAN13
# Make sure to pass the number as string
number = '01773873289'

# Now, lets ccreate an objecct of EAN13
# class and pass the number
my_code = EAN13(number)

# Our barcode is ready. Lets save it.
my_code.save("new_code")
