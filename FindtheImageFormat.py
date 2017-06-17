def photoExtension():

    fileName = input("File Name ? ")                            #It's better to ask here, why adding new func for this ?!

    try:
        fh = open(fileName, 'rb').read(10)                      #read the first 10 bytes of the image file

        if fh[6:11] in [b'JFIF', b'Exif']:                      #If there are JFIF or Exif bytes between 7 and 10 bytes, jpeg
            print("The extension of {} is JPEG".format(fileName))

        elif fh[:8] == b'\211PNG\r\n\032\n':                    #The first 8 bytes of png contain the following value: b'\x89PNG\r\n\x1a\n'
            print("The extension of {} is PNG".format(fileName))

        elif fh[:3] == b'GIF':                                  #the first 3 bytes of gif contain: GIF
            print("The extension of {} is GIF".format(fileName))

        elif fh[:2] in [b'II', b'MM']:                          #the first 2 bytes of TIFF contain : b'II' or b'MM'
            print("The extension of {} is TIFF".format(fileName))

        elif fh[:2] in [b'BM']:                                 #the first 2 bytes of BMP contain : b'BM'
            print("The extension of {} is BMP".format(fileName))

    except FileNotFoundError:
        print("The file was not found...")


if __name__ == '__main__':
    photoExtension()
