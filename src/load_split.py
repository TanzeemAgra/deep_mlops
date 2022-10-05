import os
import numpy as np
import shutil
import random
import yaml
import argparse
from getdata import get_data
from folder import create_fold
import shutil
import sys


#####method for splitting the images for train and test####
def train_test_split(config):
    config =  get_data(config)
    root_dir = config['data_source']['data_src'] 
    dest = config['load_data']['preprocessed_data']
    p = config['load_data']['full_p']
    cla = config['data_source']['data_src']
    cla = os.listdir(cla)
    cla = [i for i in cla if not i.endswith('.dvc') and cla if not i.startswith('.git')]
    print(cla)
    splitr = config['train_split']['split_ratio']
    print(splitr)
    

    for k in range(len(cla)):
        print(cla[k])
        per = len(os.listdir((os.path.join(root_dir,cla[k]))))
        cnt = 0
        for j in os.listdir(os.path.join(root_dir,cla[k])):
            #per = len(os.path.join(root_dir,cla[k]))
            #print(per)
            pat = os.path.join(p+'/'+cla[k],j)
            split_ratio = round((splitr/100)*per)
            print(split_ratio)
            if cnt != split_ratio:
                #print(cnt)
                shutil.copy(pat,dest+'/'+'train/class_'+str(k))
                cnt = cnt+1

            else:
                shutil.copy(pat,dest+'/'+'test/class_'+str(k))

    print('done')


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = 'parameters.yaml')
    passed_args = args.parse_args()
    train_test_split(config=passed_args.config)