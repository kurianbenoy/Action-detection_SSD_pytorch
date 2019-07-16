import torch
import torch.nn as nn

k = torch.load('models/mobilenet_v1_with_relu_69_5.pth')

for i in k.keys():
    print(i)
    
import random
import shutil

test_file = 'ImageSplits/test.txt'
jpg_imag = 'JPEGImages/'
val_data = 'validation/'

l = []
with open(test_file) as f:
    for file in f:
	    l.append(file.split('\n')[0])

    random.shuffle(l)
    new_m = open(file, 'w')
    for i in l[:2500]:
        file= 'ImageSplits/val.txt'
        
        new_m.write(i)
        shutil.copy2(jpg_imag+i,val_data)
