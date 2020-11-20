# SkittlesIP
Image processing program that detects skittles and their individual colors in .jpg photos on a variety of backgrounds.

Required Libraries: OpenCV, NumPy
Verified & Tested in: Python 3.7 - 3.8.1
Last tested: 11/19/2020

Image/Machine Requirements:
(Semi)solid background that does not blend in with the skittles
Skittles must be whole to be detected
Skittles must not be vertical
Image should have minimal glare
Image should be top down view
Machine must have Python 3.7 installed
Machine must have OpenCV libraries installed
Machine must have NumPy libraries installed

Technical Performance Measures:
Must run in under 60 seconds for a 1500x1125 image (Originals included with release are 
Must be at least 50% accurate in detecting skittle objects with no more than 10 false positives.
Must be at least 50% accurate in determining skittle color with no more than 2 false positives.

Initial assessment results:
Avg Circle Detection Time: 0.0573 Seconds
Avg Color Detection time: 1.4375 Seconds 
Average Total running time (Original Image): 15.456 Seconds

Object Detection Accuracy: 100%
Object Color Detection Accuracy: 100%
8% CPU Usage  *Processor AMD Ryzen 7 1800X @ 3.60 GHz
32% CPU Usage *Processor Intel(R) Core(™) i5-8250U @ 1.60 GHz
75 MB RAM Usage *Uniform across both machines

Tutorials Used:
“Hough Circle Transform.” OpenCV Open Source Computer Vision, docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html.
“Detection of a Specific Color(Blue Here) Using OpenCV with Python?” Tutorialspoint, 9 Apr. 2019, www.tutorialspoint.com/detection-of-a-specific-color-blue-here-using-opencv-with-python
