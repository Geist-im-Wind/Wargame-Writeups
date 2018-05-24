NOT COMPLETE

Level Info: "Well done. You’ve moved past an easy substitution cipher.

The main weakness of a simple substitution cipher is repeated use of a simple key. In the previous exercise you were able to introduce arbitrary plaintext to expose the key. In this example, the cipher mechanism is not available to you, the attacker.

However, you have been lucky. You have intercepted more than one message. The password to the next level is found in the file ‘krypton4’. You have also found 3 other files. (found1, found2, found3)

You know the following important details:

    The message plaintexts are in English (*** very important) - They were produced from the same key (*** even better!)

Enjoy."

My initial impression was that this was another rotation cipher, but the Python program I wrote to bruteforce this showed me this was an incorrect assumption:
```python
import sys
import string

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open(sys.argv[1], "r") as f:
        encrypted = f.read().replace('\n', '')
        for i in range(1, 26):
                tr = string.maketrans(ALPHABET, ALPHABET[i:] + ALPHABET[:i])
                print str(i) + ":"
                print encrypted.translate(tr) + "\n"
```

With it mentioning that the text being in English was key, I did some research and found documentation on cryptoanalysis for simple substitution ciphers.

```python

```
