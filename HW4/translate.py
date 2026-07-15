# translate.py
# Yuan Xie
#
# Big Latin Translator

# prompt the word
word = input("Enter a word:")
# convert into lowercase
word = word.lower()
if word[0]=='a' or word[0]=='e' or word[0]=='i' or word[0]=='o' or word[0]=='u':
    print(word,"in Pig latin is",str(word)+"way")
else:
    print(word,"in Pig latin is",str(word[1:])+str(word[0])+"ay")
