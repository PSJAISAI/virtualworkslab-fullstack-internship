function getQuote(){

fetch('/quote')
.then(res=>res.json())
.then(data=>{

document.getElementById('quote')
.innerText = `"${data.quote}"`;

document.getElementById('author')
.innerText = `- ${data.author}`;

loadHistory();

});

}

function loadHistory(){

fetch('/history')
.then(res=>res.json())
.then(data=>{

let html='';

data.forEach(item=>{

html += `
<div class="history-card">
<p>${item[0]}</p>
<b>${item[1]}</b>
</div>
`;

});

document.getElementById('history')
.innerHTML = html;

});

}

loadHistory();