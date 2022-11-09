/* $(document).ready(() => {
    $('.card').on('click', () => {
        let id = $('.card').attr('id');
        console.log(id);

        $.ajax({
            url: "./server.php",
            type: "GET",
            data: { card: id },
            success: function (response) {
                console.log('Si entro');
                console.log(response);
            },
            error: function () {
                console.log('No funcionó');
            }
        });
    });
}); */

/* function devolverCarta(x) {
    return new Promise(resolve => {
      setTimeout(() => {
        //const je = '<img class="img-thumbnail img-fluid" src="./img/gato.png"></a>'
        $.ajax({
            url: "./server.php",
            type: "GET",
            data: { card: x },
            success: function (response) {
                console.log('Si entro');
                resolve(response);
            },
            error: function () {
                console.log('No funcionó');
            }
        });
        
      }, 2000);
    });
  } */

/* async function carta(id) {
    document.getElementById(id).innerHTML = "Hiciste click";
    console.log(id)
    const a = await devolverCarta(id);
    document.getElementById(id).innerHTML = '<img class="img-thumbnail img-fluid" src=./../img/'+a+'>'
} */

async function carta(id) {
    $.ajax({
        url: "./server.php",
        type: "GET",
        data: { card: id},
        success: function (response) {
            console.log('Si entro');
            //resolve(response);
            document.getElementById(id).innerHTML = '<img class="img-thumbnail img-fluid" src=./../img/'+response+'>'
        },
        error: function () {
            console.log('No funcionó');
        }
    });
}