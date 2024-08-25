import cv2
from pyzbar.pyzbar import decode

# Read Image
def read_image(image_filename):
    img = cv2.imread(image_filename)
    return img

# Show Image
def show_image(window_name, image_file):
    cv2.imshow(window_name, image_file)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_barcode(barcodes_images):
    barcodes = decode(img)
    for b in barcodes:
        barcode_data = b.data.decode("utf-8")
        barcode_type = b.type
    print(f"   DATA : {barcode_data}\n   TYPE : {barcode_type}")
    print(f"\n\n\nComplete decoded data : {barcodes}")

if __name__ == "__main__":
    #path to images
    barcode_jpg = "images/barcode.jpg"       
    barcode_png = "images/barcode_1.png"   

    img = read_image(barcode_png)            #read image
    show_image("Barcode", img)           #view image
    read_barcode(img)                    #read barcode data
