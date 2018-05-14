Level Goal: "There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think"

So, we have a single program that allows us to connect to a given port. If the port transmits information matching the password of the current level, we are given the password to advance.

In just testing the program with `./suconnect 20`, it appears to attempt a connection, but be refused from the port being closed. Time to bust out netcat.

Using netcat, we can set up a server to listen for connections from this program, then, when it connects, send it the password manually to unlock the next password. `tmux` helps tremendously for this, as it allows us to easily view the server and the client in a single window in the SSH session. To make a new session, type `tmux new`. From there, you can use the shortcut Ctrl + B + " to split the window into 2 vertical halves. Now we have our session ready.

First, I run `nc -l -p 10000`. This gets the listening server up and running. Next, I use the Ctrl + B + O shortcut to switch to the other pane in tmux. In that pane, I use our suconnect program to connect to the listening server I have active. With them successfully connected, I switch back to the server and paste in the password, sending it back to the client program. Having received the correct password, I am given the password for the next level.

Password: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
