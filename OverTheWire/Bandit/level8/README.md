The level goal for this level seems as simple as the last:

"The password for the next level is stored in the file data.txt and is the only line of text that occurs only once"

My first intuition is just to run `uniq -u data.txt`, and it should return the only unique line. This didn't seem to have the intended effect, however, since it returned at least 50 lines. After looking up my problem, I realized that `uniq` will only work on a file that has been sorted. With that knowledge, I simply ran `sort data.txt | uniq -u`, which takes the results of the sorted file and redirects them to be run against `uniq -u`, which will find the sole unique line.

Password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
