from pyzbar.pyzbar import decode
import cv2

def read_barcode(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Decode the barcodes in the image
    barcodes = decode(gray)

    # Print the decoded information
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        print(f"Barcode Data: {barcode_data}")

# Replace 'your_barcode_image.png' with the actual path to your PNG image
image_path = 'my_barcode.png'
read_barcode(image_path)
