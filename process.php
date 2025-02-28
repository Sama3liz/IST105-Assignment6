<?php

$a = escapeshellarg($_POST['a']);
$b = escapeshellarg($_POST['b']);
$c = escapeshellarg($_POST['c']);
$d = escapeshellarg($_POST['d']);
$e = escapeshellarg($_POST['e']);

$command = escapeshellcmd("python3 data_management.py $a $b $c $d $e");
$output = shell_exec($command);

echo "<h2>Assignment 6:</h2>";
echo "<p>" $output, "</p>";


?>
