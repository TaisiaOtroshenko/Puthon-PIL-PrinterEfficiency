from PIL import Image, ImageDraw, ImageFont
import statistics as stat

s = input("Введите путь до файла: ")
image = Image.open(s)
draw = ImageDraw.Draw(image)
pix = image.load()
b_pixs = []
for i in range(image.size[0]):
    for j in range(image.size[1]):
        p = pix[i, j]
        b_pixs.append(stat.mean([p[0], p[1], p[2]]))
t = 100-stat.mean(b_pixs)*100/255
print("Процент черной краски в изображении -", "%.3f" % t, "%")
