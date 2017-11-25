# YOLO_on_the_ROS
This code is to run YOLO with python + opencv3.3.1 on the ROS(Robotic Operating System)
If you publish your own image with the topic "camera/image_color,
   then this package would re-publish the image-annotated with the topic "MyDarknet/img_annotated"

Reference
Paper : Redmon, Joseph, et al. "You only look once: Unified, real-time object detection." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2016.
Site : https://pjreddie.com/darknet/yolo/

Used Opencv
Github : https://github.com/opencv/opencv/blob/master/samples/dnn/yolo_object_detection.cpp

![Alt text](/src/img_annotated.png?raw=true "origin image")
