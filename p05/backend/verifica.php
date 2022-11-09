<?php
$id1 = $_GET['card1'];
$id2 = $_GET['card2'];
function query($id)
{
    $curl = curl_init();

    curl_setopt_array(
        $curl,
        array(
            CURLOPT_URL => 'http://127.0.0.1:5000?card=' . $id,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_ENCODING => '',
            CURLOPT_MAXREDIRS => 10,
            CURLOPT_TIMEOUT => 0,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
            CURLOPT_CUSTOMREQUEST => 'GET',
        )
    );

    $response = curl_exec($curl);

    curl_close($curl);
    return $response;
}

if (strcmp(query($id1), query($id2)) !== 0) {
    echo '';
} else {
    echo '1';
}