import os

filenames = os.listdir("./data_txt/")
with open('all_words.txt', 'w') as outfile:
    for fname in filenames:
        with open("./data_txt/"+fname) as infile:
            outfile.write(infile.read())
