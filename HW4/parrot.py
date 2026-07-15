# parrot.py
# Yuan Xie
#
# repeat what you prompted

# prompt your words
while True:
    line = input('>')
    # if the input is quiet
    if line.lower() == 'quiet':
        break
    #if the input is not quiet
    else:
        print(line.upper())
        continue
