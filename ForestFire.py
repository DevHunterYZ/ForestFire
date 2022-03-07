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

#%% CNN Model
model = Sequential()
model.add(Conv2D(32,(3,3),input_shape = x.shape))
model.add(Activation("relu"))
model.add(MaxPooling2D())

model.add(Flatten())
model.add(Dense(16))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(numberOfClass))
model.add(Activation("softmax"))

model.compile(loss = "categorical_crossentropy",
              optimizer = "rmsprop",
              metrics = ["accuracy"])
batch_size = 32

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.3,
                                   horizontal_flip = True,
                                   zoom_range = 0.3)

test_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = train_datagen.flow_from_directory(
    train_path,
    target_size=x.shape[:2],
    batch_size = batch_size,
    color_mode = "rgb",
    class_mode = "categorical")             
        

test_generator = test_datagen.flow_from_directory(
    test_path,
    target_size = x.shape[:2],
    batch_size = batch_size,
    color_mode = "rgb",
    class_mode = "categorical")
                  
model.fit_generator(
    generator = train_generator,
    steps_per_epoch = 32//batch_size,
    epochs = 8,
    validation_data = test_generator,
    validation_steps = 8 // batch_size)
