sentence = input("Enter a sentence: ")
word = max(sentence.split(), key=len)
print("Longest word is: " + word + " and its length is: " + str(len(word)))
