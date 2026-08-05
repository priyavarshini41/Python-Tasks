document
.getElementById("fileInput")

.addEventListener(
"change",

function(){

let file=this.files[0];

document
.getElementById("preview")
.innerHTML=

"Selected File: "+file.name;

}
)