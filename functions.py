import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def preprocess_img(image, img_shape=224):
    image = tf.image.resize(image, [img_shape, img_shape])
    return tf.cast(image, tf.float32)

def pred_and_plot(filename, model):
  """
  Imports an image located at filename, makes a prediction on it with
  a trained model and plots the image with the predicted class as the title.
  """
  img_clear = mpimg.imread("/content/" + filename)
  img = preprocess_img(img_clear)

  # Make a prediction
  pred = tf.round(model.predict(tf.expand_dims(img, axis=0)))
  # Plot the image and predicted class
  plt.imshow(img_clear)
  plt.title(f"Prediction: {pred}")
  plt.axis(False)