Level Info: "ROT13 is a simple substitution cipher.

Substitution ciphers are a simple replacement algorithm. In this example of a substitution cipher, we will explore a ‘monoalphebetic’ cipher. Monoalphebetic means, literally, “one alphabet” and you will see why.

This level contains an old form of cipher called a ‘Caesar Cipher’. A Caesar cipher shifts the alphabet by a set number. For example:

plain:  a b c d e f g h i j k ...
cipher: G H I J K L M N O P Q ...

In this example, the letter ‘a’ in plaintext is replaced by a ‘G’ in the ciphertext so, for example, the plaintext ‘bad’ becomes ‘HGJ’ in ciphertext.

The password for level 3 is in the file krypton3. It is in 5 letter group ciphertext. It is encrypted with a Caesar Cipher. Without any further information, this cipher text may be difficult to break. You do not have direct access to the key, however you do have access to a program that will encrypt anything you wish to give it using the key. If you think logically, this is completely easy.

One shot can solve it!

Have fun."

Well, this is made way more simple with the 'encrypt' program. While I could just enter the entire alphabet for the full key, because we are made aware that it is a Caesar Cipher, I can just put in A, see how far it rotated, then apply that to every letter.

After creating a tmp directory, giving it appropriate permissions, and linking to the keyfile.dat located in /krypton/kryton2, we're ready to actually feed a file into encrypt.

I just run `echo a > file` followed by ` /krypton/krypton2/encrypt file`. This created a ciphertext file containing "M", meaning that all letters are rotated forward 12 places, since A is in position 1, and M is in position 13. Now we just have to rotate it back 12, which can be done with `tr 'A-Za-z' 'O-ZA-No-za-n'`. Running `cat /krypton/krypton2/krypton3 | tr 'A-Za-z' 'O-ZA-No-za-n'` gets us the password.

Password: CAESARISEASY
