import os
from PIL import Image

os.chdir('imgs') # поменяем директорию на ту, где у нас расположены картинки
# recolor_green = True

for fname in os.listdir(os.getcwd()): # os.listdir - соответственно, есть ли что-нибудь, у нас, в папке,
    try:
        if ".bmp" in fname:
            # print(fname, os.path.splitext(fname))
            # if recolor_green:
            #     print("Recoloring")
            #     img = Image.open(fname)
            #     img = img.convert("RGBA")
            #     pixdata = img.load()
            #     for y in range(img.size[1]):
            #         for x in range(img.size[0]):
            #             if pixdata[x, y] != (255, 255, 255, 255):
            #                 print(pixdata[x, y])
                        # if pixdata[x, y] == (255, 255, 255, 255):
                            # pixdata[x, y] = (0, 0, 0, 255)
            Image.open(fname).save(os.path.splitext(fname)[0] + '.png') # а os.getcwd() - папка, в которую мы однажды перешли
            os.remove(fname)
    except Exception as e:
        print(e)
        print('Sorry, we have no pictures.')