import cv2
import numpy as np
import os
from PIL import Image

class BaseImage:

    def __init__(self):
        self.base_path = 'orl_faces/'
        self.image_paths = []
        self.images = []
        self.load()

    def load(self):
        for directory in os.listdir(self.base_path):
            if directory[len(directory) - 1] != 'E':
                for image_name in os.listdir(self.base_path + '/' + directory):
                    image_path= self.base_path + '/' + directory + '/' + image_name
                    self.image_paths.append(image_path)            # add the image paths
                    image = Image.open(image_path).convert('L')
                    image = np.array(image, 'uint8')
                    self.images.append(image)#cv2.imread(image_path , 0)) # load images in grayscale

    def mean_image(self):
        mean = np.zeros(self.images[0].shape, dtype=np.uint32) # due to integer summations uint32
        for image in self.images:
            mean = mean + image
        mean /= len(self.images)
        mean = np.array(mean,dtype=np.uint8) # converting back to uin8
        return mean



loader = BaseImage()
loader.mean_image()
