function devolverCarta(x,y) {
    return new Promise(resolve => {
      setTimeout(() => {
        $.ajax({
            url: "./backend/verifica.php",
            type: "GET",
            data: {
                card1: x,
                card2: y
            },
            success: function (response) {
                console.log('Si entro');
                console.log(response);
                if (response)
                    resolve(0)
                else
                    resolve(1)
            },
            error: function () {
                console.log('No funcionó');
            }
        });
        
      }, 2000);
    });
}

async function carta2(id, id2) {
    console.log(id)
    console.log(id2)
    const siOno = await devolverCarta(id, id2);
    if(siOno==1){
        document.getElementById(id).innerHTML = '<img class="img-thumbnail img-fluid" src="./img/200px-NAP-01_Back.png">'
        document.getElementById(id2).innerHTML = '<img class="img-thumbnail img-fluid" src="./img/200px-NAP-01_Back.png">'
    }
    a =''
    b =''
}

var a =''
var b =''

function carta(id) {
    if(a==''|| b==''){
        $.ajax({
            url: "./backend/server.php",
            type: "GET",
            data: { card: id},
            success: function (response) {
                console.log('Si entro');
                //resolve(response);
                document.getElementById(id).innerHTML = '<img class="img-thumbnail img-fluid" src=./img/'+response+'>'
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
/* $(document).ready(() => {
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
}); */
