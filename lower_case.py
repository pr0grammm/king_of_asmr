f = open("all_words.txt")

text= f.read();
text = text.lower()

fw = open("all_words_lower.txt","w")
fw.write(text)

f.close()
fw.close()


