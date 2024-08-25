# View availabe barcode types 
import barcode
import barcode.writer
print(barcode.PROVIDED_BARCODES)
# 'codabar', 'code128', 'code39', 'ean', 'ean13', 'ean13-guard', 'ean14', 'ean8', 'ean8-guard', 'gs1', 'gs1_128', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'itf', 'jan', 'nw-7', 'pzn', 'upc', 'upca'

# import barcode type (EAN13) from barcode module 
from barcode import EAN13 

data = '456789123452'
  
# Create Barcode
ean13_code = EAN13(data) 
# Save as svg 
ean13_code.save("images/svg_code")

# Create barcode using writer 
from barcode.writer import ImageWriter

# Save as png image
ean13_code = EAN13(data, writer=ImageWriter(format="PNG")) 
ean13_code.save("images/png_code")

# Save as jpeg image
ean13_code = EAN13(data, writer=ImageWriter(format="JPEG")) 
ean13_code.save("images/jpeg_code")