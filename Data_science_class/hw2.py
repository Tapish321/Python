import sys
import os

def make_length_wordcount(input_file):
    length_wordcount_dict = {}
    for line in input_file:
        if len(line) == 0:
            pass
        else:
            line = line.lower()
            words  = line.split()

            for word in words:
                word = int(len(word))
                if word in length_wordcount_dict:
                    length_wordcount_dict[word] += 1
                else:
                    length_wordcount_dict[word] = 1
    return length_wordcount_dict

def make_word_count(input_file):
    input_file.seek(0,0)
    wordcount_dict = {}
    for line in input_file:
        if len(line) == 0:
            pass
        else:
            line = line.lower()
            words  = line.split()
            for word in words:
                word = str(word)
                if word in wordcount_dict:
                    wordcount_dict[word] += 1
                else:
                    wordcount_dict[word] = 1
    return wordcount_dict


def analyse_text(input_file,input_file_name):
    length_wordcount = make_length_wordcount(input_file)
    wordcount = make_word_count(input_file)
    file_name_,file_extension = input_file_name.split(".")
    outfile = file_name_ + "_analyzed_IMRAN_BIJAPURE." + file_extension
    sorted_length_wordcount = iter(sorted(length_wordcount.iteritems()))
    sorted_wordcount = iter(sorted(wordcount.iteritems()))
    file_output = open(outfile,"w")
    for key,value in sorted_length_wordcount:
        value_write =  'Words of length {} : {}'.format(key, value)
        file_output.write(value_write)
        file_output.write("\n")

    for key,value in sorted_wordcount:
        value_write =  '{} : {}'.format(key, value)
        file_output.write(value_write)
        file_output.write("\n")
    file_output.close()


input_file = ["nasdaq.txt","raven.txt","frankenstein.txt"]
for file_name in input_file:
    file_reader = open(file_name,"r")
    output = analyse_text(file_reader,file_name)
    file_reader.close()

