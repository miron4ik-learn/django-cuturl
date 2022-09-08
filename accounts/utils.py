import string
from random import choice

def generate_short_url(size = 6):
  letters = string.ascii_lowercase
  rand_str = ''.join(choice(letters) for i in range(size))
  return rand_str