const input =
document.getElementById(
"message"
);

input.addEventListener(
"keypress",
function(e){

if(e.key==="Enter")
sendMessage();

});

function sendMessage(){

let message=input.value;

if(message=="")
return;

let chatbox=
document.getElementById(
"chatbox"
);

chatbox.innerHTML += `

<div class="user-message">
${message}
</div>

`;

input.value="";

chatbox.innerHTML += `

<div
class="bot-message"
id="typing">

Typing...

</div>

`;

chatbox.scrollTop=
chatbox.scrollHeight;

fetch("/chat",{

method:"POST",

headers:{
"Content-Type":
"application/json"
},

body:JSON.stringify({

message:message

})

})

.then(response=>response.json())

.then(data=>{

document
.getElementById(
"typing"
)
.remove();

chatbox.innerHTML += `

<div class="bot-message">
${data.reply}
</div>

`;

chatbox.scrollTop=
chatbox.scrollHeight;

});

}