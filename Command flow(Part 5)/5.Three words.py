def threewords(text):
 words = text.split()
 for i in range(len(words) - 2):
  if words[i].isalpha() and words[i+1].isalpha() and words[i+2].isalpha():
   return True
 return False
  
message = input("Введите текст:")
print(threewords(message))