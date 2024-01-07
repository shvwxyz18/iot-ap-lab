import cv2
cam = cv2.VideoCapture(0) 
result, image = cam.read() 
if result: 
	cv2.imshow("test", image) 
	cv2.imwrite("test.png", image) 
	cv2.waitKey(0) 
	cv2.destroyWindow("test") 
else: 
	print("No image detected. Please! try again") 

#you can run this even on your system, no need of RaspberryPi
