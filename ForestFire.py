import keras 
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import matplotlib.pyplot as plt
from glob import glob
import pandas as pd

train_path = ".../Yangın"
test_path = ".../Normal"

img = load_img(".../Yangın/1.jpg")
plt.imshow(img)
plt.axis("off")
plt.show()

x = img_to_array(img)
print(x.shape)

className = glob(train_path + '/*')
numberOfClass = len(className)
print("NumberOfClass: ", numberOfClass)
