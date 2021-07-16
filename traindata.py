#https://pythonprogramming.net/training-self-driving-car-neural-network-python-plays-gta-v/?completed=/balancing-neural-network-training-data-python-plays-gta-v/
# %%
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
import numpy as np
# %%
physical_devices = tf.config.experimental.list_physical_devices('GPU')
print("Num GPUs Available: ", len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0], True)
# %%
model = Sequential([
    Conv2D(filters=96, kernel_size=(11,11), strides=(4, 4), activation='relu', input_shape=(50,50,1)),
    BatchNormalization(),
    MaxPool2D(pool_size=(3,3), strides=(2,2), padding="same"),
    Conv2D(filters=256, kernel_size=(5,5), strides=(1,1), activation='relu', padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3,3), strides=(2,2), padding="same"),
    Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
    BatchNormalization(),
    Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
    BatchNormalization(),
    Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3,3), strides=(2,2), padding="same"),
    Flatten(),
    Dense(4096, activation='relu'),
    Dropout(0.5),
    Dense(4096, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')

])
# %%
LR = 1e-3
EPOCHS = 50
MODEL_NAME = 'spaceinvaders-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',50)

#https://stackoverflow.com/questions/55890813/how-to-fix-object-arrays-cannot-be-loaded-when-allow-pickle-false-for-imdb-loa/56062555
# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

train_data = np.load('training_data.npy')

# restore np.load for future normal usage
np.load = np_load_old



train = train_data[:-500]
test=train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1, 50,50,1)
Y = np.array([i[1] for i in train])

test_x = np.array([i[0] for i in test]).reshape(-1,50,50,1)
test_y = np.array([i[1] for i in test])
# %%
model.compile(optimizer=Adam(learning_rate=0.00001), loss='categorical_crossentropy', metrics=['accuracy'])
# %%
model.fit(x=X, y=Y,batch_size=100, epochs=50,verbose=1, validation_data=(test_x, test_y))
# %%
model.save(MODEL_NAME)