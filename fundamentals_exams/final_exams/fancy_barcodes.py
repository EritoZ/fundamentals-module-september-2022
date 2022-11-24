import re

barcodes_amount = int(input())

for _ in range(barcodes_amount):
    valid_barcode = re.search(r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+", input())

    if valid_barcode:
        digits = re.findall(r"\d+", valid_barcode.group())

        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")

