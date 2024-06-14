import qrcode
import os
import shutil

# function to create qrcode given link and file name
def generate_qrcode(link, file_name):
    # create qrcode object
    qrc = qrcode.QRCode(
        version = 1,
        box_size = 10,
        border = 5
    )
    qrc.add_data(link)
    qrc.make(fit = True)
    img = qrc.make_image(fill_color = "#000000", background = "#ffffff")
    img.save(file_name)

# prompt user for details
link = input("Enter the url: ")
file_name = input("Enter the name of the QRCode: ")
file_name += ".png"

# call function
generate_qrcode(link, file_name)
print(f"Successfully saved file as {file_name}")

# path to folder containing all qrcodes
qrc_directory_path = "/Users/anushapatel/Downloads/QRCodes"

# if folder does not exist, make one
if os.path.exists(qrc_directory_path) == False:
    print("The directory does not exists.")
    os.mkdir(qrc_directory_path)

# move newly made .png to new directory
shutil.move(file_name, qrc_directory_path)