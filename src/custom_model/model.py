import os
import tensorflow as tf
import numpy as np
from PIL import Image

def loadModel(model):
  base_dir = os.getcwd()
  path = os.path.join(base_dir, 'src\custom_model\models')
  file = os.path.join(path, model)

  return tf.keras.models.load_model(file)

def predict_fish(img, model):
  img = Image.open(img)
  # file = tf.keras.utils.load_img(img, target_size=(160,160))
  file = img.resize((160,160), resample=0)
  # x = tf.keras.preprocessing.image.img_to_array(file)
  x = np.array(file)
  x = np.expand_dims(x, axis=0)
  x = np.vstack([x])

  return model.predict(x)

def predict_freshness(img, model):
  img = Image.open(img)
  # file = tf.keras.utils.load_img(img, target_size=(160,160))
  # x = tf.keras.preprocessing.image.img_to_array(file)
  # x = np.expand_dims(x)
  file = img.resize((160,160), resample=0)
  x = np.array(file)
  x = np.expand_dims(x, axis=0)
  predictions = model.predict(x)
  predictions = tf.where(predictions < 0.5, 0, 1)

  return predictions
