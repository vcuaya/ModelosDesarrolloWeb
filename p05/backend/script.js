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

function devolverCarta(x,y) {
    return new Promise(resolve => {
      setTimeout(() => {
        //const je = '<img class="img-thumbnail img-fluid" src="./img/gato.png"></a>'
        /* $.ajax({
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
        }); */
        resolve(1)
        
      }, 2000);
    });
  }

async function carta2(id, id2) {
    console.log(id)
    console.log(id2)
    const siOno = await devolverCarta(id, id2);
    if(siOno==1){
        document.getElementById(id).innerHTML = '<img class="img-thumbnail img-fluid" src=./../img/200px-NAP-01_Back.png>'
        document.getElementById(id2).innerHTML = '<img class="img-thumbnail img-fluid" src=./../img/200px-NAP-01_Back.png>'
    }
    a =''
    b =''
}

var a =''
var b =''

function carta(id) {
    if(a==''|| b==''){
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
    if(a!='' && b==''){
        b = id
        console.log("entro b")
    }
    if(a==''){
        a = id
        console.log("entro a")
    }
    if(a!='' && b!=''){
        carta2(a,b)  
    }
    
}