import nhs_number
import pyperclip

def generator():
    number = nhs_number.generate(quantity=1, for_region=nhs_number.REGION_ENGLAND)
    pyperclip.copy(number[0])
    print(number[0])

generator()