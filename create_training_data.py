#https://pythonprogramming.net/self-driving-car-neural-network-training-data-python-plays-gta-v/
import numpy as np
from grab_screen import grab_screen
import cv2
import time
from getkeys import key_check
import os


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array

    [Left, Shoot, Right] boolean values.
    '''
    output = [0,0,0]
    
    if 'A' in keys:
        output[0] = 1
    if 'D' in keys:
        output[2] = 1
    if 'W' in keys:
        output[1] = 1
    return output

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []

def main():

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
        
    while(True):
        # 500x500 windowed mode
        screen = grab_screen(region=(0,0,500,500))
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # resize to something a bit more acceptable for a CNN
        screen = cv2.resize(screen, (50,50))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen,output])
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name,training_data)
main()