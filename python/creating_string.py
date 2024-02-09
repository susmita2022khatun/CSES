s = input()
letter = list(s)
output = set()
def numways(word, letter):
    if len(letter)==1:
        output.add(word+letter[0])
    else:
        for i in range(len(letter)):
            numways(word + letter[i], letter[0:i]+letter[i+1:])
numways("",letter)
print(len(output))
print("\n".join(sorted(output)))