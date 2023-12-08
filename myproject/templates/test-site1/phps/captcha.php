<?php
session_start();

$width = 120;
$height = 40;

$image = imagecreatetruecolor($width, $height);

$white = imagecolorallocate($image, 255, 255, 255);
$black = imagecolorallocate($image, 0, 0, 0);

imagefilledrectangle($image, 0, 0, $width, $height, $white);

$characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
$length = strlen($characters);
$randomString = '';

for ($i = 0; $i < 6; $i++) {
    $randomString .= $characters[rand(0, $length - 1)];
}

$_SESSION['captcha_code'] = $randomString;

$font = 'path/to/your/font.ttf'; // 替换成你的字体文件路径

imagettftext($image, 20, 5, 15, 30, $black, $font, $randomString);

header('Content-Type: image/png');
imagepng($image);
imagedestroy($image);
?>
