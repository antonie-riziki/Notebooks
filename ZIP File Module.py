import zipfile

""" Zipping and Compression of files """
with zipfile.ZipFile("files.zip","w", compression = zipfile.ZIP_DEFLATED) as myZip:
    myZip.write("hubble_data.csv")
    myZip.write("hubble_data_copy.txt")
