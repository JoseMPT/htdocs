<?php
require_once "connection.php";

$con = connection();
if($con)
    echo "<h1>Conexión exitosa</h1>";
else
    echo "<h2>Error de conexión</h2>";
