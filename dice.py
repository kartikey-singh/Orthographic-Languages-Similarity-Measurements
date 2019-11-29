import pickle
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Character n-gram model
# dice = 2*|ngram(x) intersection ngram(y)|/|ngram(x) union ngram(y)|
def ngram(q, n=2):
    return [q[i:i+n] for i in range(len(q)-n+1)]


def dice(x, y, n=2):
    intersection = len(set(ngram(x, n)).intersection(ngram(y, n)))
    union = len(ngram(x, n) + ngram(y, n))
    dice = 2*intersection/union
    return round(dice, 3)


with open('Words List/Hindi.pkl', 'rb') as f:
    hindi_list = pickle.load(f)

with open('Words List/Bhojpuri.pkl', 'rb') as f:
    bhojpuri_list = pickle.load(f)

with open('Words List/Magahi.pkl', 'rb') as f:
    magahi_list = pickle.load(f)

with open('Words List/Maithili.pkl', 'rb') as f:
    maithili_list = pickle.load(f)

ortho_languages = [bhojpuri_list, magahi_list, maithili_list]
langs = ['Bhojpuri', 'Magahi', 'Maithili']
words_taken = 300

for lang, lang_list in zip(langs, ortho_languages):
    cols = ['Hindi Words']
    cols += lang_list[:words_taken]
    df = pd.DataFrame(columns=cols)
    df['Hindi Words'] = hindi_list[:words_taken]
    for hindi_word in hindi_list[:words_taken]:
        for lang_word in lang_list[:words_taken]:
            dice_val = dice(hindi_word, lang_word)
            df.loc[np.where(df['Hindi Words'] == hindi_word)
                   [0][0], lang_word] = dice_val

    print(lang)
    df['Max Similarity'] = df.iloc[:, 1:-1].max(axis=1)
    df['Similarity'] = df.iloc[:, 1:-1].astype('float64').idxmax(axis=1)
    df.to_csv('Dice stats/' + lang + '_stats.csv', index=False)


df_maithili = pd.read_csv('Dice stats/Maithili_stats.csv')
df_bhojpuri = pd.read_csv('Dice stats/Bhojpuri_stats.csv')
df_magahi = pd.read_csv('Dice stats/Magahi_stats.csv')

dataframes = [df_bhojpuri, df_magahi, df_maithili]

for lang, df in zip(langs, dataframes):
    df = df[df['Max Similarity'] != 1].sort_values(
        'Max Similarity', ascending=False)
    df = df[['Hindi Words', 'Max Similarity', 'Similarity']][:10]
    df.to_csv('Dice stats/' + lang + '_final.csv')
