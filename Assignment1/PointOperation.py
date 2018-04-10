import cv2
import numpy as np
from matplotlib import pyplot as plt 

def Hist_Equalization(imginput,imgoutput):
    image = cv2.imread(imginput,0)
    plt.hist(image.flatten(),256,[0,256])
    plt.show()
    equalize = cv2.equalizeHist(image)
    plt.hist(equalize.flatten(),256,[0,256])
    cv2.imwrite(imgoutput,equalize)
    plt.show()

if __name__ == '__main__':
    Hist_Equalization('images/SEM256_256.pgm','images/Seed.pgm')
    Hist_Equalization('images/Cameraman.pgm','images/CameraBoy.pgm')