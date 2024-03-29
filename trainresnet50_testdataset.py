import matplotlib.pyplot as plotter_lib
import numpy as np
import PIL as image_lib
import tensorflow as tflow
from tensorflow.keras.layers import Flatten
from keras.layers.core import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

print ("Import dataset...")
import pathlib
demo_dataset = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
directory = tflow.keras.utils.get_file('flower_photos', origin=demo_dataset, untar=True)
data_directory = pathlib.Path(directory)

print ("Splitting data into two parts...")
img_height,img_width=180,180
batch_size=32
train_ds = tflow.keras.preprocessing.image_dataset_from_directory(
  data_directory,
  validation_split=0.2,
  subset="training",
  seed=123,
label_mode='categorical',
  image_size=(img_height, img_width),
  batch_size=batch_size)

print ("Creating validation subset...")
validation_ds = tflow.keras.preprocessing.image_dataset_from_directory(
  data_directory,
  validation_split=0.2,
  subset="validation",
  seed=123,
label_mode='categorical',
  image_size=(img_height, img_width),
  batch_size=batch_size)

print ("Visualizing six random images from dataset...")
import matplotlib.pyplot as plotter_lib
plotter_lib.figure(figsize=(10, 10))
epochs=10
for images, labels in train_ds.take(1):
  for var in range(6):
    ax = plt.subplot(3, 3, var + 1)
    plotter_lib.imshow(images[var].numpy().astype("uint8"))
    plotter_lib.axis("off")

print ("Importing ResNet-50 model...")
demo_resnet_model = Sequential()
pretrained_model_for_demo= tflow.keras.applications.ResNet50(include_top=False,
                   input_shape=(180,180,3),
                   pooling='avg',classes=5,
                   weights='imagenet')
for each_layer in pretrained_model_for_demo.layers:
        each_layer.trainable=False
demo_resnet_model.add(pretrained_model_for_demo)
demo_resnet_model.add(Flatten())
demo_resnet_model.add(Dense(512, activation='relu'))
demo_resnet_model.add(Dense(5, activation='softmax'))

print ("Training the ResNet-50 model...")
demo_resnet_model.compile(optimizer=Adam(lr=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
history = demo_resnet_model.fit(train_ds, validation_data=validation_ds, epochs=epochs)

print ("Evaluating the model and visualizing  model’s training and accuracy ...")
plotter_lib.figure(figsize=(8, 8))
epochs_range= range(epochs)
plotter_lib.plot( epochs_range, history.history['accuracy'], label="Training Accuracy")
plotter_lib.plot(epochs_range, history.history['val_accuracy'], label="Validation Accuracy")
plotter_lib.axis(ymin=0.4,ymax=1)
plotter_lib.grid()
plotter_lib.title('Model Accuracy')
plotter_lib.ylabel('Accuracy')
plotter_lib.xlabel('Epochs')
plotter_lib.legend(['train', 'validation'])

print ("Saving...")
plotter_lib.savefig('output-plot.png')

print ("Done.")