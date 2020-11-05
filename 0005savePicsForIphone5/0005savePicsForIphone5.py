#encoding=utf-8
#第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import cv2

def cutImageforIpad():
    img=cv2.imread("img001.jpg")
    cv2.namedWindow("windows1")
    cv2.imshow("windows1", img)
    cv2.waitKey(0)
    height=img.shape[0]
    width=img.shape[1]
    print("original shape: height="+str(height)+" width="+str(width))
    img=img[int(height/2):height, 0:width]
    #print("now shape: height=%d width=%d"%(height/2)%width)
    cv2.imshow("windows1", img)
    cv2.waitKey(0)


cutImageforIpad()


