# Progrram Name 3 QR Code and Barcode genetator and decoding (Borcode Deecoder)
# importing library
'''import cv2
from pyzbar.pyzbar import decode

# Meke onne method to decode the barcode
def BarcodeReader(image):
    # read the image in numpy array using cv2
    img = cv2.imread(image)

    # Decode the barcode image
    detectedBarcodes = decode(img)

    # if not detected then print the maessage
    if not detectedBarcodes:
        print("Barcode Not Detected or your barccode is blank/corrupted!")
    else:
        # Traverse through all the detected barcods in image
        for barcode in detectedBarcodes:
            # Locate the barcode position in image
            (x,y,w,h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                # Print the barcode data
                print(barcode.data)
                print(barcode.type)

    # Display the image
    cv2.imshow("lmage",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # take the image from user
    image = "img.jpg"
    BarcodeReader(image)
'''

import cv2
from pyzbar.pyzbar import decode

def BarcodeReader(image):
    try:
        img = cv2.imread(image)

        if img is None:
            print("Error: Unable to read the image file.")
            return

        detected_barcodes = decode(img)

        if not detected_barcodes:
            print("Barcode Not Detected or the barcode is blank/corrupted!")
        else:
            for barcode in detected_barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                if barcode.data != "":
                    print("Barcode Data:", barcode.data)
                    print("Barcode Type:", barcode.type)

        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    image = "img.jpg"  # Update the image path accordingly
    BarcodeReader(image)
