Module Descriptions:

Face recognition - This system uses the Python library "face_recognition" to count the amount of the faces in the picture taken before using the camera on the PYNQ-Z.

IO Handler - This module takes care of the buttons and LED functionality, meaning whenever the players show the correct amount of faces in the picture the LED will lit up green and on the contrary it will lit red, meaning that the players used one of their three strikes. 

Game Management System - This module takes care of the scoring system. Players will gain a point whenever they show correct amount of the faces in the picture, however they will lose one of the three strikes whenever the amount of faces in the picture will not indicate the same amount as was shown before. 

User Interface - The users will be given a display element with the PYNQ board where they can see the results and the score.

HTTP Server - The admin can view the gameplay, where they can see the process of the game. They can see current score and the results of the face recognition module. 

User Stories:

As a user I want the game to start when I press the button on the board 
so that I can play the game

As a user I want the game to recognize all faces in the photo 
so that the game is fair

As a user I want the game to give me a visible feedback through LED's on the board or user interface 
so that I know that the timer has started 

As a user I want the game to have a pause option 
so that I can pause the game if anyone gets injured or goes to the bathroom

As a user I want to input the number of max face count via buttons 
so that the game knows how many persons will be maximum in the picture

As a user I want to see the score 
so that I know how bad I am at the game

As a user I want to be able to save the after photo 
so that I can keep the good memories 

Constraints, Risks and Assumptions:

The main constraints of this project will be from the hardware sphere. The limited resources of the PYNQ board can be an issue, so working on the optimization of the system will be critical, with performance being given a high priority.


Risks:
- USB Camera -> Its reliability and performance will directly impact the performance of the system
- Team’s motivation -> Poor motivation will affect the team’s productivity and teamwork, slowing down the development of the project.
- Web Server Performance -> A poor web server performance will affect the monitoring of the system by the admins


Assumptions:
- Library Compatibility -> The team assumes that the libraries used for the system like OpenCV will be compatible with the PYNQ board.
- Reliability of the hardware -> The team assumes that the PYNQ board and I/O devices are fully functional and reliable.


https://github.com/suniljs6/Counting-number-of-faces-in-a-picture-using-python-opencv
![Reason why we chose OpenCV](opencv.png "Reason why we chose OpenCV")
