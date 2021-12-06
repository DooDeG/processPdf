#!/usr/local/python3.8.1
# coding: utf-8
# author: kanong2020
import os
import glob
import fitz
 
# 防止字符串乱码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
 
 
 
def frompic2pdf(img_path, pdf_path, pdf_name):
    # print(img_path + pdf_name + '.jpg')
    # 使用glob读图
    for img in sorted(glob.glob(img_path + pdf_name + '.png')):
        # 打开空文档
        doc = fitz.open()
        # 打开指定图片
        imgdoc = fitz.open(img)
        # 使用图片创建单页的PDF
        pdfbytes = imgdoc.convertToPDF()
        imgpdf = fitz.open("pdf", pdfbytes)
        # 将当前页写入文档
        doc.insertPDF(imgpdf)
        # 保存为指定名称的PDF文件
        doc.save(pdf_path + pdf_name + '.pdf')
        # 关闭
        doc.close()
 
 
if __name__ == '__main__':
    # 读取图片地址
    img_path = r'C:\Users\tim\Desktop\pdf\finalimage\\'
    # 即将生成的pdf的目标地址
    pdf_path = r'C:\Users\tim\Desktop\pdf\finalpdf\\'
    num = 0
    for root, dirs, files in os.walk(img_path):
        for file in files:
            # 目标文件名称 无后缀
            destfileName = os.path.splitext(file)[0]
            print(num)
            num = num +1
            frompic2pdf(img_path=img_path, pdf_path=pdf_path, pdf_name=destfileName)
 