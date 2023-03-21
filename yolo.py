import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
import glob

# Display
from IPython.display import Image, display
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def printimage(filename, path):
    model_builder = keras.applications.xception.Xception
    img_size = (99, 99)
    preprocess_input = keras.applications.xception.preprocess_input
    decode_predictions = keras.applications.xception.decode_predictions

    last_conv_layer_name = "block14_sepconv2_act"

    # The local path to our target image
    img_path = keras.utils.get_file(filename, path)
    display(Image(img_path))


def yoloF():
    print(" yolo function")
    # Opening JSON file
    f = open('listclasses.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    listofdir = glob.glob('./Images/*')
    for dirname in listofdir:
        print(dirname)
        for i in data['breeds']:
            if i in dirname.lower() :
                print(i)
    
        
        #printimage(i, path)


  
