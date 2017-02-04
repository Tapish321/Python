#last.text file canbe found at Python/Data_science_class/last.txt

# Open last.txt file with read-only file mode.
file = open("last.txt", "r")
# OPEN FILE LAST.TXT
# READ THE FILE AND STORE IN CONTENT.

#CLOSSE THE FILE
#file.close()
# COUNTING THE NUMBER OF CHARACTERS IN THE FILE AND STORE VALUE IN ans3
# Find the number of characters in the file and assign it to ans3 variable.
content = file.read()
ans3 = len(content)


#Find the number of words in the file and assign it to ans4 variable.
words =  content.split()
ans4 = len(words)





# Find the number of lines in the file and assign it to ans5 variable.
file = open("last.txt", "r")
lines = file.readlines()
ans5 = len(lines)


#Count the last names starting with L and assign it to ans6 variable.
#print words
ans6 = 0
for name in words:
    if name.startswith('L')== True :

        ans6 = ans6 + 1




#Count the last names ending with E and assign it to ans7 variable.
ans7 = 0
for name in words:
    if name.endswith('E')== True :

        ans7 = ans7 + 1

#Count the last names with length 3 and assign it to ans8 variable.
onlywords = words[0::2]
ans8=0
for names in words:
    if len(names)==3:
        ans8 = ans8 + 1



#Count the numbers larger than 0.1 and assign it to ans9 variable.
onlynumbers = words[1::2]
#print onlynumbers
#print len(onlynumbers)
ans9 = 0
#print type(onlynumbers[0])
for num in onlynumbers:
    if float(num) > 0.1:
        ans9 = ans9 + 1





# Count the numbers smaller than 0.02 and assign it ans10 variable.
ans10 = 0
# print type(onlynumbers[0])
for num in onlynumbers:
    if float(num) < 0.02:
        ans10 += 1



# Get the number associated to your last name and assign it to ans11 variable. If your last name doesnt appear, ans11 should be 0.

n =0
for name in lines:
    i = name.split('\t')
    if (i[0]=="BIJAPURE"):
        n=1
        ans11=i[1]
if (n == 1):
     ans11
else:
    ans11 = 0

# Find the last name that comes last in the dictionary order and assign it to ans12 variable.
ans12 = max(onlywords)

#print max(words)
# Find the last name that comes first in the dictionary order and assign it to ans13 variable.
ans13 = min(onlywords)

#print min(words)
# Find the longest last name and assign it to ans14 variable.
#ans14 = ""
#largestLen=0
#for word in onlywords:
    #if largestLen < len(word):
        #largestLen = len(word)
       # ans14 = word
#print ans14
ans14 = max(onlywords, key=len)
#print ans14
# Find the shortest last name and assign it to ans15 variable.
#ans15 = ""
smallestLen=100
#for word in onlywords:
   # if smallestLen > len(word):
        #smallestLen = len(word)
        #ans15 = word
#print ans15
ans15= min(onlywords, key=len)
file.close()
#print ans15
#(Note: dont worry about the weird last name in the file. I put it there intentionally.)
#Create a new file hw1_2_answers_FIRST_LAST.txt using open() function with write mode, where FIRST and LAST should be your first and last names. For example, hw1_2_answers_GENE_LEE.txt.
outfile = open("hw1_2_answers_IMRAN_BIJAPURE", "w")
#Write your first name, last name, and email address in the first line of hw1_2_answers_FIRST_LAST.txt file.
outfile.write("IMRAN BIJAPURE imran.bijapure@mavs.uta.edu \n")

#outfile.write(" answer3=" print ans3 "\n answer4 =" print ans4  "\n answer5=" print ans5  "\n answer6=" print ans6  "\n answer7=" print ans7 "\n answer8=" print ans8 "\n answer9=" print ans9 "\n answer10=" print ans10 "\n answer11=" print ans11 "\n answer12=" print ans12 "\n answer13="print ans13 "\n answer14=" print ans14 "\n answer15=" print ans15 \n")
outfile.write(('answer3={}'.format(ans3)))
outfile.write(('\nanswer4={}'.format(ans4)))
outfile.write(('\nanswer5={}'.format(ans5)))
outfile.write(('\nanswer6={}'.format(ans6)))
outfile.write(('\nanswer7={}'.format(ans7)))
outfile.write(('\nanswer8={}'.format(ans8)))
outfile.write(('\nanswer9={}'.format(ans9)))
outfile.write(('\nanswer10={}'.format(ans10)))
outfile.write(('\nanswer11={}'.format(ans11)))
outfile.write(('\nanswer12={}'.format(ans12)))
outfile.write(('\nanswer13={}'.format(ans13)))
outfile.write(('\nanswer14={}'.format(ans14)))
outfile.write(('\nanswer15={}'.format(ans15)))
#Write Homework 1 Part 2 is done!!! in the last line of hw1_2_answers_FIRST_LAST.txt file.
outfile.write("\nHomework 1 part 2 is done!!!")
#	Close hw1_2_answer_FIRST_LAST.txt file.
outfile.close()


