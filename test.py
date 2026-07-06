from src.tokenizer import Tokenizer
tokenizer=Tokenizer()
tokenizer.build_vocabulary("hello world")
print(tokenizer.vocabulary)
print(tokenizer.char_to_id)
print(tokenizer.id_to_char)

encoded=tokenizer.encode("hello")
print("Encoded:",encoded)

decoded=tokenizer.decode(encoded)
print("Decoded:",decoded)
