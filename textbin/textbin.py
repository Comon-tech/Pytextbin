class Textbin():
  def to_binary(self, text):
    binary = " ".join(format(ord(i), 'b')for i in str(text))
    return binary
    
  def to_text(self, binary):
      text = "".join(chr(int(i, 2)) for i in binary.split())
      return text
      
textbin = Textbin()


