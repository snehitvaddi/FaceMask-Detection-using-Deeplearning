# Face-Detection-using-OpenCV
Using OpenCV's inbuilt model for Face Detection.

### Description
OpenCV provides a very accurate inbuilt face detection model. In this project, I've used that model and created my own face detection project.
1. The script to detect faces (**face_detector.py**) from images is inside the **image** folder. The image must also be placed inside this folder with the name **image.png**
2. The script to detect faces (**face_detector.py**) in video is inside the **video** folder
3. The information about the model is present inside **model_data** folder
4. **Pipfile**, **Pipfile.lock** and **requirements.txt** are useful for setting up the environment.
5. **Readme.md** includes project's documentation

## Setup
You can setup using either of the two methods below.

### Setup (Pipenv Virtual Environment)
1. Clone the project to your local system
2. Navigate inside the project directory on your local system inside the terminal
3. Install all dependencies using `pipenv install --ignore-pipfile`
4. Start environment with `pipenv shell`

### Setup (pip3)
1. Clone the project to your local system
2. Navigate inside the project directory on your local system inside the terminal
3. Install all dependencies using `pip3 install -r requirements.txt`

## Detection

### Detecting faces in Image
1. Place the image in the folder **image** with the name `image.png`
2. Run the **face_detector.py** inside **image** folder using `python image/face_detector.py`

### Detecting faces in Video
1. Run the **face_detector.py** inside **video** folder using `python video/face_detector.py`
