Level Goal: "The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…"

In looking into each command they suggest, I found that s_client is almost certainly what we are looking for. It allows one to connect to an SSL server in much the same way as I previously connected with netcat.

In reading the manual, my initial thought was to run `echo <password> | openssl s_client -connect localhost:30001`. This gave the error referenced above, however. After this, I read the manual over again, and simply added the `ign_eof` flag to `s_client` for the password.

Password: cluFn7wTiGryunymYOu4RcffSxQluehd
