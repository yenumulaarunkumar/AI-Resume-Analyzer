const dropArea = document.getElementById("drop-area");
const input = document.getElementById("resume");

if (dropArea) {

    dropArea.addEventListener("dragover", function(e){
        e.preventDefault();
        dropArea.classList.add("bg-light");
    });

    dropArea.addEventListener("dragleave", function(){
        dropArea.classList.remove("bg-light");
    });

    dropArea.addEventListener("drop", function(e){

        e.preventDefault();

        input.files = e.dataTransfer.files;

        dropArea.classList.remove("bg-light");

    });

}