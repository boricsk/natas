#!/usr/bin/php
<?php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in, $key) {
    //$key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
// meg kell nezni a json encodolas milyen eredmenyt ir ki
//echo(json_encode($defaultdata));

//próbéljuk meg kitalálni a kulcsot, iszen van XOR kódolt adatunk és tudjuk annak
//minek kell lenni (defaultdata)

$chiphertext = hex2bin("306c3b242439382d383d3f23392a6a766920276e676c2a2b28212423396c726e68282e2a2d282e6e36");
$plaintext = json_encode($defaultdata);
$keyBreaked = 'KNHL';

//echo($plaintext);
//echo($chiphertext);

//a kulcsnak ebből kell jönni, az ismétlődéseket kell keresni
//echo(xor_encrypt($plaintext,$chiphertext));
$gooddata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$good_data_plain = json_encode($gooddata);
echo($good_data_plain);
$good_cipher = xor_encrypt($good_data_plain, $keyBreaked);
//echo($good_cipher);
$cookie_data = base64_encode($good_cipher);
echo($cookie_data);


?>