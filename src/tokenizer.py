class Tokenizer: #defining a new class.
    def __init__(self):#telling the system its about its own self, function in a class is called method.
        self.vocabulary=[]
        self.char_to_id={}
        self.id_to_char={}

    def build_vocabulary(self,text):
        unique_charecters=set()

        for charecter in text:
                unique_charecters.add(charecter)

        self.vocabulary=sorted(unique_charecters)
        for index,charecter in enumerate(self.vocabulary):
            self.char_to_id[charecter]=index
            self.id_to_char[index]=charecter
    def encode(self,text):
         if not self.vocabulary:
              raise ValueError(
                   "Vocabulary has not been built. Call build_vocabulary() first"
              )
         encoded=[]
         for charecter in text:
              encoded.append(self.char_to_id[charecter])

         return encoded
        
    def decode(self,token_ids):
         decoded=[]
         for token in token_ids:
              decoded.append(self.id_to_char[token])
         return "".join(decoded)