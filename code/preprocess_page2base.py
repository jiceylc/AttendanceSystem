import cv2


def preprocess(filename,id):

    # 加载分类器
    face_cascade = cv2.CascadeClassifier("classifier.xml")

    # 读取图像
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 人脸检测
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 绘制矩形框
    for (x, y, w, h) in faces:
        # cv2.imshow(filename, img)
        # 仅绘制识别的图像
        f = cv2.resize(gray[y:(y+h), x:(x+w)], (200, 200))
        # print(f)
        # cv2.imshow(filename, f)
        filename="static/template/"+id+".jpg"
        print(filename)
        cv2.imwrite(filename, f)
    return filename

# if __name__ == "__main__":
#     preprocess("new.jpg","1627405118")
#     cv2.waitKey()
#     cv2.destroyAllWindows()
