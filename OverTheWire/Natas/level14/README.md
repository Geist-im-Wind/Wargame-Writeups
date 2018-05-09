This time we have a username and password field to deal with. In looking at the source code, we can see that there isn't much to it.

```php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas14', '<censored>');
    mysql_select_db('natas14', $link);

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if(mysql_num_rows(mysql_query($query, $link)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysql_close($link);
}
```

Upon a username being submitted, it opens up a local mysql database connection, then selects a database from it. If a debug flag is in the initial array key, it executes a query for users that where the username and password are matching. Then, it determines whether any matching users were found, and, if they were, gives the password.

Well, we can set the username, password, and debug flag by simply doing `http://natas14.natas.labs.overthewire.org/?username=a&password=b&debug`. This gets us a page where the query being executed is read out to us, but access is still denied.

It looks like my best bet is looking into MySQL injection. From what I know of other injection types, my first bet is to utilize commenting to somehow change what is being executed.

Looking into the OWASP injection methods, I found the method the "1=1" method.

My initial attempt resulted in this query:
` Executing query: SELECT * from users where username="1" = "1" and password="1' = "1"`, but this was giving errors.

After playing around with it a bit, I got the username to equate to true with `username ="1" = '1"`. This left only the password to figure out.

After doing a whole bunch of research into MySQL, I realized that an or operator would allow me to have an incorrect expression to take the " given by the code and give me free reign over what the what was on the other end of the or operator.

I finally ended up with ` Executing query: SELECT * from users where username="1" = '1" and password="1' or '1' = "1"`, which equates to `Executing query: SELECT * from users where username=true and password=true`, since `'1' = "1"` and `"1" = '1"`.

Password: AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
