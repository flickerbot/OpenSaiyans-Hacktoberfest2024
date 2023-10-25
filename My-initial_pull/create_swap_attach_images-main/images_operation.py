################## import modules  #########################
import cv2,numpy

########### using first image from local storage ###########
photoA=cv2.imread('photoA.jpg')

########### Creating image background for second image ##########
horizontal=[]
vertical=[]
center=250
pixel_color=[255,255,255]
for i in range(2*center):
    horizontal.append(pixel_color)
for j in range(2*center):
    vertical.append(horizontal)
bg=numpy.array(vertical,dtype="uint8")

########### creating new image similar to photoA #########
bcolor=0
thickness=20
photoB=cv2.rectangle(bg,(center-200,center-200),(center+200,center+200),bcolor,thickness)
photoB=cv2.circle(photoB,(center-100,center-50),50,bcolor,thickness)
photoB=cv2.circle(photoB,(center+100,center-50),50,bcolor,thickness)
photoB=cv2.circle(photoB,(center,center+100),25,bcolor,thickness)
cv2.imwrite('photoB.jpg',photoB)

######### swaping images ##############
# storing photoA as list because it will not be impacted after replacing object in photoA 
# and can be used later to repace object in photoB by converting it into numpy array
temp_photoA=photoA.tolist() 
temp_photoA=numpy.array(temp_photoA,dtype="uint8")
photoA[140:290,280:430]=photoB[140:290,280:430]
photoB[140:290,280:430]=temp_photoA[140:290,280:430]
cv2.imwrite('photoA_swap.jpg',photoA)
cv2.imwrite('photoB_swap.jpg',photoB)

########### concatenating images ##########
# same size of images can be concatenated depending on axis
con_photo=numpy.concatenate((temp_photoA,photoA),axis=1)
cv2.imwrite('collage.jpg',con_photo)