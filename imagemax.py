from PIL import Image
import os
import glob
def Picture_Synthesis(mother_img,
                      son_img,
                      save_img,
                      coordinate=None):
    """
    :param mother_img: 母图
    :param son_img: 子图
    :param save_img: 保存图片名
    :param coordinate: 子图在母图的坐标
    :return:
    """
    #将图片赋值,方便后面的代码调用
    M_Img = Image.open(mother_img)
    S_Img = Image.open(son_img)
    factor = 1#子图缩小的倍数1代表不变，2就代表原来的一半

    #给图片指定色彩显示格式
    M_Img = M_Img.convert("RGBA")  # CMYK/RGBA 转换颜色格式（CMYK用于打印机的色彩，RGBA用于显示器的色彩）

    # 获取图片的尺寸
    M_Img_w, M_Img_h = M_Img.size  # 获取被放图片的大小（母图）
    print("母图尺寸：",M_Img.size)
    S_Img_w, S_Img_h = S_Img.size  # 获取小图的大小（子图）
    print("子图尺寸：",S_Img.size)

    size_w = int(S_Img_w / factor)
    size_h = int(S_Img_h / factor)

    # 防止子图尺寸大于母图
    if S_Img_w > size_w:
        S_Img_w = size_w
    if S_Img_h > size_h:
        S_Img_h = size_h

    # # 重新设置子图的尺寸
    # icon = S_Img.resize((S_Img_w, S_Img_h), Image.ANTIALIAS)
    icon = S_Img.resize((S_Img_w, S_Img_h), Image.ANTIALIAS)
    w = int((M_Img_w - S_Img_w) / 2)
    h = int((M_Img_h - S_Img_h) / 2)

    try:
        if coordinate==None or coordinate=="":
            coordinate=(w, h)
            # 粘贴子图到母图的指定坐标（当前居中）
            M_Img.paste(icon, coordinate, mask=None)
        else:
            print("已经指定坐标")
            # 粘贴子图到母图的指定坐标（当前居中）
            M_Img.paste(icon, coordinate, mask=None)
    except:
        print("坐标指定出错 ")
    # 保存图片
    M_Img.save(save_img)

if __name__ == "__main__":
    Image_glob = os.path.join("C:/Users/tim/Desktop/pdf/image", "*.png")
    Image_list = []
    Image_list.extend(glob.glob(Image_glob))
    # print(Image_list[::])
    # print(len(Image_list))
    num = 0
    for filename in Image_list:
        print(filename)
        
        Picture_Synthesis(mother_img="C:/Users/tim/Desktop/pdf/background/a443.png",
                            son_img=filename,
                            save_img="C:/Users/tim/Desktop/pdf/finalimage/" +str(num)+ "newimg.png",
                            #   coordinate=None#如果为None表示直接将子图在母图中居中也可以直接赋值坐标
                            coordinate=(250,0)
                            )
        num = num +1
    # path = r'C:\Users\tim\Desktop\tttt' # 路径
    # n = len(os.listdir(path))
    # print('共有{}张PDF'.format(n))
    # i=1
    # for filename in os.listdir(path):
    #     # 1、PDF地址
    #     pdfPath = path+'/'+filename
    #     # 2、需要储存图片的目录
    #     imagePath = r'C:\Users\tim\Desktop\pdf\image'
    #     pyMuPDF_fitz(pdfPath, imagePath,i)
    #     print('已处理{}张PDF，剩余{}张PDF'.format(i,(n-i)))
    #     i=i+1
    

# from PIL import Image
# import os
# import random
 
 
# def handle_img(imgdir,imgFlodName,img_path):
#     imgs = os.listdir(imgdir+imgFlodName)
#     imgNum = len(imgs)
#     print(imgNum)
#     image_ori = os.listdir(img_path)
#     image_Num = len(image_ori)
#     print(image_Num)
 
#     for i in range(imgNum):
#         img1 = Image.open(imgdir + imgFlodName + "/" + imgs[i])
#         img = img1.resize((102,102))
 
#         for j in range(image_Num):
 
#             oriImg = Image.open(img_path + "/" + image_ori[j])
#             image = oriImg.size
#             # oriImg.paste(img, (image[0]-102, image[1]-102))
 
#             if image[0]<image[1]:
#                 oriImg.paste(img,(random.randint(0,image[0]-102),random.randint(0,image[0]-102)))
#             else:
#                 oriImg.paste(img, (random.randint(0, image[1]-102), random.randint(0, image[1]-102)))
#             oriImg.show()
#             oriImg1 = oriImg.convert('RGB')
#             oriImg1.save("F:/Download/sign2_data"+"/"+str(i)+".jpg")
 
 
# imgdir = "F:/Download/"
# imgFlodName = "v2.0sign_picture"
# image_path = "F:/Download/image"
# handle_img(imgdir,imgFlodName,image_path)