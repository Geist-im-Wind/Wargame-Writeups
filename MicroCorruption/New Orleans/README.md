Well, we've finished the tutorial. Now, on to get that $$$ from New Orleans.

To start with, I'll run through the program to see what it's doing. Afterwards, I'll take any functions that have names that intrigue me and analyze those more closely.

It seems to have a similar input to the tutorial, with the option to type in a hex encoded entry. After causing a breakpoint at main, the <create_password> function caught my attention. If they are creating the password in memory for us beforehand, we may simply be able to input their created password to bypass security.

Sure enough, they explicitly write the hex characters being written to memory to later check against for the inputted password. Specifically, they use `39 75 30 6b 29 50 45`, followed by a null byte. If you just input the hex inputs into the password checker, you're in.
