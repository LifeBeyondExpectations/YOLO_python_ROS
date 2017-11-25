# YOLO + Python + ROS
This code is to run YOLO with python + opencv3.3.1 on the ROS(Robotic Operating System)
If you publish your own image with the topic "camera/image_color,
   then this package would re-publish the image-annotated with the topic "MyDarknet/img_annotated"

Reference
Paper : Redmon, Joseph, et al. "You only look once: Unified, real-time object detection." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2016.
Site : https://pjreddie.com/darknet/yolo/

Used Opencv
Github : https://github.com/opencv/opencv/blob/master/samples/dnn/yolo_object_detection.cpp

![Alt text](/src/img_annotated.png?raw=true "origin image")

#Dependency
1. Opencv 3.3.1
2. ROS-lunar
3. python (version does not matter)

#How to run
1. download package in your catkin_ws directory
2. catkin_make
3. publish your own image with the topic 'camear/image_color' or just you can modify the topic in yolo.py 
4. rosrun ${your package name} yolo.py
5. rosrun image_view image_view image:=MyDarknet/image_annotated

#Review : YOLO(c++) + opencv  + ROS does not work. 
I tried to run yolo.cpp which is not uploaded in this git, but failed because of the version of the opencv in ROS. If you install ROS-Lunar with full packages, opencv will be automatically installed with the version 3.2.0. For me, this version of opencv does not run yolo_object_detection.cpp(https://github.com/opencv/opencv/blob/master/samples/dnn/yolo_object_detection.cpp) 

After that, I installed newly updated opencv 3.3.1 and change CMakeList.txt to look up the opencv packages. Then it works. But the problem still exists. Opencv-ROS provide some packages such as image_transport or cv_bridge etc .. they are running on the opencv3.2 which is built-in on the ROS with binary files. In short, subscribing image need opencv3.2.0(I hope that ros-opencv would update their own version) yolo-opencv-cpp needs opencv3.3.1.

I cannot find the good solution to change the binary files of opencv3.2.0 which is buil-in on the ROS with opencv3.3.1 that I newly installed. If possible, then everything gonna work well in cpp + yolo + ROS. Since it dose not work well from now on, Python is the second-choice we have. I am not sure about its policy of compilers, it can run yolo.py with different version of opencv so that it can solve the matter.
