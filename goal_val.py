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
    for i in l[:2500]:
        shutil.copy2(jpg_imag+i,val_data)


