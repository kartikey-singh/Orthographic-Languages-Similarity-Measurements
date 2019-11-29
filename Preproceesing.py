import pickle
import re
from suffixtree import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Stage 1 Filtering (Don't Run).
def read_filter_write(file, source_dir, target_dir, un_dir):
    with open(source_dir + un_dir + '/' + file, 'r') as f:
        data = f.read().replace('\n', ' ')

    data = filtering(data)

    with open(target_dir + un_dir + '/' + file, "w") as f:
        f.write(data)

    return data


# Removing stopword english numericals, keeping only unicode of devanagri, removing devanagri numericals,
# removing extra white spaces
def filtering(data):
    patterns = {r'<.*>+': '',
                r'[!@#$%^&*()_+<>|,.:;()+=…&×{}<>"→?\'0-9।-]': '',
                r'[^\u0900-\u097F ]': '',
                r'[\u0964-\u096F]': '',
                r'[\s+]': ' '}

    for pattern, result in patterns.items():
        data = re.sub(pattern, result, data)

    return data


source_dir = 'Unfiltered/'
unfiltered_dirs = os.listdir(source_dir)
target_dir = 'Filtered/'

for un_dir in unfiltered_dirs:
    files = os.listdir(source_dir + un_dir)
    for file in files:
        read_filter_write(file, source_dir, target_dir, un_dir)


# Stage 2 Reading filtered files for each language and storing only unique words into a new folder. (Don't Run)
# Keep unique words with len > 2 as pickled lists
filtered_dirs = os.listdir(target_dir)

for f_dir in filtered_dirs:
    files = os.listdir(target_dir + f_dir)
    word_list = []

    for file in files:
        with open(target_dir + f_dir + '/' + file, 'r') as f:
            data = f.read()
        words = data.split(' ')
        words = list((filter(None, words)))
        word_list += [word for word in words if len(word) > 2]

    word_list = list(set(word_list))

    with open('Words List/' + f_dir + '.pkl', 'wb') as f:
        pickle.dump(word_list, f)
