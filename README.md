## FaceMask-Detection-using-Deeplearning
Classification model to classify people with and without masks.
A pilot project of Face mask detection. During the times of COVID-19, covering our face with a mask and maintaining social distancing is essential.  
With advancements in the field of Deep Learning, now we can easily train a model and check if someone is earning a mask or not.

## Dataset: 
Data set can be downloaded from https://github.com/prajnasb/face_detector/tree/master/dataset

## Output:

<a href="https://youtu.be/yketl5zUZEw"><img src="https://github.com/snehitvaddi/FaceMask-Detection-using-Deeplearning/blob/master/outputs/Capture.PNG" width="700" height="350"></a>

## Setup
You can setup using either of the two methods below.

### Method 1: Setup (Pipenv Virtual Environment)
1. Clone the project to your local system
2. Navigate inside the project directory on your local system inside the terminal
3. Install all dependencies using `pipenv install --ignore-pipfile`
4. Start environment with `pipenv shell`

### Method 2: Setup (pip)
1. Clone the project to your local system
2. Navigate inside the project directory on your local system inside the terminal
3. Install all dependencies using `pip install -r requirements.txt`

## Detection

### Detecting faces with maks in video
1. Navigate to jupyter-notebook `./FaceMask Detection using Deep Learning.ipynb` 
2. Run import libraries cell and load model cell.
3. For getting real-time results, run predicition and casscade classifier cell
