#!/usr/bin/node

function main() {
console.log("Content-Type: text/html;charset-utf-8");
console.log("");
console.log("test");
try {
var username = document.getElementsByName("username")[0].value;;
var password = document.getElementsByName("password")[0].value;
var magicnum1 = oForm.elements["magicnum"].value;
}
catch(err) {
   console.log("<p>There was an error with your input: </p>" + err);
}

var s = "<h1>Hello " + username +"with a password of" + password +"</h1></br>";
//s = s * magicnum1;
console.log(s);

}

main();

function validString(input){
   return !(/[\\/&;]/.test(input));
}
