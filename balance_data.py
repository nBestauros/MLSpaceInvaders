import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

#https://stackoverflow.com/questions/55890813/how-to-fix-object-arrays-cannot-be-loaded-when-allow-pickle-false-for-imdb-loa/56062555
# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

train_data = np.load('training_data.npy')

# restore np.load for future normal usage
np.load = np_load_old

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
shoots = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0]:
        lefts.append([img,choice])
    elif choice[1] == 1:
        shoots.append([img,choice])
    elif choice == [0,0,1]:
        rights.append([img,choice])
    else:
        print('no matches')


shoots = shoots[:len(lefts)][:len(rights)]
lefts = lefts[:len(shoots)]
rights = rights[:len(shoots)]

final_data = shoots + lefts + rights
shuffle(final_data)

np.save('training_data_v2.npy', final_data)