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
+'<h2 align="center">Environment Variables</h2>'
+ '<script>'
+' var bgcolorlist=new Array("#DFDFFF", "#FFFFBF", "#80FF80", "#EAEAFF", "#C9FFA8", "#F7F7F7", "#FFFFFF", "#DDDD00") document.body.style.background=bgcolorlist[Math.floor(Math.random()*bgcolorlist.length)]'
+' </script>'
+'</body>'
+'<html>';


console.log(header + body);

var obj = process.env;
var a =Object.getOwnPropertyNames(obj).sort();
a.forEach(function(val, idx, array) {
  console.log('<b>' + val + ': ' + '</b>'  + obj[val]+ '<br>');
}); 
