import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

"""
#LINE
x=np.linspace(0,20,1000)
y= np.sin(x)+0.2 *x
plt.plot(x,y)
plt.xlabel('input')
plt.ylabel('output')
plt.title('my plot')
plt.show()


"""

"""
#Scatter Plot
x=np.random.randn(200,2)
x[:50] +=4
y=np.zeros(200)
y[:50] = 1
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()
"""

"""
#histograms
x=np.random.randn(1000)
plt.hist(x,bins=50)
plt.show()
"""


#images
im=Image.open('ML Flow.jpg')
print type(im)
arr=np.array(im)
print arr
print arr.shape
plt.imshow(arr)
gray=arr.mean(axis=2)
gray.shape
plt.imshow(gray,cmap='gray')
plt.show()




