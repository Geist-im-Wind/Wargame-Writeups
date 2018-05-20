I jumped into IO knowing no idea what it was other than a wargame and that it used both radare2 and gdb. I am nowhere close to great with either, but I like a good challenge.

Opening the Readme in home, I get the following:

```
Welcome to the IO wargame
-------------------------

You have done the hard part. You've found our realm. Where you can play with
classic, and up to date vulnerabilities in software. Since many of you may be
unfamiliar with how a wargame works, the following paragraphs will explain the basics.
If you have played linux shell based wargames before you can skip to the last section,
which lists all the IO specific information.

The problems are presented to you as a series of programs. They will vary
in size from a few lines to real software. The point is usually to exploit this bug in such
a way that you can control the program's execution flow. With the aim of having it read out
the password file for the next level.

The way this works is that the programs are "SUID binaries"
(http://en.wikipedia.org/wiki/Setuid). Set-user-id programs run with the privileges of the
owner of the program. Not the user starting the program. This is also how for example the
"passwd" program on a standard unix works. You will need to hijack these elevated privileges
of the level programs and use them to read the file in /home/levelX+1/.pass. which contains
the password for that level.


How to get started
------------------

Currently you are "level1" user.
You can only access files that are owned by level1, or are accessible
by everybody. (Or accessible to one of the groups 'level1' user is in.)

  level1@io:~# cd /levels
  level1@io:/levels# ls -las level01
  8 -r-sr-x--- 1 level2 level1 7500 Nov 16  2007 level01

When you run it will ask you for a code. Which you must somehow find.
Given the correct password it will launch a new shell with level2 rights.

  level1@io:/levels$ ./level01
  Enter the 3 digit passcode to enter: [something you have to find]
  Congrats you found it, now read the password for level2 from /home/level2/.pass
  sh-4.2$ id
  uid=1001(level1) gid=1001(level1) euid=1002(level2) groups=1001(level1),1029(nosu)
                                    -----------------
                                            \_________> new privileges

as you can see, by the output of the "id" command you now have euid (effective user id)
of level2. You can now read files that belong to level2. The point is to use these privileges
to read the password file for the next level.

  level1@io:/levels$ cat /home/level2/.pass
  [BINGO YOU DID IT]

Now you have the level2 password and are able to login as level2. Disconnect the current
connection and login as level2 and use the password you just found.

At this point you may want to tell the world of your achievement. You can do so by adding your tag,
comment, or pretty much anything you want to the tags file.

  level2@io:~$ echo "<p>superleetzor was here and pwnd level1</p>" >> tags

This will then become visible online at:
  http://io.netgarage.org:84/tags/level2.html

And that's pretty much it. We allow pretty much everything in the tags files. So feel free
to be creative. Though use some common sense. Also disable javascript when you view these
files in a browser...


FAQ
---

Q: I'm very new to all this, will I be able to solve this game? Is it hard?
A: It's a staged game. The first stage which lasts about to level10 is
   relatively basic. You should be able to solve these levels regardless of
   your background, age, ... If you are willing to persevere and ask
   for a little bit of help. After that point you will have had the pleasure
   of learning the basics pretty well. The game then moves on to slightly
   more advanced levels. There is no shame in getting stuck here, and asking
   for some help or guidance. Or just leave it be for the time being.
   The io wargame has been and will continue to be stable for at least the
   foreseeable future.

Q: Is there somewhere I can write files?
A: Yes, you can write in the /tmp directory.
   However this directory is set up in such a way that you can not
   list the files that are present. This is done so you can't easily
   access the files other players are working on. You are encouraged
   to make your own subdirectory to work in. For example by issueing
   the following commands.

   mkdir /tmp/somethinghardtoguess
   cd /tmp/somethinghardtoguess

   you can now write list, store temporary files, and whatnot in this
   directory. We will periodically clear out this directory whenever
   the needs arise. This will usually be announced in the chat room.
   however it's typically a good idea to have a local backup of your
   work.

Q: Do you have a list of papers i can read for level X?
A: Typically there are some things you can read, but there is no level
   specific list. Feel free to try you luck in the chatroom with that
   question. Though independent research and figuring out what the
   problem is, is part of the game. Hence you will not always be
   provided with a say all document. IO is not a comprehensive reading
   exercise.

Q: Why can't i use su?
A: su ties up processes needlessly. To free up resources we disable su,
   and require you to reconnect.

Q: Why can't i use nano, vim, ... to edit the tags file?
A: The tags files are set to "append only",  due to something called
   ,,the editor bug'', editors tend to rewrite portions of the file at once
   instead of appending. You will have to use the append (>>) output
   redirector.

Q: I really like this readme, do you want me to translate it?
A: Sure, feel free to log on to our IRC or email it to somebody. There
   should be email addresses in the motd.

Q: I'm trying hard to learn, but any shellcode i try or test still segfaults wth?!
A: You are probably compiling the levels or your testcode manually without taking
into consideration that some sections of memory are not executable by
default. This is the current setting and we have no intention of hiding
this from the players. Most of the levels on this game have an executable stack.
There are several reasons for this. Mainly because the
workarounds to bypass certain protections are too cumbersome
to be worked into each level.
The later levels do touch on these topics.

When you want to test shellcode you can use code similar to the one
included below in order to test:

#include <sys/mman.h>
#include <string.h>
#include <stdio.h>

char sc[]= "your shellcode here";

int main(){
        void * a = mmap(0, 4096, PROT_EXEC |PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_SHARED, -1, 0);
        printf("allocated executable memory at: %p\n", a);
        ((void (*)(void)) memcpy(a, sc, sizeof(sc)))();
}


Q: Why does this document contain so many spelling errors?
A: It was written by bla.



Game specifics
--------------

- levels are in the directory /levels
- passwords are stored in the home directory for the level, in a file called .pass.
  for example /home/level2/.pass contains the password for the user "level2"
- Chat:
        There is a chatroom at our irc network irc.netgarage.org, ssl port 6697
(- forum:
        at our website http://forum.netgarage.org/ though using the chat room will
        probably help you out quicker and better. )  no longer available

- aslr is off and most levels have an executable stack
```

That was quite a lot to parse, but all in all, I think I know what I'm getting myself into.

First, I go to `/levels` and run `./level01`. Seeing that it wants a simple 3 digit code, I ended up deciding to go ahead and look into radare2. I found it easier than expected, to be honest.

Opening the executable in radare2, I ran `aaa`, then `V`, then finally another `V` to get it in graphical view. From there, I used the little I knew of assembly to find that after it was running `fscanf` to get entry from me, it was comparing the register that was put into to '0x10f', which converts from hexadecimal to decimal as 271. Password in hand, I solved the level and read the password.

Password: XNWFtWKWHhaaXoKI
