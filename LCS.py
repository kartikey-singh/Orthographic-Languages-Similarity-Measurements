import pickle
import re
from suffixtree import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def process_word(language, word, match_list):
    datum = {'Language': language, 'Word': word, 'Length': len(word), 'Empty Match': True,
             'Partial Matches': match_list, 'Correct Match': False}

    if not match_list:
        return datum

    datum['Empty Match'] = False
    correct_match = list(set(match_list).intersection([word]))
    if not correct_match:
        return datum
    else:
        datum['Correct Match'] = True
        return datum


def average_matches(df):
    return len(df[df['Empty Match'] == False])/len(df['Empty Match'])


def plot_graph(df, lang):
    df1 = df.groupby(['Length']).sum()
    y_pos = np.arange(len(df1))
    plt.figure(figsize=(9, 6))
    bars = plt.bar(y_pos, df1['Correct Match'],
                   alpha=0.7, align='center', color='lightgreen')
    plt.xticks(y_pos, df1.index)
    plt.subplots_adjust(bottom=0.3)
    plt.title(f'Exact Matches vs. Length of Words for {lang}')
    plt.tick_params(top=False, bottom=False, left=False,
                    right=False, labelleft=False, labelbottom=True)

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    for bar in bars:
        plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                       bar.get_height(), ha='center', fontsize=8)

    x = plt.gca().xaxis
    plt.savefig(f'Stat Images/Stat for{lang}.png')



with open('Words List/Hindi.pkl', 'rb') as f:
    hindi_list = pickle.load(f)

with open('Words List/Bhojpuri.pkl', 'rb') as f:
    bhojpuri_list = pickle.load(f)

with open('Words List/Magahi.pkl', 'rb') as f:
    magahi_list = pickle.load(f)

with open('Words List/Maithili.pkl', 'rb') as f:
    maithili_list = pickle.load(f)


# Unique words in each language
print(len(hindi_list))
print(len(bhojpuri_list))
print(len(magahi_list))
print(len(maithili_list))


ortho_languages = [bhojpuri_list, magahi_list, maithili_list]
langs = ['Bhojpuri', 'Magahi', 'Maithili']
cols = ['Language', 'Word', 'Length', 'Empty Match', 'Partial Matches', 'Correct Match']

# pickle tree ...
tree = SuffixTree(True, hindi_list)

for lang, lang_list in zip(langs, ortho_languages):
    print(lang)
    df = pd.DataFrame(columns=cols)
    for word in lang_list:
        match_list = tree.findString(word)
        datum = process_word(lang, word, match_list)
        df = df.append(datum, ignore_index=True)

    plot_graph(df, lang)
    df.to_csv('LCS Stats/' + lang + '_stats.csv', index=False)

df_maithili = pd.read_csv('LCS Stats/Maithili_stats.csv')
print(100*average_matches(df_maithili))
df_bhojpuri = pd.read_csv('LCS Stats/Bhojpuri_stats.csv')
print(100*average_matches(df_bhojpuri))
df_magahi = pd.read_csv('LCS Stats/Magahi_stats.csv')
print(100*average_matches(df_magahi))

print(100*len(df_maithili[df_maithili['Correct Match'] == True])/len(df_maithili))
print(100*len(df_bhojpuri[df_bhojpuri['Correct Match'] == True])/len(df_bhojpuri))
print(100*len(df_magahi[df_magahi['Correct Match'] == True])/len(df_magahi))