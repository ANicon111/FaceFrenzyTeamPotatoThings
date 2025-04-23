Face recognition - This system uses the Python library "face_recognition" to count the amount of the faces in the picture taken before using the camera on the PYNQ-Z.

IO Handler - This module takes care of the buttons and LED functionality, meaning whenever the players show the correct amount of faces in the picture the LED will lit up green and on the contrary it will lit red, meaning that the players used one of their three strikes. 

Game Management System - This module takes care of the scoring system. Players will gain a point whenever they show correct amount of the faces in the picture, however they will lose one of the three strikes whenever the amount of faces in the picture will not indicate the same amount as was shown before. 

User Interface - The users will be given a display element with the PYNQ board where they can see the results and the score.

HTTP Server - The admin can view the gameplay, where they can see the process of the game. They can see current score and the results of the face recognition module. 

https://github.com/suniljs6/Counting-number-of-faces-in-a-picture-using-python-opencv
![Reason why we chose OpenCV](opencv.png "Reason why we chose OpenCV")
