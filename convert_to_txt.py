"""
    remove lines with
        -single no
        -stuff within brackets(() and <>)
        - ..-->..
"""

import re
import os

for filename in os.listdir("./data_srt/"):
    filename = filename.split(".")[0]
    f= open("./data_srt/" + filename + ".srt")
    fw= open("./data_txt/" + filename + ".txt","w")
    
    text = f.readlines()

    for line in text:
        if re.match("\d+", line):
            continue

        #elif re.match("[(<].*?[)>]",line):
        #newline = re.sub("[(<].*?[)>]","",line)
        else:
            fw.write(re.sub("[(<].*?[)>]","",line))


    fw.close()
    f.close()
        




