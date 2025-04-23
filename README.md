# Face Recognition Game on PYNQ-Z

This project implements a face recognition game using the **PYNQ-Z** board. Players compete by presenting a specific number of faces in front of a camera. The system counts the number of faces in the captured photo using computer vision, provides feedback, tracks scores, and allows interaction through buttons, LEDs, and a web interface.

---

## 🔍 Overview

This interactive game encourages participation by detecting the number of faces in a photo and providing immediate feedback via LEDs and a user interface. The system uses the **`face_recognition`** Python library and **OpenCV** to perform facial detection, and runs on a resource-constrained embedded system (PYNQ-Z).

---

## 🎮 User Stories & Testable Scenarios

### ✅ As a user I want the game to start when I press the button on the board so that I can play the game

- **Given** the system is powered on and idle  
- **When** the "Start" button is pressed  
- **Then** the game begins, the timer starts, and feedback is given via LEDs or the UI

### 🧑‍🤝‍🧑 As a user I want the game to recognize all faces in the photo so that the game is fair

- **Given** a photo is taken  
- **When** N human faces are visible  
- **Then** all N faces are accurately counted and logged/displayed

### 💡 As a user I want the game to give me a visible feedback through LED's on the board or user interface so that I know that the timer has started 
- **Given** the game starts  
- **When** the timer begins  
- **Then** the LED or UI updates to show the game is active

### ⏸ As a user I want the game to have a pause option so that I can pause the game if anyone gets injured or goes to the bathroom
- **Given** the game is running  
- **When** the "Pause" button is pressed  
- **Then** the game pauses and visual feedback is given

### 🔢 As a user I want to input the number of max face count via buttons so that the game knows how many persons will be maximum in the picture
- **Given** the game is in setup mode  
- **When** the "+" or "–" buttons are used  
- **Then** the max face count is updated and used for game validation

### 🏆 As a user I want to see the score so that I know how bad I am at the game
- **Given** a round is completed  
- **When** scoring is calculated  
- **Then** the score is displayed until reset or next round

### 📸 As a user I want to be able to save the after photo so that I can keep the good memories 
- **Given** a round has ended  
- **When** the photo is taken  
- **Then** the image is saved locally or to the cloud for future access

---

## 🧩 Module Descriptions

### 🎭 Face Recognition
Uses the `face_recognition` Python library to count the number of visible human faces in a captured photo.

### 🧠 Game Management System
Handles score logic. Players gain a point for correct face count and lose one of three strikes for an incorrect count.

### 🧰 IO Handler
Manages hardware input and output:
- **Buttons** for starting/pausing the game or setting face count
- **LEDs** to show success (green) or failure (red)

### 💻 User Interface
Displays score and game state directly on the PYNQ board screen.

### 🌐 HTTP Server
Provides real-time remote monitoring for admins:
- View current score and face recognition results
- Observe live game state

---

## ⚠️ Constraints, Risks & Assumptions

### 🚧 Constraints
- Limited hardware resources of the PYNQ-Z board
- Performance optimization is essential

### ⚠️ Risks
- **USB Camera Reliability**: Affects image capture accuracy and timing
- **Team Motivation**: Impacts development pace
- **Web Server Load**: Might bottleneck real-time monitoring

### ✅ Assumptions
- Compatibility with OpenCV and other libraries
- Fully functional and reliable PYNQ board and peripherals

---

## 🔍 Why OpenCV?

![Reason why we chose OpenCV](opencv.png "Reason why we chose OpenCV")

We selected OpenCV due to its robust performance, broad community support, and seamless integration with the `face_recognition` library on embedded systems like PYNQ-Z.

---

## 📚 References

- [`face_recognition` Python Library](https://github.com/ageitgey/face_recognition)
- [OpenCV GitHub Repository](https://github.com/opencv/opencv)
- [Example Face Detection Project](https://github.com/suniljs6/Counting-number-of-faces-in-a-picture-using-python-opencv)

---

## 🛠️ Built With

- Python
- OpenCV
- face_recognition
- PYNQ Framework
- HTML/CSS (for Web UI)
