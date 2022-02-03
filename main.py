import pandas as pd

df = pd.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv')

nato_dict = {j.letter:j.code for (i,j) in df.iterrows()}

ask = input("type: ").upper()
nato_list = [nato_dict[i] for i in ask if i in nato_dict]
print(nato_list)


