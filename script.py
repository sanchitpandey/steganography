from PIL import Image

def decode(img):
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                r, g, b, a = img.getpixel((col, row))	
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg

def code(img, msg):
    length = len(msg)
    newImg = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if row == 0 and col == 0 and index < length:
                x = length
            elif index <= length:
                x = ord(msg[index -1])
            else:
                x = r
            newImg.putpixel((col, row), (x, g , b))
            index += 1
    return newImg

def callCode():
    img = Image.open(imgName)
    text = input("Enter text to encode: ")
    outImg = code(img, text)
    outImg.save(outImgName)
    print("File encoded at: {}".format(outImgName))
def callDecode():
    import os
    os.startfile(outImgName)
    im = Image.open(outImgName)
    decoded = decode(im)
    print("Hidden text: {}".format(decoded))

outImgName = ""
imgName = ""

run = "y"
while run == "y":
    imgName = input("Enter image to perform operations on:")
    outImgName = "output-" + imgName
    run1 = input("Do you wish to encode?(y/n)")
    if run1 == "y":
        callCode()
    run2 = input("Do you want to decode?(y/n)")
    if run2 == "y":
        callDecode()

    run = input("Run program again? (y/n)")


    



