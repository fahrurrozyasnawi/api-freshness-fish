import os
import tensorflow as tf
import numpy as np

# class_names = [
#     'IKAN BANDENG', 
#     'IKAN BANJAR', 
#     'IKAN BARONANG BATIK', 
#     'IKAN BAWAL', 
#     'IKAN BETE BETE', 
#     'IKAN CAKALANG', 
#     'IKAN KAKAP MERAH', 
#     'IKAN LAYANG', 
#     'IKAN TEMBANG', 
#     'IKAN TENGGIRI', 
#     'IKAN TERI', 
#     'IKAN TUNA']

def loadModel(model):
  base_dir = os.getcwd()
  path = os.path.join(base_dir, 'src\custom_model\models')
  file = os.path.join(path, model)

  return tf.keras.models.load_model(file)

def predict(img, model):
  file = tf.keras.preprocessing.image.load_img(img, target_size=(160,160))
  x = tf.keras.preprocessing.image.img_to_array(file)
  x = np.expand_dims(x)

  return model.predict(x)
