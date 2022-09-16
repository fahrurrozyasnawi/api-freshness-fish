from custom_model.model import loadModel, predict_fish, predict_freshness
from flask_restful import Resource
from flask import Response, request, flash
import tensorflow as tf
import numpy as np

class_names = [
    'IKAN BANDENG', 
    'IKAN BANJAR', 
    'IKAN BARONANG BATIK', 
    'IKAN BAWAL', 
    'IKAN BETE BETE', 
    'IKAN CAKALANG', 
    'IKAN KAKAP MERAH', 
    'IKAN LAYANG', 
    'IKAN TEMBANG', 
    'IKAN TENGGIRI', 
    'IKAN TERI', 
    'IKAN TUNA']

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
model_1 = loadModel('fish_classify_afterfinetune_2_4.h5')
model_2 = loadModel('my_model_afterfinetune_2_1.h5')


def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class ClassifyFish(Resource):
  def post(self):
    if 'file' not in request.files:
      flash('No Image selected')
      return 'No Image File', 200

    img = request.files['file']
    if img.filename == '':
      flash('No item selected')
      return 'No image File', 200

    if img and allowed_file(img.filename):
      result = predict_fish(img, model_1)
      maxindex = int(np.argmax(result))
      return class_names[maxindex], 200

class FreshnessClassify(Resource):
  def post(self):
    if 'file' not in request.files:
      flash('No Image selected')
      return 'No Image File', 200

    img = request.files['file']
    if img.filename == '':
      flash('No item selected')
      return 'No image File', 200

    if img and allowed_file(img.filename):
      result = predict_freshness(img, model_2)
      return 'Segar' if result == 0 else 'Tidak Segar', 200
      
