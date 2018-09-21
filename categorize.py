""" The script creates symbolic links
corresponding to each of the three label categories:
benign, malignant, and indeterminate.
"""
import yaml
from glob import glob
import os, errno
from os.path import join
# from tqdm import tqdm

def mkdir(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def get_klass(rec):
    return rec['meta']['clinical']['benign_malignant']

def get_image_name(lab, path=None):
    s = path + '/Images/' + os.path.basename(lab) + '.jpg'
    return s

def main(path='./Data'):
    train_path = path + '/train'

    # Create directories for each label
    for klass in ['benign', 'malignant', 'indeterminate']:
        mkdir(join(train_path, klass))

    # Create symbolic links from descriptions
    fs = glob(path + '/Descriptions/*')
    # for f in tqdm(fs):
    for f in fs:
        cont = yaml.load(open(f))
        klass = get_klass(cont)
        img = get_image_name(f, path='../..')
        new_name = join(train_path, klass, os.path.basename(img))
        if not os.path.isfile(new_name):
            print(img, new_name)
            os.symlink(img, new_name)

main()
