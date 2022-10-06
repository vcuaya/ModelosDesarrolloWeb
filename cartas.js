
    var elements = document.getElementsByClassName("carta");
    var bandera = 0;
   
    for (var i = 0; i < elements.length; i++) {
        elements[i].addEventListener('click', myFunction, false);
    }
    function myFunction() {
        this.removeEventListener('click', myFunction, false);
        
        if (bandera< 2) {
            bandera+=1;
            var attribute = this.getAttribute("id");
            document.getElementById("demo").innerHTML = attribute;
        }
        if(bandera==2){
            document.getElementById("demo1").innerHTML = "NO ELIJAS";
            setTimeout(myTimer, 3000);
        }
        
        console.log("bandera:",bandera);
        this.addEventListener('click', myFunction, false);
    }

    
    function myTimer() {
        document.getElementById("demo1").innerHTML = "YA elige";
        bandera=0;
      }
   

    
    