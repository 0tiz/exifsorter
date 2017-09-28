import piexif

exif_data = piexif.load("C:\\projekt\\vmanifest\\User\\Hurricane\\images\\Hurrican Proflyer.jpg")
print(exif_data['0th'][306])
