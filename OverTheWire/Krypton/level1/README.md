Level Info: "The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!"

After navigating to the /krypton/krypton1/ folder and reading the krypton2 file, I realized that if it is a simple rotation, it is likely rot13. Opening a python shell, I tested it with:
```python
import codecs
print codecs.decode('YRIRY GJB CNFFJBEQ EBGGRA', 'rot_13')
```

which got me "LEVEL TWO PASSWORD ROTTEN".

Password: ROTTEN
