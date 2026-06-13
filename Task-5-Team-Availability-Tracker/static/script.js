const avatars = {
1:"https://i.pravatar.cc/150?img=1",
2:"https://i.pravatar.cc/150?img=5",
3:"https://i.pravatar.cc/150?img=8",
4:"https://i.pravatar.cc/150?img=10"
};

function loadMembers(){

fetch('/members')
.then(res=>res.json())
.then(data=>{

let html='';

data.forEach(member=>{

let status =
member[2] == 1
? '<span class="available">🟢 Available</span>'
: '<span class="unavailable">🔴 Unavailable</span>';

html += `
<div class="card">

<img
src="${avatars[member[0]]}"
class="avatar">

<h2>${member[1]}</h2>

<p>${status}</p>

<button onclick="toggle(${member[0]})">
Change Status
</button>

</div>
`;

});

document.getElementById(
'teamContainer'
).innerHTML = html;

});
}

function toggle(id){

fetch(`/toggle/${id}`)
.then(()=>loadMembers());

}

loadMembers();