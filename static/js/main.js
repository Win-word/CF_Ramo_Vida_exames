

var b1 = document.getElementById("b1");
var b2 = document.getElementById("b2");
var cp = document.getElementById("imgExame");
//alert("Pagina de Realizacao de exame!");


function changePage1(){
    //alert("pagina 1");
    cp.src = "/static/exame/imageExame11.jpg";
    b1.style.background = "#2474c3";
    b2.style.background = "white";




}

function changePage2(){
    //alert("pagina 2");
    
    cp.src = "/static/exame/imageExame22.jpg";
    b2.style.background = "#2474c3";
    b1.style.background = "white";

}



