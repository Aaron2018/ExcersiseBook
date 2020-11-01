#第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
from cv2 import cv2

def addNoti(num1):
    img=cv2.imread('/Users/carey/Documents/vscode/python/练习册/0000img1.jpg')
    
    w=int(img.shape[0]*0.9)
    h=int(img.shape[1]*0.1)

    cv2.putText(img, num1, (w, h), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    cv2.namedWindow("Image")
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


addNoti(input("Please input what you want to put: "))