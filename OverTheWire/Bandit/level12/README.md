Level Goal: "The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)"

To start off, I immediately made a copy of the file in a randomly named /tmp/ directory to begin my work. Knowing that `xxd` creates a hex dump of a file from its man page, I ran `xxd -r data.txt data.tar`. This outputted the reverted hexdump into a tar file for me to extract.

I then ran `tar --extract data.tar` to extract the tar file, and it outputted a still compressed file simply named "data". I ran `file data` and found that it was a bzip compressed file. I ran `bunzip2 data`, which uncompressed it into "data.out". I ran a file command on that, found that it was a gzip file this time, renamed it to have a ".gz" suffix, and it became a "tar" file again. This time, however, I needed to run `tar xvf`, since it was a POSIX tar file. From here, I just followed the same set of commands I previously gave in response until I got the password.

Password: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
