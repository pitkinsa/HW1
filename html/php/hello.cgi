#!/usr/bin/php
<?php
 echo "Content-type: text/html \n\n";
 function generateRandomColor(){
   $array = array( "aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow");
   return $array[array_rand($array)];
 }
$color = generateRandomColor();
 echo "<!DOCTYPE html>
        <html lang='en'>
        <head>
          <title>HW1 in PHP</title>
        </head>
        <body style='background:$color'>
          <h1>Hello World from PHP @ " .date("Y/m/d"). "</h1>
        </body>
        </html>";

