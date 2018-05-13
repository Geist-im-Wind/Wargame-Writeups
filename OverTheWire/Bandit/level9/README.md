This is another variant on finding the password in the given file, with a little more complexity than the previous ones. The level goal is as follows:

"The password for the next level is stored in the file data.txt in one of the few human-readable strings, beginning with several ‘=’ characters."

Knowing that I could use `strings` to get only the human-readable strings out of the file, I simply piped (`|`) a `strings` command to `grep "^="`, which matches all lines starting with '='. The full command was `strings data.txt | grep "^="`.

From there, it was easy to find the password, as it was one of the few lines and was obvious.

Password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
