from PIL import Image
import random
a=input()
img = Image.open(a)
pixels = img.load()
#filesv=input("Укажите куда вы хотите сохранять файл")

def baw():
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            z = (r + g + b) // 3
            r =z
            g =z
            b = z
            pixels[i, j]=(r, g, b)
    img.show()
    #img.save(filesv)
       
def twocolors():
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            z = (r + g + b) // 3
            if nb > z:
                pixels[i, j] = (237, 28, 28)
            else:
                pixels[i, j]=(7, 13, 58)
    img.show
    #img.save(filesv)


def contrast():
    nb=int(input("Напишите число с 50 до 200"))
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            some=random.randint(-nb, nb)
            r +=some
            b +=some
            g +=some

            if r > 255:
             r = 255
            if g > 255:
                g = 255
            if b > 255:
                 a = 255
            if r < 0:
                r=0
            if g < 0:
                g=0
            if b < 0:
                b=0
            pixels[i, j]=(r, g, b)
    img.show()
    #img.save(filesv)
    

def squares():
    for i in range(img.width//2, img.width ):
        for j in range(img.height//2, img.height):
            r, g, b = pixels[i, j]
            r+=39
            g+=90
            b+=18
            pixels[i, j]=(r, g, b)

    for k in range(0, img.width//2):
        for t in range(0, img.height//2):
            r, g, b = pixels[k, t]
            g+=10
            r+= 25
            b+=130
            pixels[k, t]=(r, g, b)

    for z in range(img.width//2,  img.width):
        for x in range(0, img.height//2):
            r, g, b = pixels[z, x]
            b+=130
            r+=10
            g+=190
            pixels[z, x]=(r, g, b)

    for y in range(0,  img.width//2):
        for f in range(img.height//2, img.height):
            r, g, b = pixels[y, f]
            b+=45
            r+=150
            g+=5
            pixels[y, f]=(r, g, b)
    img.show()
    #img.save(filesv)

def mirror():
    for i in range(img.width//2+1):
        for j in range(img.height):
            pixels[img.width-1-i, j]=pixels[i, j]
    img.show()
    #img.save(filesv)

def blur():
    from PIL import ImageFilter
    im1 = img.filter(ImageFilter.BLUR)
    im1.show()
    #img.save(filesv)


def fourlights():
    img_size = img.size
    new_img = Image.new('RGB', (2*img_size[0],2*img_size[1]))
    for i in range(0,2*img_size[0],img_size[0]):
        for j in range(0,2*img_size[1],img_size[1]):
            new_img.paste(img, (i,j))
    new_img.show()
    #img.save(filesv)

def collage():
    b=input("Введите 1 фото")
    c=input("Введите 2 фото")
    d=input("Введите 3 фото")
    e=input("Введите 4 фото")
    img = Image.open(b)
    img1 = Image.open(c)
    img2 = Image.open(d)
    img3 = Image.open(e)
    img_size = img.size
    new_img = Image.new('RGB', (2156,2*img_size[1]))
    new_imgg.paste(img, (0,0))
    new_im.paste(img2, (0,img_size[1]))
    new_img.paste(img1, (1000,0))
    new_im.paste(img3, (1000,img_size[1]))
    new_im.show()
    #img.save(filesv)

print("Выберете ваш фильтр :")
print("1 4рех цветное фото ")
print("2 Колаж 4рех фотов")
print("3 Размытость")
print("4 Зеркальность фотки")
print("5 Шум на фоту")
print("6 4рех светное фото")
print("7 Черно-белоё фото")
print("8 2ух цветноё фото")
choice=int(input())
if choice == 1:
    squares()
if choice == 2:
    collage()
if choice == 3:
    blur()
if choice == 4:
    mirror()
if choice == 5:
    contrast()
if choice == 6:
    fourlights()
if choice == 7:
    baw()
if choice == 8:
    twocolors()

