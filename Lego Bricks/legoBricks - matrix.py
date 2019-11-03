import timeit
code_to_test = """
import cv2
import numpy as np

image=cv2.imread('opencv1 image 2.jpg',1)
#cv2.imshow('window1',image)
#cv2.waitKey(0)
imgmat = np.array(image)
#imgmat = imgmat[100:110,55:65,:]

imgfin = np.zeros(imgmat.shape)
imgfin = imgfin.astype('uint8')
#print(imgfin)

imgblue = np.zeros(imgmat.shape)
imgblue[:,:,0] = 255
#imgblue = imgblue.astype('uint8')

imggreen = np.zeros(imgmat.shape)
imggreen[:,:,1] = 255
#imggreen = imggreen.astype('uint8')

imgred = np.zeros(imgmat.shape)
imgred[:,:,2] = 255
#imgred = imgred.astype('uint8')

iblue = imgblue - imgmat
igreen = imggreen - imgmat
ired = imgred - imgmat

iblue2 = np.power(iblue, 2)
igreen2 = np.power(igreen, 2)
ired2 = np.power(ired, 2)

iblues = iblue2[:,:,0] + iblue2[:,:,1] + iblue2[:,:,2]
igreens = igreen2[:,:,0] + igreen2[:,:,1] + igreen2[:,:,2]
ireds = ired2[:,:,0] + ired2[:,:,1] + ired2[:,:,2]

bluecheck = np.zeros(imgmat.shape)

bluecheck[:,:,0] = np.where(iblues<=ireds,
                  np.where(iblues<=igreens,255,0),0)
bluecheck[:,:,1] = np.where(iblues<=ireds,
                  np.where(iblues<=igreens,0,0),0)
bluecheck[:,:,2] = np.where(iblues<=ireds,
                  np.where(iblues<=igreens,0,0),0)
bluecheck = bluecheck.astype('uint8')

greencheck = np.zeros(imgmat.shape)
greencheck[:,:,0] = np.where(igreens<iblues,
                  np.where(igreens<=ireds,0,0),0)
greencheck[:,:,1] = np.where(igreens<iblues,
                  np.where(igreens<=ireds,255,0),0)
greencheck[:,:,2] = np.where(igreens<iblues,
                  np.where(igreens<=ireds,0,0),0)
greencheck = greencheck.astype('uint8')

redcheck = np.zeros(imgmat.shape)
redcheck[:,:,0] = np.where(ireds<iblues,
                  np.where(ireds<igreens,0,0),0)
redcheck[:,:,1] = np.where(ireds<iblues,
                  np.where(ireds<igreens,0,0),0)
redcheck[:,:,2] = np.where(ireds<iblues,
                  np.where(ireds<igreens,255,0),0)
redcheck = redcheck.astype('uint8')

imgfin = bluecheck + greencheck + redcheck

"""
elapsed_time = timeit.timeit(code_to_test, number=1)
print(elapsed_time)

#cv2.imshow('window2',imgfin)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
