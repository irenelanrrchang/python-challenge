#Pyparagragh



file = '3. Python/paragraph_1.txt'


# Approximate word count
with open(file, 'r', encoding='UTF-8') as paragraph:
  paragraph_lines = paragraph.readlines()
  for line in paragraph_lines:
        words = line.split()
        num_words = len(words)
  print("Approximate Word Count:", num_words)

# Aproximate sentence count
  for line in paragraph_lines:
      num_sentence = line.count(".")
  print("Approximate Word Count:", num_sentence)

# Average sentence length (in words)
  avg_sentence_lengh = num_words/ num_sentence
  print("Average sentence length:", avg_sentence_lengh )

# Approximate letter count (per word)
  num_letters = 0
  for word in words:
      num_letters = num_letters + len(word)
  avg_num_letter = num_letters/ num_words 
  print("Approximate Letter Count per Word:", avg_num_letter)


    
    
        