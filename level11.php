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
//Amit tudunk : XOR-al kódolt sütik, amit egy a PHP-ben található loaddata függvény kódol. Van a kódban egy $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
//változó, ami az alapértéket mutatja. A jelszó akkor fog megjelenni, ha a showpassword = yes.
//PoC
//Mivel a kulcsot nem ismerjük, de van egy kódolt és egy plaintext adatunk ebből meg lehet határozni a kulcsot. Ha ez megvan akkor a megfelelő süti értéket vissza kell
//kódolni és ezeket az adatokat kell beküldeni.

$chiphertext = hex2bin("306c3b242439382d383d3f23392a6a766920276e676c2a2b28212423396c726e68282e2a2d282e6e36");
$plaintext = json_encode($defaultdata);
$leaked_key = xor_encrypt($plaintext, $chiphertext);
echo("A keresett kulcs :")."\n";
echo($leaked_key)."\n"; 
//A visszakapott eredményből látszik , hogy a kulcs az KNHL.
$keyBreaked = 'KNHL';

//echo(xor_encrypt($plaintext,$chiphertext));
$gooddata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$good_data_plain = json_encode($gooddata);
echo("A payload :")."\n";
echo($good_data_plain)."\n";
$good_cipher = xor_encrypt($good_data_plain, $keyBreaked);
echo("A payload xorozva:")."\n";
echo($good_cipher)."\n";
$cookie_data = base64_encode($good_cipher);
echo("A payload xorozva és base64-el kódolva, ezt kell beküldeni:")."\n";
echo($cookie_data)."\n";


?>