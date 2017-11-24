//jaesungchoe
#include "opencv2/core/version.hpp"

#if CV_MINOR_VERSION == 3
#include <opencv2/dnn.hpp>
#include <opencv2/dnn/shape_utils.hpp>
#endif

#if CV_MINOR_VERSION == 2
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdlib>
/*jaesungChoe*/
//#include "darknet/include/darknet.h"
/* https://github.com/opencv/opencv/blob/master/samples/dnn/yolo_object_detection.cpp */
/*jaesungChoe*/
//#include <opencv2/opencv.hpp>
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>

//#include <vector>
//#include <string>
#endif



#if CV_MINOR_VERSION == 3
cv::dnn::Net net;
float confidenceThreshold = 0.0;
std::vector<std::string> classNamesVec;
#endif

const size_t network_width = 416;
const size_t network_height = 416;
const char* about = "This sample uses You only look once (YOLO)-Detector "
                    "(https://arxiv.org/abs/1612.08242) "
                    "to detect objects on camera/video/image.\n"
                    "Models can be downloaded here: "
                    "https://pjreddie.com/darknet/yolo/\n"
                    "Default network is 416x416.\n"
                    "Class names can be downloaded here: "
                    "https://github.com/pjreddie/darknet/tree/master/data\n";
const char* params
    = "{ help           | false | print usage         }"
      "{ cfg            |  /home/jaesungchoe/catkin_ws/src/yolo/src/darknet/cfg/yolo.cfg     | model configuration }"
      "{ model          |  /home/jaesungchoe/catkin_ws/src/yolo/src/darknet/yolo.weights     | model weights       }"
      "{ camera_device  | 0     | camera device number}"
      "{ video          |  /home/jaesungchoe/catkin_ws/src/yolo/src/darknet/data/dog.jpg     | video or image for detection}"
      "{ min_confidence | 0.24  | min confidence      }"
      "{ class_names    |  /home/jaesungchoe/catkin_ws/src/yolo/src/darknet/data/coco.names     | class names         }";

using namespace std;

void JS_yolo(cv::Mat frame)
{

    cout << "into JS_yolo" << endl;

    #if CV_MINOR_VERSION == 3
        using namespace cv;
        using namespace cv::dnn;
        cout << "where are you fuck 03" << endl;


    //    Mat frame;
    //        cap >> frame; // get a new frame from camera/video or read image

        if (frame.empty())
        {
            waitKey();
    //        break;
            return;
        }

        if (frame.channels() == 4)
            cvtColor(frame, frame, COLOR_BGRA2BGR);

        //! [Resizing without keeping aspect ratio]
        Mat resized;
        resize(frame, resized, Size(network_width, network_height));
        //! [Resizing without keeping aspect ratio]

        //! [Prepare blob]
        Mat inputBlob = cv::dnn::blobFromImage(resized, 1 / 255.F); //Convert Mat to batch of images
        //! [Prepare blob]

        //! [Set input blob]
        net.setInput(inputBlob, "data");                   //set the network input
        //! [Set input blob]

        //! [Make forward pass]
        Mat detectionMat = net.forward("detection_out");   //compute output
       //! [Make forward pass]

       vector<double> layersTimings;
       double freq = getTickFrequency() / 1000;
       double time = net.getPerfProfile(layersTimings) / freq;
       ostringstream ss;
       ss << "FPS: " << 1000/time << " ; time: " << time << " ms";
       putText(frame, ss.str(), Point(20,20), 0, 0.5, Scalar(0,0,255));


        for (int i = 0; i < detectionMat.rows; i++)
        {
            const int probability_index = 5;
            const int probability_size = detectionMat.cols - probability_index;
            float *prob_array_ptr = &detectionMat.at<float>(i, probability_index);

            size_t objectClass = max_element(prob_array_ptr, prob_array_ptr + probability_size) - prob_array_ptr;
            float confidence = detectionMat.at<float>(i, (int)objectClass + probability_index);

            if (confidence > confidenceThreshold)
            {
                float x = detectionMat.at<float>(i, 0);
                float y = detectionMat.at<float>(i, 1);
                float width = detectionMat.at<float>(i, 2);
                float height = detectionMat.at<float>(i, 3);
                int xLeftBottom = static_cast<int>((x - width / 2) * frame.cols);
                int yLeftBottom = static_cast<int>((y - height / 2) * frame.rows);
                int xRightTop = static_cast<int>((x + width / 2) * frame.cols);
                int yRightTop = static_cast<int>((y + height / 2) * frame.rows);

                Rect object(xLeftBottom, yLeftBottom,
                            xRightTop - xLeftBottom,
                            yRightTop - yLeftBottom);

                rectangle(frame, object, Scalar(0, 255, 0));

                if (objectClass < classNamesVec.size())
                {
                    ss.str("");
                    ss << confidence;
                    String conf(ss.str());
                    String label = String(classNamesVec[objectClass]) + ": " + conf;
                    int baseLine = 0;
                    Size labelSize = getTextSize(label, FONT_HERSHEY_SIMPLEX, 0.5, 1, &baseLine);
                    rectangle(frame, Rect(Point(xLeftBottom, yLeftBottom - labelSize.height),
                                          Size(labelSize.width, labelSize.height + baseLine)),
                              Scalar(255, 255, 255), CV_FILLED);
                    putText(frame, label, Point(xLeftBottom, yLeftBottom),
                            FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0,0,0));
                }
                else
                {
                    cout << "Class: " << objectClass << endl;
                    cout << "Confidence: " << confidence << endl;
                    cout << " " << xLeftBottom
                         << " " << yLeftBottom
                         << " " << xRightTop
                         << " " << yRightTop << endl;
                }
            }
        }

        imshow("detections", frame);
        if (waitKey(1) >= 0) return;//break;
    #endif
}

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
    //printf("into the imageCallback");
    cout << "into the imageCallback" << endl;

    try
    {
        JS_yolo(cv_bridge::toCvShare(msg, "bgr8")->image);
//        cv::imshow("view", cv_bridge::toCvShare(msg, "bgr8")->image);
//        cv::waitKey(1);
    }catch(cv_bridge::Exception& e){
        ROS_ERROR("could not convert '%s' to 'bgr8'. ", msg->encoding.c_str());
    }
}

void initSubscriber(int argc, char **argv)
{
    cout << "into the initSubscriber" << endl ;

    ros::init(argc, argv, "yolo_subscribe_image");

    cout << "where are you fuck 01 ?" << endl;

    ros::NodeHandle nh;
    //cv::namedWindow("view");
    //cv::startWindowThread();
    cout << "where are you fuck 02 ?" << endl;
    image_transport::ImageTransport it(nh);
    image_transport::Subscriber sub = it.subscribe("camera/image_color", 1, imageCallback, ros::VoidPtr(), image_transport::TransportHints("compressed")); //
    cout << "before ros::spin()" << endl;
    ros::spin();
}


int main(int argc, char** argv)
{
    cout << "into the main()" << endl;
    #if CV_MINOR_VERSION == 3
        cout << "CV_MINOR_VERSION == 3" << endl;

        using namespace cv;
        using namespace cv::dnn;

        CommandLineParser parser(argc, argv, params);

        if (parser.get<bool>("help"))
        {
            cout << about << endl;
            parser.printMessage();
            return 0;
        }

        String modelConfiguration = parser.get<String>("cfg");
        String modelBinary = parser.get<String>("model");

        //! [Initialize network]
    //    dnn::Net net = dnn::readNetFromDarknet(modelConfiguration, modelBinary);
        net = dnn::readNetFromDarknet(modelConfiguration, modelBinary);
        //! [Initialize network]

        if (net.empty())
        {
            cerr << "Can't load network by using the following files: " << endl;
            cerr << "cfg-file:     " << modelConfiguration << endl;
            cerr << "weights-file: " << modelBinary << endl;
            cerr << "Models can be downloaded here:" << endl;
            cerr << "https://pjreddie.com/darknet/yolo/" << endl;
            exit(-1);
        }

        VideoCapture cap;
        if (parser.get<String>("video").empty())
        {
            int cameraDevice = parser.get<int>("camera_device");
            cap = VideoCapture(cameraDevice);
            if(!cap.isOpened())
            {
                cout << "Couldn't find camera: " << cameraDevice << endl;
                return -1;
            }
        }
        else
        {
            cap.open(parser.get<String>("video"));
            if(!cap.isOpened())
            {
                cout << "Couldn't open image or video: " << parser.get<String>("video") << endl;
                return -1;
            }
        }

//        vector<string> classNamesVec;
        ifstream classNamesFile(parser.get<String>("class_names").c_str());
        if (classNamesFile.is_open())
        {
            string className = "";
            while (classNamesFile >> className)
                classNamesVec.push_back(className);
        }

        //float confidenceThreshold = parser.get<float>("min_confidence");
        confidenceThreshold = parser.get<float>("min_confidence");
    #endif

    //jaesungchoe
    #if CV_MINOR_VERSION == 3
        printf("fuck 3.3 : %d.%d.%d \n",CV_MAJOR_VERSION, CV_MINOR_VERSION, CV_SUBMINOR_VERSION);
    #endif

    #if CV_MINOR_VERSION == 2
        printf("fuck 3.2 : %d.%d.%d \n",CV_MAJOR_VERSION, CV_MINOR_VERSION, CV_SUBMINOR_VERSION);
    #endif
    cout << "where are you : before initSubscriber()" << endl;
    initSubscriber(argc, argv);
    cout << "where are you" << endl;

    return 0;
} // main
//#endif