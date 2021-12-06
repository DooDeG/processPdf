import datetime
import random
import os

import fitz  # fitz就是pip install PyMuPDF

def pyMuPDF_fitz(pdfPath, imagePath,i):  # PDF路径 保存图片路径 PDF编号
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    # print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = random.uniform(-0.8,0.8) # 页面旋转随机角度
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        # zoom_x = 5 # 修改该参数可以改变像素
        # zoom_y = 5
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.writePNG(imagePath + '/' + 'image{}_{}.png'.format(i,pg))  # 将图片写入指定的文件夹内
                                                       # 第i张pdf的第pg页

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    # print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


if __name__ == "__main__":
    path = r'C:\Users\tim\Desktop\tttt' # 路径
    n = len(os.listdir(path))
    print('共有{}张PDF'.format(n))
    i=1
    for filename in os.listdir(path):
        # 1、PDF地址
        pdfPath = path+'/'+filename
        # 2、需要储存图片的目录
        imagePath = r'C:\Users\tim\Desktop\pdf\image'
        pyMuPDF_fitz(pdfPath, imagePath,i)
        print('已处理{}张PDF，剩余{}张PDF'.format(i,(n-i)))
        i=i+1