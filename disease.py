import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array
import keras
from tensorflow.keras.utils import load_img
#from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg19 import VGG19,preprocess_input,decode_predictions
import numpy as np

model =load_model('C:\\Users\\Dell\\Desktop\\maj\\model (1).h5',compile=False)

#model1=load_model('pest_model.h5')


#result=model.predict(path)

#print(result)


d={0: 'Apple_scab', 1: 'Black_rot', 2: 'Cedar_apple_rust', 3: 'healthy', 4: 'healthy', 5: 'Powdery_mildew', 6: 'healthy', 7: 'Cercospora_leaf_spot Gray_leaf_spot', 8: 'Common_rust_', 9: 'Northern_Leaf_Blight', 10: 'healthy', 11: 'Black_rot', 12: 'Esca_(Black_Measles)', 13: 'Leaf_blight_(Isariopsis_Leaf_Spot)', 14: 'healthy', 15: 'Haunglongbing_(Citrus_greening)', 16: 'Bacterial_spot', 17: 'healthy', 18: 'Bacterial_spot', 19: 'healthy', 20: 'Early_blight', 21: 'Late_blight', 22: 'healthy', 23: 'healthy', 24: 'healthy', 25: 'Powdery_mildew', 26: 'Leaf_scorch', 27: 'healthy', 28: 'Bacterial_spot', 29: 'Early_blight', 30: 'Late_blight', 31: 'Leaf_Mold', 32: 'Septoria_leaf_spot', 33: 'Spider_mites Two-spotted_spider_mite', 34: 'Target_Spot', 35: 'Tomato_Yellow_Leaf_Curl_Virus', 36: 'Tomato_mosaic_virus', 37: 'healthy'}


def prediction(path):
  img=load_img(path,target_size=(256,256))
  i=img_to_array(img)
  im=preprocess_input(i)
  img=np.expand_dims(im,axis=0)
  pred=np.argmax(model.predict(img))
  return (d[pred])
