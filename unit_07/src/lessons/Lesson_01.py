def get_current_working_directory():
  pass

def encode_string(str_to_encode):
  """ Encodes a string using base64"""
  pass

def decode_string(base64_str_to_decode):
  """ Decodes a string encoded in base64"""
  pass
  

if __name__ == "__main__":
  print(get_current_working_directory())
  print(encode_string("Python is a cool programming language!"))
  # should print UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE=
  str_to_decode = "UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE="
  print(decode_string(str_to_decode))
  # should print Python is a cool programming language!