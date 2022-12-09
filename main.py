import pandas
data_file = pandas.read_csv("nato_phonetic_alphabet.csv")
df_data_file = pandas.DataFrame(data_file)
# print(df_data_file)
phonetic_dict = {row.letter: row.code for (index, row) in df_data_file.iterrows()}
# print(phonetic_dict)
is_on = True
while is_on:
    user_input = input("Enter a word: ").upper()
    try:
        result = [phonetic_dict[letter] for letter in user_input]
        print(result)
        is_on = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
