<?php 
$is_open=False;
$is_open = $_GET["door"];
error_reporting(E_ALL);
$command = escapeshellcmd('sudo /var/www_scripts/trigger_gd.py');

#If we sent a valid true request
if ($is_open) {
   $output = shell_exec($command);
   echo $output;
?>
<head>
<META http-equiv="refresh" content="2;URL=index.php">

</head>
<?php
}
else {
?>
<head>
<META http-equiv="refresh" content="2;URL=index.php">

</head>
<?php
}


?>
<a href="index.php?door=True"><img src="images/gd.png" width="50%" height="50%"></a>
<br>
<p>It is <b><?php include('temp_log.out'); ?>F</b> inside.</p>
</ br>
<p>Door states:</p>
<?php include('door.log'); ?>
