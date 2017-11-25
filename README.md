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
