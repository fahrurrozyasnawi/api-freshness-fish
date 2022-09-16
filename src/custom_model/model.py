import os
import tensorflow as tf
import numpy as np

def loadModel(model):
  base_dir = os.getcwd()
  path = os.path.join(base_dir, 'src\custom_model\models')
  file = os.path.join(path, model)

  return tf.keras.models.load_model(file)

def predict_fish(img, model):
  file = tf.keras.preprocessing.image.load_img(img, target_size=(160,160))
  x = tf.keras.preprocessing.image.img_to_array(file)
  x = np.expand_dims(x)
  x = np.vstack([x])

  return model.predict(x)

def predict_freshness(img, model):
  file = tf.keras.preprocessing.image.load_img(img, target_size=(160,160))
  x = tf.keras.preprocessing.image.img_to_array(file)
  x = np.expand_dims(x)
  predictions = model.predict(x)
  predictions = tf.where(predictions < 0.5, 0, 1)

  return predictions
