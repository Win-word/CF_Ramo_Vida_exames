

var b1 = document.getElementById("b1");
var b2 = document.getElementById("b2");
var cp = document.getElementById("imgExame");
alert("Pagina de Realizacao de exame!");


function changePage1(){
    
    cp.src = "/static/exame/imageExame1.jpg";
    b1.style.background = "#2474c3";
    b2.style.background = "white";

}

function changePage2(){
    
    cp.src = "/static/exame/imageExame2.jpg";
    b2.style.background = "#2474c3";
    b1.style.background = "white";

}



