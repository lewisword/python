from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    #加载一个TrueType或者OpenType字体文件，并且创建一个字体对象。这个函数从指定的文件加载了一个字体对象，并且为指定大小的字体创建了字体对象。
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)#为图片加上指定的文字，这个是99，可以设置字体和颜色，第一个参数是指定位置，分别是距离左边缘和上边缘的距离
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)
