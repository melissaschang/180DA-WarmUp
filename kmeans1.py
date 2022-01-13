#This code was taken and edited from https://gist.github.com/aysebilgegunduz/68c777d78e31638a3f905efe441dda03#file-dominant_color-py
#which is mentioned in the mediuma article https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
#Changes made to the code are commented down below

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from IPython.display import clear_output


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist


def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

#turns on video capture
cap = cv2.VideoCapture(0);


i = 0

while True:
    #displays the frame of the video
    _, frame = cap.read()

    #I added this code to figure out how large my camera frame is
    #height, width, _ = frame.shape 
    #print(height, width)
    #dim 480 640

    #I set region to 100 pixels close to the middle of the frame
    region=frame[200:300,240:340]

    #I drew a rectangle around my desired region
    cv2.rectangle(frame, (237, 197), (343, 303), (0, 255, 0), 3)

    #shows the actual camera window
    cv2.imshow("frame", frame)

    #the color palette was changing too fast, so I added in a for loop to only change it every 20 frames
    if (i == 20):
        img = cv2.cvtColor(region, cv2.COLOR_BGR2RGB)

        img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
        clt = KMeans(n_clusters=3) #cluster number
        clt.fit(img)

        hist = find_histogram(clt)
        bar = plot_colors2(hist, clt.cluster_centers_)
       # cv2.imshow('dominant', bar)
        clear_output(wait=True)

        #this line makes the plot interactive, allowing the plot to continuously update
        plt.ion()

        plt.axis("off")
        plt.imshow(bar)

        #pause
        plt.pause(0.05)
        plt.show()

    i+=1
    if (i>20):
        i=0

    key = cv2.waitKey(1)

    if key == 'q':
        break



cap.release()
cv2.destroyAllWindows()

    
