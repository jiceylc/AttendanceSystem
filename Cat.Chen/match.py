import cv2
import numpy as np

def match(photolst):
    lst=['1.png','3.png','template.jpg',"4.png"]
    # ,'3.png','template.jpg'
    #读入图像
    img=cv2.imread(photolst,0)
    #cv2.imshow("2",img)
    resd =[]
    for i in lst:
        template=cv2.imread(i,0)
    # cv2.imshow("1",template)
        w,h=template.shape[::-1]

        #图像预处理
        #filter2D方法
        fil = np.array([[-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]],dtype="float32")

        res = cv2.filter2D(img,-1,fil)   
    # cv2.imshow("res",res)

        #高斯函数
        dst=cv2.GaussianBlur(img,(5,5),0)
        #cv2.imshow('dst',dst)

        #六种相似度计算方法
        # methods = ['cv2.TM_CCOEFF_NORMED']
    # 'cv2.TM_CCOEFF', , 'cv2.TM_CCORR','cv2.TM_CCOEFF_NORMED'
    #               'cv2.TM_CCORR_NORMED' , ['cv2.TM_SQDIFF'], 
        #模板匹配

        img1=dst.copy()
        # method=eval(meth)
        res=cv2.matchTemplate(img1,template,cv2.TM_CCOEFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
        if(max_val>0.7):
            resd.append(i+"已签到")
            # if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
            #     top_left=min_loc
            # else:
            #     top_left=max_loc
            # bottom_right=(top_left[0]+w,top_left[1]+h)
            # cv2.rectangle(img1,top_left,bottom_right,255,2)
        # cv2.imshow("rect",img1)#循环为何只输出一张rect？
            img=img1
    return resd
    # cv2.imshow('final',img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()


