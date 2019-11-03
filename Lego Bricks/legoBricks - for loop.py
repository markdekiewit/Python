import timeit
code_to_test = """
import cv2
import numpy as np

image=cv2.imread('opencv1 image1.jpg',1)


imgmat = np.array(image)

imglay1 = np.array(image[:,:,0])
imglay2 = np.array(image[:,:,1])
imglay3 = np.array(image[:,:,2])
imgb = np.zeros((960, 768 ,3))
imgb[:,:,0] = 255


distb1 = imglay1 - imgb[:,:,0]
distb2 = imglay2 - imgb[:,:,1]
distb3 = imglay3 - imgb[:,:,2]


distb1  = np.power(distb1, 2)
distb2  = np.power(distb2, 2)
distb3  = np.power(distb3, 2)


finalb1 = distb1 + distb2 + distb3


#****************************************
imgg = np.zeros((960, 768 ,3))
imgg[:,:,1] = 255


distg1 = imglay1 - imgg[:,:,0]
distg2 = imglay2 - imgg[:,:,1]
distg3 = imglay3 - imgg[:,:,2]


distg1  = np.power(distg1, 2)
distg2  = np.power(distg2, 2)
distg3  = np.power(distg3, 2)


finalg1 = distg1 + distg2 + distg3


#*****************************************
imgr = np.zeros((960, 768 ,3))
imgr[:,:,2] = 255


distr1 = imglay1 - imgr[:,:,0]
distr2 = imglay2 - imgr[:,:,1]
distr3 = imglay3 - imgr[:,:,2]


distr1  = np.power(distr1, 2)
distr2  = np.power(distr2, 2)
distr3  = np.power(distr3, 2)


finalr1 = distr1 + distr2 + distr3

newimg = np.zeros((960,768,3))

for i in range(768):
    for j in range(960):
        if min(finalb1[j,i], finalg1[j,i], finalr1[j,i]) == finalb1[j,i]:
           newimg[j,i] = [255,0,0]
        elif min(finalb1[j,i], finalg1[j,i], finalr1[j,i]) == finalg1[j,i]:
            newimg[j,i] = [0,255,0]
        else:
            newimg[j,i] = [0,0,255]
newimg = newimg.astype('uint8')            

"""
elapsed_time = timeit.timeit(code_to_test, number=1)
print(elapsed_time)

#cv2.imshow('window1',newimg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()