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

#Read .txt file in Python3
f = open('train.txt', 'r')
x = f.read().splitlines()
f.close()

#Shape of a tensor in TensorFlow

tensor_name.get_shape().as_list()

#Embed a Youtube video on jupyter

from IPython.display import YouTubeVideo
YouTubeVideo('dEFd_2_b6X8')

#Nice Distribution Plot
plt.figure(figsize=(16,6))
features = train_df.columns.values[2:202]
plt.title("Distribution of max values per row in the train and test set")
sns.distplot(train_df[features].max(axis=1),color="brown", kde=True,bins=120, label='train')
sns.distplot(test_df[features].max(axis=1),color="yellow", kde=True,bins=120, label='test')
plt.legend()
plt.show()

#Fixing the seed
import os, torch, random,numpy as np, tensorflow as tf
def seed_everything(seed=1234):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
    #torch.manual_seed(seed)
    #torch.cuda.manual_seed(seed)
    #torch.backends.cudnn.deterministic = True

#Convnet on PyTorch
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, kernel_size=5)
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(16 * 5 * 5 , 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.max_pool2d(self.conv1(x), 2)
        x = F.relu(x)
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 16 * 5 * 5 )
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # PyTorch v0.4.0
model = Net().to(device)

summary(model, (3, 32, 32))

#Numpy np.average Weighted average
import numpy as np
k = np.average([3,5,7],weights = [10,5,20])
print(k)
#k = 5.571428


#Embedding Layer on Tabular Data
#https://www.kaggle.com/kernels/scriptcontent/14377501/download
def create_model(data, catcols, numcols):    
    inputs = []
    outputs = []
    for c in catcols:
        num_unique_values = int(data[c].nunique())
        embed_dim = int(min(np.ceil((num_unique_values)/2), 50))
        inp = layers.Input(shape=(1,))
        out = layers.Embedding(num_unique_values + 1, embed_dim, name=c)(inp)
        out = layers.SpatialDropout1D(0.3)(out)
        out = layers.Reshape(target_shape=(embed_dim, ))(out)
        inputs.append(inp)
        outputs.append(out)
    
    num_input = layers.Input(shape=(data[numcols].shape[1], ))
    inputs.append(num_input)
    outputs.append(num_input)
    
    x = layers.Concatenate()(outputs)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    x = Dense(128, activation="relu")(x)
    x = Dropout(0.3)(x)
    x = BatchNormalization()(x)
    x = Dense(32, activation="relu")(x)
    x = Dropout(0.3)(x)
    x = BatchNormalization()(x)
    y = Dense(1, activation="sigmoid")(x)
    
    model = Model(inputs=inputs, outputs=y)
    model.compile(loss='binary_crossentropy', optimizer='adam')
    return model

clf = create_model(data, catcols, numcols)
clf.fit([train.loc[:, catcols].values[:, k] for k in range(train.loc[:, catcols].values.shape[1])] + 
	[train.loc[:, numcols].values], 
        train.target.values,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS)
test_preds = clf.predict([test.loc[:, catcols].values[:, k] for k in range(test.loc[:, catcols].values.shape[1])] 
			 + [test.loc[:, numcols].values])

#Variance Threshold to select features
from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=1.5).fit(train2[cols])
train3 = sel.transform(train2[cols])
test3 = sel.transform(test2[cols])

#Hash a string

import hashlib

public_ids = []
for i in range(256*512+1):
    st = str(i)+"test"
    public_ids.append( hashlib.md5(st.encode()).hexdigest() )

# np.allclose, returning two n dimensional arrays are close to each other
import numpy as np

if np.allclose(useful_train,useful_public):
    print('Public dataset has the SAME structure as train')
else:
    print('Public dataset DOES NOT HAVE the same structure as train')

# all models in sklearn scikit-learn
from sklearn.utils.testing import all_estimators
estimators = all_estimators()

#Multiprocessing
import multiprocessing


def load_data(data):
    return pd.read_csv(data)

with multiprocessing.Pool() as pool:
    train, test, sub = pool.map(load_data, ['../input/train.csv', '../input/test.csv', '../input/sample_submission.csv'])

#DataFramedeki tüm column'ları çarpmak için
pd.DataFrame([[1,2,3,4],[5,6,7,8]]).prod(axis=1)
#return a pd.Series object
#24
#1680

#pd.DataFrame().iteritems()
#https://www.kaggle.com/c/ieee-fraud-detection/discussion/101203
for col, values in df_train.iteritems():
    num_uniques = values.nunique()
    print ('{name}: {num_unique}'.format(name=col, num_unique=num_uniques))
    print (values.unique())
    print ('\n')

#Resumetable
from scipy import stats
def resumetable(df):
    print(f"Dataset Shape: {df.shape}")
    summary = pd.DataFrame(df.dtypes,columns=['dtypes'])
    summary = summary.reset_index()
    summary['Name'] = summary['index']
    summary = summary[['Name','dtypes']]
    summary['Missing'] = df.isnull().sum().values    
    summary['Uniques'] = df.nunique().values
    summary['First Value'] = df.loc[0].values
    summary['Second Value'] = df.loc[1].values
    summary['Third Value'] = df.loc[2].values

    for name in summary['Name'].value_counts().index:
        summary.loc[summary['Name'] == name, 'Entropy'] = round(stats.entropy(df[name].value_counts(normalize=True), base=2),2) 

    return summary

#https://www.kaggle.com/nroman/eda-for-cis-fraud-detection
# This code is stolen from Chris Deotte. 
def relax_data(df_train, df_test, col):
    cv1 = pd.DataFrame(df_train[col].value_counts().reset_index().rename({col:'train'},axis=1))
    cv2 = pd.DataFrame(df_test[col].value_counts().reset_index().rename({col:'test'},axis=1))
    cv3 = pd.merge(cv1,cv2,on='index',how='outer')
    factor = len(df_test)/len(df_train)
    cv3['train'].fillna(0,inplace=True)
    cv3['test'].fillna(0,inplace=True)
    cv3['remove'] = False
    cv3['remove'] = cv3['remove'] | (cv3['train'] < len(df_train)/10000)
    cv3['remove'] = cv3['remove'] | (factor*cv3['train'] < cv3['test']/3)
    cv3['remove'] = cv3['remove'] | (factor*cv3['train'] > 3*cv3['test'])
    cv3['new'] = cv3.apply(lambda x: x['index'] if x['remove']==False else 0,axis=1)
    cv3['new'],_ = cv3['new'].factorize(sort=True)
    cv3.set_index('index',inplace=True)
    cc = cv3['new'].to_dict()
    df_train[col] = df_train[col].map(cc)
    df_test[col] = df_test[col].map(cc)
    return df_train, df_test

#https://www.kaggle.com/nroman/eda-for-cis-fraud-detection
def plot_numerical(feature):
    """
    Plot some information about a numerical feature for both train and test set.
    Args:
        feature (str): name of the column in DataFrame
    """
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(16, 18))
    sns.kdeplot(train[feature], ax=axes[0][0], label='Train');
    sns.kdeplot(test[feature], ax=axes[0][0], label='Test');

    sns.kdeplot(train[train['isFraud']==0][feature], ax=axes[0][1], label='isFraud 0')
    sns.kdeplot(train[train['isFraud']==1][feature], ax=axes[0][1], label='isFraud 1')

    test[feature].index += len(train)
    axes[1][0].plot(train[feature], '.', label='Train');
    axes[1][0].plot(test[feature], '.', label='Test');
    axes[1][0].set_xlabel('row index');
    axes[1][0].legend()
    test[feature].index -= len(train)

    axes[1][1].plot(train[train['isFraud']==0][feature], '.', label='isFraud 0');
    axes[1][1].plot(train[train['isFraud']==1][feature], '.', label='isFraud 1');
    axes[1][1].set_xlabel('row index');
    axes[1][1].legend()

    pd.DataFrame({'train': [train[feature].isnull().sum()], 'test': [test[feature].isnull().sum()]}).plot(kind='bar', rot=0, ax=axes[2][0]);
    pd.DataFrame({'isFraud 0': [train[(train['isFraud']==0) & (train[feature].isnull())][feature].shape[0]],
                  'isFraud 1': [train[(train['isFraud']==1) & (train[feature].isnull())][feature].shape[0]]}).plot(kind='bar', rot=0, ax=axes[2][1]);

    fig.suptitle(feature, fontsize=18);
    axes[0][0].set_title('Train/Test KDE distribution');
    axes[0][1].set_title('Target value KDE distribution');
    axes[1][0].set_title('Index versus value: Train/Test distribution');
    axes[1][1].set_title('Index versus value: Target distribution');
    axes[2][0].set_title('Number of NaNs');
    axes[2][1].set_title('Target value distribution among NaN values');

#https://www.kaggle.com/nroman/eda-for-cis-fraud-detection
#covariate_shift
def covariate_shift(feature):
    df_card1_train = pd.DataFrame(data={feature: train[feature], 'isTest': 0})
    df_card1_test = pd.DataFrame(data={feature: test[feature], 'isTest': 1})

    # Creating a single dataframe
    df = pd.concat([df_card1_train, df_card1_test], ignore_index=True)
    
    # Encoding if feature is categorical
    if str(df[feature].dtype) in ['object', 'category']:
        df[feature] = LabelEncoder().fit_transform(df[feature].astype(str))
    
    # Splitting it to a training and testing set
    X_train, X_test, y_train, y_test = train_test_split(df[feature], df['isTest'], test_size=0.33, random_state=47, stratify=df['isTest'])

    clf = lgb.LGBMClassifier(**params, num_boost_round=500)
    clf.fit(X_train.values.reshape(-1, 1), y_train)
    roc_auc =  roc_auc_score(y_test, clf.predict_proba(X_test.values.reshape(-1, 1))[:, 1])

    del df, X_train, y_train, X_test, y_test
    gc.collect();
    
    return roc_auc


# selecting categorical features or extracting
#train  is a pd DataFrame.
numerical_cols = train.select_dtypes(exclude = 'object').columns
categorical_cols = train.select_dtypes(include = 'object').columns

#Calling a method with argument in Pandas Multi Columns
def temp(a1,a2,a3=3):
    return a1 + a2 + a3
df = pd.DataFrame({'A':[3,4,5],'B':[4,5,6]})
df[['A','B']].apply(lambda x: temp(x[0],x[1],a3=4),axis=1)

#Rolling mean in pandas series transform method and shift
temp_df['rolling_mean_'+str(i)] = temp_df.groupby(['id'])[TARGET].transform(lambda x: x.shift(1).rolling(i).mean())

#Convert a dataframe to sparse matrix to lower memory usage
from scipy import sparse 
temp_matrix = sparse.csr_matrix(temp_df)

print(type(temp_matrix))
#scipy.sparse.csr.csr_matrix

print(temp_matrix[:5].todense())
#matrix([[nan, nan, nan, nan, nan, nan],
#        [nan, nan, nan, nan, nan, nan],
#        [nan, nan, nan, nan, nan, nan],
#        [nan, nan, nan, nan, nan, nan],
#        [nan, nan, nan, nan, nan, nan]])


#Forcing python to return a data type
def rmsse(self, valid_preds: pd.DataFrame, lv: int) -> pd.Series:
	valid_y = getattr(self, f'lv{lv}_valid_df')
	score = ((valid_y - valid_preds) ** 2).mean(axis=1)
	scale = getattr(self, f'lv{lv}_scale')
	return (score / scale).map(np.sqrt)

#How to reduce lightgbm memory usage
X_train_np = X_train.values.astype(np.float32)
X_valid_np = X_valid.values.astype(np.float32)

del X_train, X_valid
gc.collect()

train_dataset = lgb.Dataset(X_train_np, label = y_train, feature_name = list(features))
train_dataset = lgb.Dataset(X_valid_np, label = y_valid, feature_name = list(features))

#Plotting correlation matrix colorized
corr = data[data['year'].isin([2013,2014,2015,2016])][features[:26] + ['quantity'] ].corr()
corr.style.background_gradient(cmap='coolwarm')

# Inheritance

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    # Overriding __init__ method of Person
    def __init__(self, fname, lname, year):
        # Thanks to super() function, it is going to inherit from the parent Class automatically.
        super().__init__(fname, lname)
        self.graduationyear = year

    #
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)






