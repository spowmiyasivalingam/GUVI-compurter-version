import cv2
import matplotlib.pyplot as plt
img =cv2.imread("img-for-practice.jpg")
print(img.shape)


cv2.rectangle(img,(1500,2550),(200,100),(0,0,225),3)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()