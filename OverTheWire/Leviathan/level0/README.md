None of the levels will come with any info. Well, guess we just jump into it.

Running `ls -la` shows me a ".backup" folder owned by leviathan1. Looks promising. Inside is a "bookmarks.html" file, which is quite difficult to parse by just reading it.

For that reason, I did a simple `grep pass` on it, which returned a line containing the password.

```html
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

Password: rioGegei8m
