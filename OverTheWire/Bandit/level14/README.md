Level Goal: "The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost."

Now, I don't know immediately how to go about doing this, but in doing even a small amount of research, I am finding that `nc` is the likely command. It allows packets to be sent to ports. I imagine if we encode the password into one of these packets, we will receive what we are looking for.

My first idea was to simply run `nc localhost 30000 <password>`. Seeing that this didn't work as intended, I realized it likely needs to be piped in. The command I used that got me the password was `echo <password> | nc localhost 30000`.

Password: BfMYroe26WYalil77FoDi9qh59eK5xNr
