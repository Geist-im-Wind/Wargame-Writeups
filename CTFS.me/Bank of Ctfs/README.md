This one is sort of silly. You need money to buy the flag. If you open the source, you'll find:

```javascript
var flag = "";

function buy() {
var balance = document.getElementById("money").innerText;

if(balance > 9999){
    document.getElementById("go").value = balance;
    return alert(document.getElementById("go").value);
}

    return alert("Can't Buy Flag "+balance);             
}
```

This basically looks at the element with the ID of "money" and sets an actual variable to that amount. The problem with this is that anyone can edit what is inside of HTML. Simply inspecting the element and typing a bunch of zeroes after your 10 will give you enough to buy the flag. Done.
