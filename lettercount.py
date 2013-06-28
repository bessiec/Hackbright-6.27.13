
# open file using the .open method
# process a character at a time as a bytestream using the .read method with argument of 1

#opening the file twain.txt
twain = open("twain.txt")
#creating a string that contains all the text in twain.txt by reading the file twain.txt
contents = twain.read()
#close the file, because we have everything in the contents
twain.close()

print len(contents)

#contents.lower()

# counter = 0
# for words in content
# ord(contents)

# counter = 0

# 	for words in contents:
# 		ord()

#will need to use string.lower() and ord()

#will need to convert all letters to lower case in order to count each letter

# needs to be interated through like a list

# for char in filetext:
# 	print char

# def count_letters(word, char):
# 	counter = 0
# 	while counter <- len(word):
# 		for char in word
# 			if char == 
# 				count +=1
# 			return count
# 			print count







