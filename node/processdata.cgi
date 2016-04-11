#!/usr/bin/node

console.log("Content-Type: text/html;charset-utf-8")
console.log("")
try {
username = oForm.elements["username"].value;
password = oForm.elements["password"].value;
magicnum1 = oForm.elements["magicnum"].value;
}
catch(err) {
   console.log("<p>There was an error with your input</p>"):
}
else {
s = "<h1>Hello " + username +"with a password of" + password +"</h1></br>";
s = s * magicnum1;
console.log(s);
}

function validString(input){
    return !(/[\\/&;]/.test(input));
}
