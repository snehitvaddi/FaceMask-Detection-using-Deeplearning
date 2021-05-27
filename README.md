### 😷 FaceMask-Detection-using-Deeplearning
A CNN based Image Classification model to classify people with and without masks.
A pilot project of Face mask detection. During the times of COVID-19, covering our face with a mask and maintaining social distancing is essential.  
With advancements in the field of Deep Learning, now we can easily train a model and check if someone is earning a mask or not.

|🗃 Dataset| 📰 HaarCascade |
|:-:|:-:|
| [Link](https://github.com/prajnasb/face_detector/tree/master/dataset)| [File](https://github.com/snehitvaddi/FaceMask-Detection-using-Deeplearning/blob/master/haarcascade_frontalface_default.xml)|

### 📢 Favour:
It would be highly motivating, if you can <b>STAR</b>⭐ this repo if you find it helpful.😅

### 🎉 Output:

<a href="https://youtu.be/yketl5zUZEw"><img src="https://github.com/snehitvaddi/FaceMask-Detection-using-Deeplearning/blob/master/outputs/Capture.PNG" width="700" height="350"></a>
### 🏃‍♂️ How to Run

#### Detecting faces with maks in video
1. Navigate to jupyter-notebook `./FaceMask Detection using Deep Learning.ipynb` <br>
**I made this file private to avoid misuse, contact me @v.snehith999@gmail.com for the file.**
2. Run import libraries cell and load model cell.
3. For getting real-time results, run predicition and casscade classifier cell

### 🧠 How it works!!
* Read input either as single image or video from webcam using OpenCV.
* Detect location of faces in given frame using Face_Frontal_Default Cascade Classifier.[Download](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
* Save the list of face portions for further steps.
* Load the Custom-trained CNN model, iterate each face through the model to predict mask on face.
* Post-process the frame ie; Tagging Face, with respective predictions.
--------
### 🔧Setup
You can setup this project using either of the methods mentioned below.

#### 👉 Method 1: Setup (Pipenv Virtual Environment)
1. Clone the project to your local system
2. Navigate inside the project directory on your local system inside the terminal
3. Install all dependencies using `pipenv install --ignore-pipfile`
4. Start environment with `pipenv shell`

#### 👉 Method 2: Setup (pip)
1. Clone the project to your local system
2. Navigate inside the project directory on your local system inside the terminal
3. Install all dependencies using `pip install -r requirements.txt`
--------

**👁‍ Creator Disclaimer**
Since the dataset used here is Open-Sourced, this code should only be used for research/academic/personal purposes only. The models were trained on the <a href="https://github.com/prajnasb/observations/tree/master/experiements/data">prajnasb's Open Source dataset</a>, any form of commercial use is strictly prohibhited. Please contact me for all further queries.😉

