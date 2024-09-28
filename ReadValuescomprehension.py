#Program for Reading the Words from Key Board with Dict Comprehension
print("Enter List of Words separated by Comma:")
d={ word:len(word.strip())   for word in input().split(",") if word.strip().isalpha()}
print("Dict of Values")
print(d)
