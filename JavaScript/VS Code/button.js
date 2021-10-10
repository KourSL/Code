function showAlert(){
    alert("Hey moona!");
}
function secondFunction(event){
    alert("Yo! pekora Shacho")
    alert(`Coordinate: ${event.clientX} - ${event.clientY}`);
}


let btn = document.getElementById("myButton");
btn.addEventListener("click", showAlert);
btn.addEventListener("click", secondFunction);