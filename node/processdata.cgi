#!/usr/bin/node

function main2(){
try {
var username1 = document.getElementsByName("username1")[0].value;
var password1 = document.getElementsByName("password1")[0].value;
var magicnum1 = document.getElementsByName("magicnum1")[0].value;
var username = document.getElementsByName("username")[0].value;
var password = document.getElementsByName("password")[0].value;
var magicnum = document.getElementsByName("magicnum")[0].value;
}
catch(err) {
   console.log("<p>There was an error with your input: </p>" + err);
}
var s = "<h1>Hello " + username + username1 +" with a password of " + password + password1 +"</h1></br>";
s = s * magicnum1;
//var myWindow = window.open("", "_self");
document.write("<h1>Hello " + username +" with a password of " + password+ "</h1></br>");
document.write("test");
}
 
 main2();
