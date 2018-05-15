Level Info: "Welcome to Krypton! The first level is easy. The following string encodes the password using Base64:

S1JZUFRPTklTR1JFQVQ=

Use this password to log in to krypton.labs.overthewire.org with username krypton1 using SSH on port 2222. You can find the files for other levels in /krypton/"

For this, I just opened a python shell and ran

```python
import base64
base64.b64decode('S1JZUFRPTklTR1JFQVQ=')
```

which returns 'KRYPTONISGREAT' as the password.

Password: KRYPTONISGREAT
