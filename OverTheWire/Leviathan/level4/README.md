Upon first inspection, it seems like nothing is in the home folder, but after running `ls -la`, we find that there is a ".trash" folder. In it is a single program named "bin".

Running an `ltrace` on it tells us that it is running `fopen("/etc/leviathan_pass/leviathan5", "r") = 0`, which will give us the password in binary. Running it without `ltrace` gives this output:

`01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010`

which translates to the password once converted from binary.

Password: Tith4cokei
