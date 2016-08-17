from base_image import *

class ORL(BaseImage):

    def __init__(self , base_path):
        super(ORL , self).__init__(base_path)
        self.load()

    def load(self):
        for directory in os.listdir(self.base_path):
            if directory[len(directory) - 1] != 'E':
                for image_name in os.listdir(self.base_path + '/' + directory):
                    image_path= self.base_path + '/' + directory + '/' + image_name
                    image = Image.open(image_path).convert('L') #read image
                    image = np.array(image, 'uint8')            # convert into a numpy array
                    self.images.append(image)

orl = ORL('orl_faces/')
#orl.load()
