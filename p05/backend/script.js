$(document).ready(() => {
    let id1 = 0;
    // let id2 = 1;
    let id2 = 10;
    $.ajax({
        url: "./verifica.php",
        type: "GET",
        data: {
            card1: id1,
            card2: id2
        },
        success: function (response) {
            console.log('Si entro');
            console.log(response);
            if (response)
                console.log('Coinciden');
            else
                console.log('No Coinciden');
        },
        error: function () {
            console.log('No funcionó');
        }
    });
});