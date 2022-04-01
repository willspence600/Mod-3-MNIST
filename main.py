#video for adrian https://youtu.be/yuuDJ3-EdNQ?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

from tkinter import *
import numpy as np
import matplotlib.pyplot as plot
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from tensorflow.keras.datasets import mnist
from sklearn import datasets, neighbors
from sklearn.model_selection import train_test_split
import torch

import combined_model_final

combined = combined_model_final.Combined()


# import mnist
# import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Machine Learning Models: Accuracy Testing")
root.geometry("1400x600")

def run_knn():

  '''# #loading data
  (X_train, y_train), (X_test, y_test) = mnist.load_data()
  # #reshaping data
  X_train = X_train[:60000]
  y_train = y_train[:60000]
  X_test = X_test[:1000]
  y_test = y_test[:1000]
  #
  X_train = X_train.reshape((60000, 28 * 28))
  X_test = X_test.reshape((1000, 28 * 28))
  #
  num = int(input("Enter number:"))
  #
  #creating and training knn classifier
  knn = neighbors.KNeighborsClassifier(n_neighbors=3, weights='uniform')
  knn.fit(X_train, y_train)
  #
  #getting a prediction
  pred = knn.predict(X_test)
  plt.imshow(X_test[num].reshape(28, 28))
  print("Real Label:", y_test[num])
  plt.show()
  print(f"Predicted Label: {int(combined.knn_pred(X_test[num]))}")
'''
  print("ran function")

def run_nbc():
    (xTrain, yTrain), (xTest, yTest) = mnist.load_data()
    trainNum = 20000
    testNum = 10000
    xTrain = xTrain.reshape(60000, 28 * 28)
    xTest = xTest.reshape(10000, 28 * 28)
    nbc_training = Label(root, text='Begin training')
    nbc_training.grid(row=2, column=3)
    naive_bayes_multinomial = MultinomialNB()
    fit_multinomial = naive_bayes_multinomial.fit(xTrain, yTrain)
    predictions = fit_multinomial.predict(xTest)
    con_matrix_multinomial = confusion_matrix(yTest, predictions)

    nbc_training2 = Label(root, text='Finished training')
    nbc_training2.grid(row=3, column=3)

    print("Begin Testing")
    nbc_testing = Label(root, text='Begin testing')
    nbc_testing.grid(row=4, column=3)

    print(fit_multinomial.score(xTest, yTest))
    print(con_matrix_multinomial)
    print("Finish Testing")

    nbc_testing = Label(root, text='Finished testing')
    nbc_testing.grid(row=5, column=3)

    nbc_accuracy = Label(root, text=f'Accuracy is {fit_multinomial.score(xTest, yTest) * 100}%')
    nbc_accuracy.grid(row=6, column=3)



    return
#nbc code


def run_cnn():
    return


def run_combined():
    return

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

def scale(r, rmin, rmax, tmin, tmax):
    return ((r - rmin)/(rmax - rmin)) * (tmax -tmin) + tmin

def drawOnCanvas(e):
    x, y = e.x, e.y

    if 4 == 4:
        r = round(brush_width/2)

        sx = x/10
        sy = y/10

        for i in range(round(sx), r + round(sx)):
            for j in range(round(sy), r + round(sy)):
                d2 = (i-sx)**2+(j-sy)**2
                base_color = int(255 - scale(d2, 0, 2*r**2, 0, 255)) + 1                

                #faster way to draw a circle using its symmetries
                #r^2 instead of (r^2)^2
                xpoints =[round(i), round(2*sx-i), round(2*sx-i), round(i)]

                ypoints =[round(j), round(2*sy-j), round(j), round(2*sy-j)]    
            
                color_at_symmetry =[
                imgdata[xpoints[0], ypoints[0]],
                imgdata[xpoints[1], ypoints[1]],
                imgdata[xpoints[2], ypoints[2]],
                imgdata[xpoints[3], ypoints[3]]
                ]       
                

                for k in range(4):                    
                    final_color = color_at_symmetry[k] 
                    print(final_color, base_color)         
                    if final_color < base_color:
                        final_color = base_color
                    color = rgb_hack((final_color, final_color, final_color))
                    canvas.create_rectangle(xpoints[k]*10, ypoints[k]*10, xpoints[k]*10+10, ypoints[k]*10+10, outline=color, fill=color)
                    imgdata[xpoints[k], ypoints[k]] = final_color
                    

        
#canvas stuff
brush_width = 6
imgdata = np.zeros((28, 28)) #keep track of color on canvas
canvas = Canvas(root, width = 280, height = 280, background="black")
canvas.grid(row=0, column=0)
canvas.bind("<B1-Motion>", drawOnCanvas)

#define all of the buttons size, text, and function which they call
button_knn = Button(root, text="Test K-Nearest Neighbour", padx=40, pady=20, command=run_knn)
button_cnn = Button(root, text="Test Convolutional Neural Network", padx=40, pady=20, command=run_cnn)
button_nbc = Button(root, text="Test Naive Bayes Classifier", padx=40, pady=20, command=run_nbc)
button_combined = Button(root, text="Test combination of all models", padx=40, pady=20, command=run_combined)

button_quit = Button(root, text="Exit", padx=40, pady=20, command=root.quit)


#put the buttons on the screen

button_knn.grid(row=0, column=1)
button_cnn.grid(row=0, column=2)
button_nbc.grid(row=0, column=3)
button_combined.grid(row=0, column=4)

button_quit.grid(row=5, column=4)

#Text boxes

root.mainloop()

