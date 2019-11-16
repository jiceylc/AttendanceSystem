#Attendance System



##                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Installation 

The front-end framework of this project uses HTML, CSS and JavaScript, the backend framework of this project uses tornado, this project is based on Python 3.7.

To run the Attendance System, you need to install some packages, the list of the packages it requires additional as follow.

- numpy
- cmake
- dlib                                               
- opencv-python
- tornado
- pymysql

 `cd` to the Attendance System folder and run the install command:

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple cmake
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple dlib
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tornado
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql
```



## Use tutorial

###1. Connecting to `SUDA_WIFI`

 

###2. Go to the following page:

```
http://10.40.36.78:8099/log
```



###3. Log in the above page:

```
Account Number: admin
Passwd: 123456
```



###4. Then you see the layout in the page just like follows:

|       签到(Check In)        | 添加用户(Add User) |
| :----------------------: | :----------------: |
| 查询记录(Query the records) | 说明(Instructions) |

If you push the "Add User" button. You can add the student's name and student ID while uploading the user's photo. We also offer the option to delete users in case you make mistakes when adding users.



If you push the "Check in" button. You can upload a photo containing one or more faces, the program will return the check-in results, which is a triple including the serial number, name and check-in status. For example, (1, “Donald”, "未签到").  We even made a sort, the unsigned student's entry will go up.



If you push the "Query the records" button. You can check the check-in record by date and name. If you check in the check-in record by date, for example, you want to check the attendance record on November 5, 2019, or check the attendance record of Donald, the system will return the results you want.



If you push the "Instructions" button. The system will return our default instructions.



###5. Then you start using this attendance system:

When the time Attendance System is used for the attendance of a course, you log in to the system as an administrator. First, you must enter the information of the student who took the course through the “Add user” button, including the students' name, students' ID and their photos. 

When it's in class, you should take a picture of the classmates who took the class (ask them to face the camera).Then push the "Check in" button, upload the photo of the students, the program will detect the faces in the picture and perform grayscale and resize processing. The program will then compare the student photos in the database with uploaded photos one by one. When it is detected that a photo in the database is highly consistent with one of the uploaded photos, it is determined that the student corresponding to the photo comes to class, and then store the information in a three-tuple form in the state table. 

After all the comparisons completed, the program will return the information in the status table according to the webpage to a certain format. You can see the students who have signed in and the students who have not signed in on the webpage.









# 考勤系统



## 安装



该项目的前端框架使用HTML，CSS和JavaScript，后端框架使用Tornado; 该项目基于Python 3.7。
为了运行考勤系统，您需要安装一些软件包，其中还需要其他软件包列表，如下所示：

- numpy
- cmake
- dlib                                               
- opencv-python
- tornado
- pymysql

通过 `cd`命令进入考勤系统文件夹并且运行以下安装命令： 

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple cmake
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple dlib
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tornado
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql
```



##使用教程

### 1. 连接 `SUDA_WIFI`

 

### 2. 进入以下网页:

```
http://10.40.36.78:8099/log
```



### 3. 登录网页:

```
Account Number: admin
Passwd: 123456
```



### 4. 网页的布局如下:

|       签到(Check In)        | 添加用户(Add User) |
| :-------------------------: | :----------------: |
| 查询记录(Query the records) | 说明(Instructions) |

如果按下“添加用户”按钮。 您可以在上传用户的照片时添加学生的姓名和学生ID。 我们还提供了删除用户的选项，以防您在添加用户时出错。



如果按下“签到”按钮。 您可以上传一张包含一张或多张面孔的照片，程序会返回签到结果，该结果是三元组，包括序列号，名称和签到状态。 例如，（1，“ Donald”，“未签到”）。 我们对状态表中的信息进行了排序，未签名学生的条目将会上浮。



如果按下“查询记录”按钮。 您可以按日期和名称查看入住记录。 例如，如果您按日期检查签到记录，例如您想查看2019年11月5日的考勤记录，或查看Donald的考勤记录，系统将返回您想要的结果。



如果您按下“说明”按钮。 系统将返回我们预设的说明。
