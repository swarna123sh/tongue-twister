print("***** Task 2: *******")
import random
import matplotlib.pyplot as plt
# Consonant list
consonants=["b","p","s","r"]
# Wordlist dictionary
wordlist={"b":"butter,better,betty,bought","p":"Peter Potter,poodle,peanut butter","s":"she,sells,seashells, seashore","r":"round,rugged,rock,ragged,rabbit ran"}
# Randomly choose the consonant
ch=random.choice(consonants)
# Display the words related to the consonants
print(wordlist[ch])
#Create your tongue twister
tt=input("Type a tongue twister using the list of words displayed \n: ")

# Function that calculates the word frequency
def count_words(text):      
    word_counts = {} 
    for word in text.split(" "): 
        if word in word_counts: 
            word_counts[word]=word_counts[word]+ 1   
        else: 
            word_counts[word]= 1 
    return word_counts 
# Call the function to store the word frequency in a dictionary
z=count_words(tt.lower())  
print(z)
# Store the keys and values in a variable to use for graph
keys = z.keys()
values = z.values()
# Plot the bar graph using the keys and values
plt.bar(keys, values)
# Store the graph in .png file
plt.savefig("out.png")