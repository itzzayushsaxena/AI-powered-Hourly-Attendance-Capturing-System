# class threading.Thread(target=None)
# This constructor should always be called with keyword arguments. Arguments are:
# target is the callable object to be invoked by the run() method. Defaults to None, meaning nothing is called.

# start()
# Start the thread’s activity.
# It must be called at most once per thread object. It arranges for the object’s run() method to be invoked 
# in a separate thread of control.
# This method will raise a RuntimeError if called more than once on the same thread object.


# cv.face.LBPHFaceRecognizer_create(int radius = 1,int neighbors = 8,int 	grid_x = 8,int grid_y = 8,
# double threshold = DBL_MAX )

# radius	The radius used for building the Circular Local Binary Pattern. 
#           The greater the radius, the smoother the image but more spatial information you can get.
# neighbors	The number of sample points to build a Circular Local Binary Pattern from. 
#           An appropriate value is to use 8 sample points. Keep in mind: the more sample points you include, 
#           the higher the computational cost.
# grid_x	The number of cells in the horizontal direction, 8 is a common value used in publications. 
#           The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector.
# grid_y	The number of cells in the vertical direction, 8 is a common value used in publications. 
#           The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector.
# threshold	The threshold applied in the prediction. If the distance to the nearest neighbor is larger than 
#           the threshold, this method returns -1.

import os
import cv2
import numpy as np
from PIL import Image
from threading import Thread



# -------------- image labesl ------------------------
def getImagesAndLabels(path):


    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # print(imagePaths)

    # create empty face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # print(pilImage)
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage)
        # getting the Id from the image
        Id = int(os.path.split(imagePath)[1].split("_")[1])
        # print(os.path.split(imagePath)[1].split("_")[1])

        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


# ----------- train images function ---------------
def train_model():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    faces, Ids = getImagesAndLabels("captured_images")
    Thread(target = recognizer.train(faces, np.array(Ids))).start()
    recognizer.save("TrainingImageLabel"+os.sep+"Trainner.yml")
    # print("TrainingImageLabel"+os.sep+"Trainner.yml")
    return True
