Level Goal: "The password for the next level is stored in the file data.txt, which contains base64 encoded data"

The password for this level seemingly involves decoding a base64 encoded file. With a quick look at the manual for `base64` using `man base64`, you will find that the `-d` flag decodes a base64 encoded file. Therefore, simply running `base64 -d data.txt` gets you the text you want.

Password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
 
