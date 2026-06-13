const images = {
1:"https://images.unsplash.com/photo-1510707577719-ae7c14805e3a",
2:"https://images.unsplash.com/photo-1534778101976-62847782c213",
3:"https://images.unsplash.com/photo-1495474472287-4d71bcdd2085",
4:"https://images.unsplash.com/photo-1509042239860-f550ce710b93"
};

function loadCoffee(){

fetch('/coffees')
.then(res=>res.json())
.then(data=>{

let html='';

data.forEach(c=>{

html += `
<div class="card">

<img src="${images[c[0]]}">

<h2>${c[1]}</h2>

<h3>⭐ Votes: ${c[2]}</h3>

<button class="vote-btn"
onclick="vote(${c[0]})">
Vote
</button>

</div>
`;

});

document.getElementById(
'coffeeContainer'
).innerHTML = html;

});
}

function vote(id){

fetch(`/vote/${id}`)
.then(()=>loadCoffee());

}

loadCoffee();