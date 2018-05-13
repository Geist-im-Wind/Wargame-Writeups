Seeing as the theme seems to be learning console commands, I immediately ran `ls -la` after logging in again. Finding an 'inhere' folder, I `cd` into it, and find that there are several files, one of which presumably has the password.

After opening "-file00" and "-file01", I am noticing that the files contain non-ascii characters. To save time, I run `grep -Pv "[\x80-\xFF]" ./*` to show only files with valid ascii. The -P tells grep to interpret the regex as a Perl-compatible regular expression. While I didn't know the exact regex, it took seconds on Google to find it. The regex `"[\x80-\xFF]"` is simply matching all text for which there are non-ascii characters. Running this with `-v` shows all results that do NOT match the given regex. This allowed me to find the one file with valid regex in the folder.

Password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
