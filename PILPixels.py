from PIL import Image
import pathlib
import requests
import glob

def OnlineImage(Link:str):
    Req = requests.get(Link)
    with open("OnlineImage.jpg", "wb") as OnlineImWrite:
        OnlineImWrite.write(Req.content)
    return "OnlineImage.jpg"

def Base10ToBase2(Number, Amount=8):
    #Base 2
    Number = int(Number)
    Bin = (bin(Number).replace("0b", ''))
    if len(Bin) == Amount:
        return Bin
    elif len(Bin) > Amount:
        print("Too high")
        return
    return "0"*(Amount-len(Bin))+Bin

def Saver(im:Image.Image):
    with open("ThumbnailSave.jpeg", "wb") as ThumbnailSave:
        Thumbnail = im.convert(mode="RGB")
        Thumbnail.thumbnail((255,255))
        Thumbnail.save(ThumbnailSave)
    with open("ResizeSave.jpeg", "wb") as ResizeSave:
        Resize = im.convert(mode="RGB").resize((255,255))
        Resize.save(ResizeSave)
    return ThumbnailSave, ResizeSave

Pics = ["Test.png", "B&WLandscape.png", "DOG.jpg", "Paint.png", "PurpToYello.png"] #, OnlineImage("")]

with Image.open(Pics[1], mode="r") as im:
    Thumb, Resize = Saver(im)
    Input = input("ThumbnailSave.jpeg (1) or ResizeSave.jpeg (2)\n")
    if Input == "2":
        SmallIm = Image.open("ResizeSave.jpeg", mode="r")
    else:
        SmallIm = Image.open("ThumbnailSave.jpeg", mode="r")
    pathlib.Path(Resize.name).unlink()
    pathlib.Path(Thumb.name).unlink()
    print(f"Image size: {SmallIm.size} (width, height)")
    RGBPixelList = (SmallIm.convert(mode="RGB").getdata())
    FlattedList = []
    for x in RGBPixelList:
        for y in x:
            FlattedList += [y]
    BinaryPixels = list(map(Base10ToBase2, FlattedList))

with open("BinaryOutput.txt", "w") as F:
    F.write(f"{Base10ToBase2(SmallIm.width)}\n{Base10ToBase2(SmallIm.height)}\n{Base10ToBase2(24)}\n")
    F.write(''.join(BinaryPixels))
