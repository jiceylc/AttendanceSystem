import cv2 
def detect(filename):
    trainnum = 1
    #加载分类器
    face_cascade=cv2.CascadeClassifier("classifier.xml")

    #读取图像
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #人脸检测
    faces = face_cascade.detectMultiScale(gray,1.3,5)


    #绘制矩形框
    for (x,y,w,h) in faces:
        imgshow = "train%d" %trainnum
        imgout = "train%d.jpg" %trainnum

        #仅绘制识别的图像
        f = cv2.resize(gray[y:(y+h),x:(x+w)],(200,200))
        print(f)
        # print(num)
        cv2.imshow(imgshow,f)
        cv2.imwrite(imgout,f)
        trainnum+=1

if __name__ == "__main__":
    detect("2.jpg")
    cv2.waitKey()
    cv2.destroyAllWindows()
