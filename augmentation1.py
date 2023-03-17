

import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import cv2
import imutils
import matplotlib.pyplot as plt
import os,sys
from os import listdir
import time   

def augment_data(path,n_generated_samples,save_to_dir):
    data_gen = ImageDataGenerator(rotation_range=10, 
                                  width_shift_range=0.1, 
                                  height_shift_range=0.1, 
                                  shear_range=0.1, 
                                  horizontal_flip=True, 
                                  vertical_flip=True, 
                                  fill_mode='nearest')                       
    dirs=os.listdir(path)
    for filename in dirs:
        image = cv2.imread(os.path.join(path,filename))
        # reshape the image
        image = image.reshape((1,)+image.shape)
        # prefix of the names for the generated sampels.
        save_prefix = 'aug_' + filename[:-4]
        i=0
        for batch in data_gen.flow(x=image, batch_size=1, save_to_dir=save_to_dir, 
                                           save_prefix=save_prefix, save_format='jpg'):
            i += 1
            if i > n_generated_samples:
                break



augment_data(path="10_per_adul", n_generated_samples=4, save_to_dir="10_per_adul_aug")
#augment_data(path="15_per_adul", n_generated_samples=4, save_to_dir="15_per_adul_aug")
#augment_data(path="20_per_adul", n_generated_samples=4, save_to_dir="20_per_adul_aug")
#augment_data(path="25_per_adul", n_generated_samples=4, save_to_dir="25_per_adul_aug")
#augment_data(path="30_per_adul", n_generated_samples=4, save_to_dir="30_per_adul_aug")
#augment_data(path="pure", n_generated_samples=4, save_to_dir="pure_aug")



def data_summary():
    

    # number of files (images) that are in the the folder named 'yes' that represent tumorous (positive) examples
    m_10_per = len(listdir("10_per_adul"))
   # m_15_per = len(listdir("15_per_adul"))
  #  m_20_per = len(listdir("20_per_adul"))
  #  m_25_per = len(listdir("25_per_adul"))
  #  m_30_per = len(listdir("30_per_adul"))
  #  m_pure = len(listdir("pure"))
    
    
    m_10_per_aug = len(listdir("10_per_adul_aug"))
  #  m_15_per_aug = len(listdir("15_per_adul_aug"))
  #  m_20_per_aug = len(listdir("20_per_adul_aug"))
   # m_25_per_aug = len(listdir("25_per_adul_aug"))
   # m_30_per_aug = len(listdir("30_per_adul_aug"))
  #  m_pure_aug = len(listdir("pure_aug"))
    
    # number of all examples
    
    
    print ("num of 10 per before ", m_10_per)
  #  print ("num of 15 per before ", m_15_per)
  #  print ("num of 20 per before ", m_20_per)
  #  print ("num of 25 per before ", m_25_per)
  #  print ("num of 30 per before ", m_30_per)
  #  print ("num of pure before ", m_pure)
    
    print ("num of 10 per after ", m_10_per_aug)
  #  print ("num of 15 per after ", m_15_per_aug)
  #  print ("num of 20 per after ", m_20_per_aug)
  #  print ("num of 25 per after ", m_25_per_aug)
  #  print ("num of 30 per after ", m_30_per_aug)
  #  print ("num of pure after ", m_pure_aug)
    
    
    
    

data_summary()