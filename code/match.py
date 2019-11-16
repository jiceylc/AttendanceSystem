# import face_recognition
# import cv2


def detect(filename):
    # print(filename)

    trainnum = 1
    waittorecoglst = []

    # 加载分类器
    face_cascade = cv2.CascadeClassifier("classifier.xml")

    # 读取图像
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 人脸检测
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 绘制矩形框
    for (x, y, w, h) in faces:
        imgshow = "train%d" % trainnum
        imgout = "train%d.jpg" % trainnum

        # 仅绘制识别的图像
        f = cv2.resize(gray[y:(y + h), x:(x + w)], (200, 200))
        # print(imgout)
        # print(f)
        # print(num)
        # cv2.imshow(imgshow, f)
        cv2.imwrite(imgout, f)
        waittorecoglst.append(imgout)
        # print(waittorecoglst)
        trainnum += 1
    # print(waittorecoglst)

    return waittorecoglst


# def recognition(baselst, baselabel, waittorecoglst):

#     # 存放提取数据库特征的人脸(图片格式)
#     base_encoding = []
#     for i in range(len(baselst)):
#         img = face_recognition.load_image_file(baselst[i])
#         tmp = face_recognition.face_encodings(img)[0]
#         base_encoding.append(tmp)
#     # print(len(base_encoding))
    

#     # 将分割的待测人脸提取特征
#     wait_encoding = []
#     for j in range(len(waittorecoglst)):
#         img = face_recognition.load_image_file(waittorecoglst[j])
#         tmp = face_recognition.face_encodings(img)[0]
#         wait_encoding.append(tmp)
#     # print(len(wait_encoding))

#     # 创建存储人员签到信息的字典，以姓名为键，以签到状态为值，0为未签到，1为已签到，默认为0
    # ans = {}
    # for m in range(len(base_encoding)):
    #     ans[baselabel[m]] = 0
    # # print(res)

#     # 人脸比较,用数据库中的人脸去对比待检测的人脸
#     # times = 1
#     for m in range(len(base_encoding)):
#         for n in range(len(wait_encoding)):
#             result = face_recognition.compare_faces([wait_encoding[n]],
#                                                     base_encoding[m],
#                                                     tolerance=0.8)
#             # print(times,result)
#             if True in result:
#                 # print(baselabel[m], "已签到")
#                 ans[baselabel[m]] = 1
#             # times += 1
#         # print(baselabel[m], "未签到")
#     # print(res)

    # # 将ans按照签到状态排序，使已签到的人员上浮
    # ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    # return ans


# # #
# # waittorecoglst = detect("source/1572941767.4229524wait_to_recog.jpg")
# # print(waittorecoglst)
# print(
#     recognition([
#         "temp/xilali.jpg",  "temp/ycy1.jpg",
#          "temp/obama1.jpg","temp/lfz1.jpg"
#     ], ['希拉里', '杨超越', '奥巴马',"李凡长"], ["temp/ycy2.jpg","temp/wjk.jpg"]))
# # print(
#     # recognition(['static/template/1627405118.jpg','static/template/1627405118.jpg','temp/ycy1.jpg','temp/wjk.jpg'],['谢铁良','崔雨豪','杨超越','王俊凯'],['temp/ycy2.jpg','temp/xusong2.jpg']))



# import sys,os,dlib,glob,numpy
# from skimage import io

# # 1.人脸关键点检测器
# predictor_path = sys.argv[1]
# # 2.人脸识别模型
# face_rec_model_path = sys.argv[2]
# # 3.候选人脸文件夹
# faces_folder_path = sys.argv[3]
# # 4.需识别的人脸
# img_path = sys.argv[4]
 
# # 1.加载正脸检测器
# detector = dlib.get_frontal_face_detector()
# # 2.加载人脸关键点检测器
# sp = dlib.shape_predictor(predictor_path)
# # 3. 加载人脸识别模型
# facerec = dlib.face_recognition_model_v1(face_rec_model_path)
 
# # win = dlib.image_window()
# # 候选人脸描述子list
# descriptors = []
# # 对文件夹下的每一个人脸进行:
# # 1.人脸检测
# # 2.关键点检测
# # 3.描述子提取
 
# for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
#     print("Processing file: {}".format(f))
#     img = io.imread(f)
#     #win.clear_overlay()
#     #win.set_image(img)
 
#     # 1.人脸检测
#     dets = detector(img, 1)
#     print("Number of faces detected: {}".format(len(dets)))
#     for k, d in enumerate(dets):  
#         # 2.关键点检测
#         shape = sp(img, d)
#         # 画出人脸区域和和关键点
#         # win.clear_overlay()
#         # win.add_overlay(d)
#         # win.add_overlay(shape)
#         # 3.描述子提取，128D向量
#         face_descriptor = facerec.compute_face_descriptor(img, shape)
#         # 转换为numpy array
#         v = numpy.array(face_descriptor)  
#         descriptors.append(v)
 
# # 对需识别人脸进行同样处理
# # 提取描述子，不再注释
# img = io.imread(img_path)
# dets = detector(img, 1)
# dist = []
# for k, d in enumerate(dets):
#     shape = sp(img, d)
#     face_descriptor = facerec.compute_face_descriptor(img, shape)
#     d_test = numpy.array(face_descriptor) 
 
#     # 计算欧式距离
#     for i in descriptors:
#         dist_ = numpy.linalg.norm(i-d_test)
#         dist.append(dist_)
 
# # 候选人名单
# candidate = ['/temp','Unknown2','Shishi','Unknown4','Bingbing','Feifei']
# # 候选人和距离组成一个dict
# c_d = dict(zip(candidate,dist))
# cd_sorted = sorted(c_d.items(), key=lambda d:d[1])
# print('\n The person is: %s' % ( cd_sorted[0][0] )  )  
# dlib.hit_enter_to_continue()

 
# coding:utf-8


import dlib
import cv2
import glob
import numpy as np


class face_recognition:

    def __init__(self,predictor_path,face_rec_model_path):

        self.predictor_path = predictor_path
        self.face_rec_model_path = face_rec_model_path
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor(self.predictor_path)
        self.face_rec_model = dlib.face_recognition_model_v1(self.face_rec_model_path)

    def face_detection(self,url_img_1,url_img_2):

        img_path_list = [url_img_1,url_img_2]
        dist = []

        for img_path in img_path_list:
            img = cv2.imread(img_path)
            # 转换rgb顺序的颜色。
            b, g, r = cv2.split(img)
            img2 = cv2.merge([r, g, b])
            # 检测人脸
            faces = self.detector(img, 1)

            if len(faces):
                for index, face in enumerate(faces):
                    # # 提取68个特征点
                    shape = self.shape_predictor(img2, face)
                    # 计算人脸的128维的向量
                    face_descriptor = self.face_rec_model.compute_face_descriptor(img2, shape)

                    dist.append(list(face_descriptor))
            else:
                pass
        return dist

    # 欧式距离

    def dist_o(self,dist_1,dist_2):
        dis = np.sqrt(sum((np.array(dist_1)-np.array(dist_2))**2))
        return dis

    def score(self,url_img_1,url_img_2):

        url_img_1 = glob.glob(url_img_1)[0]
        url_img_2 = glob.glob(url_img_2)[0]
        data = self.face_detection(url_img_1,url_img_2)
        goal = self.dist_o(data[0],data[1])

        # 判断结果，如果goal小于0.4的话是同一个人，否则不是。我所用的是欧式距离判别
        return 1-goal


# 调用模型 下载地址：http://dlib.net/files/

def recognition(baselst,labellst,waitlst):

    predictor_path = "face_model/shape_predictor_68_face_landmarks.dat"
    face_rec_model_path = "face_model/dlib_face_recognition_resnet_model_v1.dat"
    face_ = face_recognition(predictor_path,face_rec_model_path)

    ans = {}
    for m in range(len(baselst)):
        ans[labellst[m]] = 0
    # print(res)

    for i in range(len(waitlst)):
        for j in range(len(baselst)):
            goal = face_.score(waitlst[i],baselst[j])
            if goal > 0.6:
                # print("{}已签到".format(labellst[j]))
                ans[labellst[j]] = 1
                break

    # 将ans按照签到状态排序，使已签到的人员上浮

    ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    return ans
#
# baseset = ["temp/wjk.jpg","temp/ycy1.jpg","temp/obama1.jpg","source/user_add1573026755.7451136.jpg"]
# labelset = ["王俊凯","杨超越","奥巴马","帅哥"]
# # waitset = ["temp/ycy2.jpg","temp/obama2.jpg"]
# waitlst = detect("wait_to_recog.jpg")
# answer = recognition(baseset,labelset,waitset)
# goal = face_.score(img_1,img_2)
# if(goal > 0.6):
#     print(True)
# else:
#     print(False)

# print(answer)
