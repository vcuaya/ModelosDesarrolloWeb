
    var elements = document.getElementsByClassName("img-thumbnail img-fluid");
    var bandera = 0;
   
    for (var i = 0; i < elements.length; i++) {
        elements[i].addEventListener('click', myFunction, false);
    }
    function myFunction() {
        this.removeEventListener('click', myFunction, false);
        
        if (bandera< 2) {
            bandera+=1;
            console.log("Si entro");
            document.getElementById("time").innerHTML = "Primero";
        }
        if(bandera==2){
            document.getElementById("time").innerHTML = "NO ELIJAS";
            setTimeout(myTimer, 3000);
        }
        
        console.log("bandera:",bandera);
        this.addEventListener('click', myFunction, false);
    }

    
    function myTimer() {
        document.getElementById("time").innerHTML = "YA elige";
        bandera=0;
      }
   

    
    