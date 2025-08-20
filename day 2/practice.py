import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpg")
print(img.shape)

cv2. circle(img,(100,200),50,(0,0,255),3)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()