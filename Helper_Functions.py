import tensorflow as tf
import os
import numpy as np
import cv2
from sklearn.utils import shuffle

#Labeling data
def label_img(img):
    word_label = img.split('_')[0]
    if word_label == 'glass': return [1,0]
    elif word_label == 'table': return [0,1]

#Function for importing data(images) from train directory.
def create_train_data():
    training_data = []
    for img in tqdm(os.listdir(TRAIN_DIR)):
        label = label_img(img)
        path = os.path.join(TRAIN_DIR,img)
        img = cv2.imread(path,1)
        img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
        training_data.append([np.array(img),np.array(label)])
    shuffle(training_data)
    np.save('train_data_bi.npy', training_data)
    return training_data
	
#STARTING WEIGHTS
def init_weights(shape):
    init_random_dist = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(init_random_dist)

#Starting BIAS
def init_bias(shape):
    init_bias_vals = tf.constant(0.1, shape=shape)
    return tf.Variable(init_bias_vals)

#Function for convolution operation
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

#Function for pooling layer
def max_pool_2by2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')
    
#Function for convolution layer
def convolutional_layer(input_x, shape):
    W = init_weights(shape)
    b = init_bias([shape[3]])
    return tf.nn.relu(conv2d(input_x, W) + b)

#Function for FC layer
def normal_full_layer(input_layer, size):
    input_size = int(input_layer.get_shape()[1])
    W = init_weights([input_size, size])
    b = init_bias([size])
    return tf.matmul(input_layer, W) + b

#Convolutional Layer 1 + RELU
convo_1 = convolutional_layer(x,shape=[6,6,3,32], striding=[1, 4, 4, 1] )
#Pooling Layer 1
convo_1_pooling = max_pool_2by2(convo_1)
#Convolutional Layer 2 + RELU
convo_2 = convolutional_layer(convo_1_pooling,shape=[6,6,32,64])
#Pooling Layer 2
convo_2_pooling = max_pool_2by2(convo_2)
#Convolutional Layer 3 + RELU
convo_3 = convolutional_layer(convo_2_pooling,shape=[6,6,64,64])
#Pooling Layer 3
convo_3_pooling = max_pool_2by2(convo_3)
#Convolutional Layer 4 + RELU
convo_4 = convolutional_layer(convo_3_pooling,shape=[6,6,64,128])
#Pooling Layer 4
convo_4_pooling = max_pool_2by2(convo_4)
#Flattening
convo_4_flat = tf.reshape(convo_4_pooling,[-1,5*5*128])
#Fully Connected 1 + RELU
full_layer_one = tf.nn.relu(normal_full_layer(convo_4_flat,2048))
#Dropout Layer 1
hold_prob1 = tf.placeholder(tf.float32)
full_one_dropout = tf.nn.dropout(full_layer_one,keep_prob=hold_prob1)
#Fully Connected 1 + RELU
full_layer_two = tf.nn.relu(normal_full_layer(full_one_dropout,1024))
#Dropout Layer 1
hold_prob2 = tf.placeholder(tf.float32)
full_two_dropout = tf.nn.dropout(full_layer_two,keep_prob=hold_prob2)
#Output Layer,containing 2 output nodes.
y_pred = normal_full_layer(full_two_dropout,2)

#Renaming files(images) in a subfolder. Converting to .jpg
import os
os.chdir(os.path.join(os.getcwd(),"peach cherry apple"))
for f in enumerate(os.listdir()):
    os.rename(f[1],'mixed2_' +str(f[0]+1) + '.jpg2' )
    print(f)
for f in enumerate(os.listdir()):
    os.rename(f[1],'mixed2_' +str(f[0]+1) + '.jpg' )
    print(f)

print(os.getcwd())
path = os.path.join(os.getcwd(),'cat_pic.jpg')
img = cv2.imread(path,1)
plt.imshow(img)

#Converting BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

#Mirroring wrt y axis.
plt.imshow(np.fliplr(img))

#Color shifting
h,w,bpp = np.shape(img)
for py in range(0,h):
    for px in range(0,w):   
        img[py][px][0]=img[py][px][0] + 50
        img[py][px][1]=img[py][px][1] - 30
        img[py][px][2]=img[py][px][2] + 100        
plt.imshow(img)

# Cropping
crop_img = img[20:300, 10:400]
plt.imshow(crop_img)

# Adding noise
noisy1 = img + 3 * image.std() * np.random.random(image.shape)

alot  = 2 * image.max() * np.random.random(image.shape)
noisy2 = image + alot


