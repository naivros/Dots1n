import base64
import random
#
#    _____^___
#   |    |    \
#    \   /  ^ |
#   / \_/   0  \
#  /            \
# /    ____      0
#/      /  \___ _/
#________          __          ____
#\______ \   _____/  |_  _____/_   | ____
# |    |  \ /  _ \   __\/  ___/|   |/    \
# |    `   (  <_> )  |  \___ \ |   |   |  \
#/_______  /\____/|__| /____  >|___|___|  /
#        \/                 \/          \/
#________                         _________                        __
#\______ \   ____   ____   ____   \_   ___ \_______ ___.__._______/  |_  ___________
# |    |  \ /  _ \ / ___\_/ __ \  /    \  \/\_  __ <   |  |\____ \   __\/ __ \_  __ \
# |    `   (  <_> ) /_/  >  ___/  \     \____|  | \/\___  ||  |_> >  | \  ___/|  | \/
#/_______  /\____/\___  / \___  >  \______  /|__|   / ____||   __/|__|  \___  >__|
#        \/      /_____/      \/          \/        \/     |__|             \/
# DOTS1N | World's First DogeBased Crypter.
# Made for Doge by Doge.
# Doge-Fueled Crypter.

OBFUSCATOR_CODE_DICT = { 'A':'qx', 'B':'xq','C':'xq', 'D':'xq', 'E':'q','F':'qxq', 'G':'xq', 'H':'q','I':'q', 'J':'qx', 'K':'xqx','L':'qxq', 'M':'x', 'N':'xq','O':'x', 'P':'qxq', 'Q':'xqx','R':'qxq', 'S':'q', 'T':'x','U':'qx', 'V':'qx', 'W':'qx','X':'xqx', 'Y':'xqx', 'Z':'xq','1':'qx', '2':'qx', '3':'qx','4':'qx', '5':'q', '6':'xq','7':'xq', '8':'xq', '9':'xq','0':'x', ', ':'xqx', 'q':'qx','?':'qxq', '/':'xq', 'x':'xqx','(':'xq', ')':'xqx', '-':'qx'}
dedogger = 1 # Run the dedogger
## HELPERS
def xor(x, y):
  return bool((x and not y) or (not x and y))
## One-way Encoder
def encode(plaintext,key):
  throw_stdout_for_dog = ""
  secret_key = 'v'.join([OBFUSCATOR_CODE_DICT[char] for char in key.upper()])
  flag=plaintext
  try:
    flag = flag.encode("ascii")
  except (UnicodeDecodeError, AttributeError):
    pass
  for char in secret_key:
    if(char == "q" and not xor(char,char)):
      flag = base64.b64encode(flag)
      throw_stdout_for_dog = throw_stdout_for_dog + "food "
    if(char == "x" and not xor(char,char)):
      flag = base64.b16encode(flag)
      throw_stdout_for_dog = throw_stdout_for_dog + "walk "
    if(char == "v" and not xor(char,char)):
      flag = flag[::-1]
      throw_stdout_for_dog = throw_stdout_for_dog + "play "
  if(dedogger):
    print("Dogeveloper Console: ")
    print(f"  [+] Encrypting new Dogger with \"%s\" "% (key))

    print(f"\t%d Doggers thrown.\n\t%d Balls Found\n\t%d Tail Per Dogger\n\tEncrypting at %d.%d Doge/s" % (random.randint(0,5),random.randint(0,5),random.randint(0,7),random.randint(0,9),1))
    print("-"*50)
  return flag
