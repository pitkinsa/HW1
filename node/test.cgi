#!/usr/bin/node

var header ='Content-type: text/html\n\n';
var d = new Date();

var body =
'<!doctype html>'
+'<head>'
+'<title>'
+'Hello world node'
+'</title>'
+'</head>'
+'<body>'
+'<h2 style="margin-bottom:20px"> Hello World from JavaScript @ ' + d + '</h2>'
+ '<hr>' 
+'<h2 align="center">Environment Variables</h2>'
+ '<script>'
+ 'var bgcolorlist=["#DFDFFF", "#FFFFBF", "#80FF80", "#EAEAFF", "#C9FFA8", "#E8FFB3", "#ECE8D5", "#FA8072", "#DDDD00", "#D2B48C", "#FF7F50", "#F5FFFA", "#96CDCD", "#A27EAF", "#61456A", "#33659A"];'
+ 'document.body.style.background=bgcolorlist[Math.floor(Math.random()*bgcolorlist.length)];'
+ ' </script>'
+'</body>'
+'<html>';


console.log(header + body);

var obj = process.env;
var a =Object.getOwnPropertyNames(obj).sort();
a.forEach(function(val, idx, array) {
  console.log('<b>' + val + ': ' + '</b>'  + obj[val]+ '<br>');
}); 


console.log( '<!doctype html>'
+ '<hr style="margin-top:20px">'
+'<h3>Post Form</h3>'
+'<form id="postform" action="processdata.cgi" method="post">'
+'<label>Name: <input type="text" name="username"></label>'
+'<br>'
+'<label>Password: <input type="password" name="password"></label>'
+'<br>'
+'<label>Magic Number: <input type="text" name="magicnum" size="2" maxlength="2"></label>'
+'<br>'
+'<input type="hidden" name="test" value="it">'
+'<input type="submit" value="send">'
+'</form>'
+'<hr>'
+'<h3>Get Form</h3>'
+'<form id="getform" action="processdata.cgi" method="get">'
+'<label>Name: <input type="text" name="username"></label>'
+'<br>'
+'<label>Password: <input type="password" name="password"></label>'
+'<br>'
+'<label>Magic Number: <input type="text" name="magicnum" size="2" maxlength="2"></label>'
+'<br>'
+'<input type="hidden" name="test" value="it">'
+'<input type="submit" value="send">'
+'</form>'
+'</body>'
+'</html>');
