```
Lockitall                                            LOCKIT PRO r a.01
______________________________________________________________________

              User Manual: Lockitall LockIT Pro, rev a.01              
______________________________________________________________________


OVERVIEW

    - This is the first LockIT Pro Lock.
    - This lock is not attached to any hardware security module.


DETAILS

    The LockIT Pro a.01  is the first of a new series  of locks. It is
    controlled by a  MSP430 microcontroller, and is  the most advanced
    MCU-controlled lock available on the  market. The MSP430 is a very
    low-power device which allows the LockIT  Pro to run in almost any
    environment.

    The  LockIT  Pro   contains  a  Bluetooth  chip   allowing  it  to
    communiciate with the  LockIT Pro App, allowing the  LockIT Pro to
    be inaccessable from the exterior of the building.

    There is  no default password  on the LockIT  Pro---upon receiving
    the LockIT Pro, a new password must be set by connecting it to the
    LockIT Pro  App and  entering a password  when prompted,  and then
    restarting the LockIT Pro using the red button on the back.

    This is Hardware  Version A.  It contains  the Bluetooth connector
    built in, and one available port  to which the LockIT Pro Deadbolt
    should be connected.

    This is Software Revision 01.




(c) 2013 LOCKITALL                                            Page 1/1
```

This is the manual we have to work with. To start with, I'll run through the program to see what it's doing. Afterwards, I'll take any functions that have names that intrigue me and analyze those more closely.

It seems to have a similar input to the tutorial, with the option to type in a hex encoded entry. After causing a breakpoint at main, the <create_password> function caught my attention. If they are creating the password in memory for us beforehand, we may simply be able to input their created password to bypass security.

Sure enough, they explicitly write the hex characters being written to memory to later check against for the inputted password. Specifically, they use `39 75 30 6b 29 50 45`, followed by a null byte. If you just input the hex inputs into the password checker, you're in.
