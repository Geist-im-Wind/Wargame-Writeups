Level Goal: "The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions"

This level features the same sort of encrypted data file as the last, but with a different type of encryption. It uses ROT13 encryption, rotating each character by 13 places to "encrypt" the data.

I knew that this would likely use the translate (`tr`) command, but I was not familiar enough with it to know exactly how to use it. Before checking the manual (`man tr`), I decided to check out the "Helpful Reading" section as usual. Unfortunately, in this reading, I found an exact Unix implementation of ROT13 using `tr`. The whole command is `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`.

This translates the normal alphabet of A-Z to an alphabet starting at N-Z, then doing A-M, which is effectively decrypting the original ROT13 encryption.

Password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
