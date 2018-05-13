Running my typical `ls -la` and finding nothing, I looked around and continued to find nothing. Looks like this is where I need to start actually using the "Level Goals" outlined on the website.

The Level Goal listed is as follows:

"The password for the next level is stored somewhere on the server and has all of the following properties:    
* owned by user bandit7
* owned by group bandit6
* 33 bytes in size"

Find immediately stands out to me as a command best to use here, as it will search from root if I tell it to, and it comes with flags for all of the above parameters. Running `find / -type f -size 33c -user bandit7 -group bandit6` seems to do what I want to do, but there are so many "Permission denied" errors that it is very difficult to know whether or not it is working. This led me to looking for ways to disable these error messages or to at least hide them.

This eventually led me to the [GNU.org page](https://www.gnu.org/software/bash/manual/bash.html#Redirections) on redirections in bash. Seeing that "2" represents the stderr, I redirected that to /dev/null/ to effectively hide the errors from my view. The final command used was `find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null`. This only had only result, located in /var/lib/dpkg/info/bandit7.password.

Password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
