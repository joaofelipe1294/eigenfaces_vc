import cv2
import numpy as np
import os
from PIL import Image

class BaseImage(object):

    def __init__(self , base_path = 'orl_faces/'):
        self.base_path = base_path
        self.images = []
        #self.classes = []
        self.load()
        cols = self.images[0].shape[0] * self.images[0].shape[1]
        self.A_matrix = np.empty(shape=[cols , 0]) #defines an empty array , it will be appended to the proper values
        self.define_A_matrix()

    def load(self):
        #raise NotImplementedError("Please Implement this method !!!")
         for directory in os.listdir(self.base_path):
            if directory[len(directory) - 1] != 'E':
                for image_name in os.listdir(self.base_path + '/' + directory):
                    image_path= self.base_path + '/' + directory + '/' + image_name
                    image = Image.open(image_path).convert('L')
                    image = np.array(image, 'uint8')
                    self.images.append(image)

    def mean_image(self):
        '''calculates the mean image of the base'''
        mean = np.zeros(self.images[0].shape, dtype=np.uint32) # due to integer summations uint32
        for image in self.images:
            mean = mean + image
        mean /= len(self.images)
        mean = np.array(mean,dtype=np.uint8) # converting back to uin8
        return mean

    def define_A_matrix(self):
        cols = self.A_matrix.shape[0]
        print(cols)
        for image in self.images:
            image = image.reshape(cols , 1)
            self.A_matrix = np.append(self.A_matrix , image , 1)



base = BaseImage()
print(base.A_matrix)
print('---------------------------------')
'''for image in base.images:
    image = image.reshape(cols , 1)
    A = np.append(A , image , 1)
print(A)'''
print(base.images[0])
print('---------------------------------')
print(base.images[1])
