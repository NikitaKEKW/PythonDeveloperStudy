message = str("How are you? Eh, ok. Low or Lower? Ohhh.")
upperSymbols = [letter for letter in message if letter.isupper()]
result = "".join(upperSymbols)
print(message, "\n" + result)
