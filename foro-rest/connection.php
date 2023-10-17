<?php
require_once "config.php";
function connection()
{
    try {
        $c = new PDO("mysql:host=".Config::SERVER.";dbname=".Config::DBNAME,Config::USER,Config::PASSWORD);
        $c->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $c->exec("use ".Config::DBNAME);
        return $c;
    } catch (PDOException $exception) {
        //die or exit
        exit("Error: ".$exception->getMessage());
    }
}