<html>
<head></head>
<body>
<hr color=orange size=15 width=100% >

<h1 align=center>Read Page </h1>

<hr color=green size=15 >
</body>
</html>

<?php

echo "Hello ";

if(isset($_POST['sub']))
{

$name=$_POST['nm'];
echo "Welcome $name<br>";


$hob=null;
if(isset($_POST['chk1']))
$hob.=$_POST['chk1'].",";
if(isset($_POST['chk2']))
$hob.=$_POST['chk2'].",";
if(isset($_POST['chk3']))
$hob.=$_POST['chk3'].",";
if(isset($_POST['chk4']))
$hob.=$_POST['chk4'];

$hob=rtrim($hob,",");



echo "Hobbies are $hob";
}


?>