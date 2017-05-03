import random
result=open("in.txt","r+") 
word=result.read();

    

word=word.split(' ')



faltu_words = []



def scramble(word):

    first = word[0]

    middle = word[1:-1]

    last = word[-1]

    jumble = random.sample(middle, len(middle))

    new = "".join(jumble)

    faltu = first + new + last

    return faltu




def scramble_hyphen (word):

    hyphen = word.split('-')

    new_hyphen = scramble(hyphen[0]) + "-" + scramble(hyphen[1])

    return new_hyphen

for item in word:

    if len(item) < 2:

        faltu_words.append(item)

    elif (item.find("-") == -1):

        faltu_words.append(scramble(item))

    else:

        faltu_words.append(scramble_hyphen(item))
        


scambler_words = " ".join(faltu_words)

result= open("out.txt","w")
result.write(scambler_words);
result.close()
