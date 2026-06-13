function generateCard(){

    let name =
        document.getElementById("name").value;

    let bio =
        document.getElementById("bio").value;

    let image =
        document.getElementById("image").value;

    fetch('/generate_profile',{

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            name:name,
            bio:bio,
            image:image
        })

    })
    .then(response => response.json())
    .then(data => {

        document.getElementById("profileCard")
        .innerHTML = `

        <div class="card">
            <img src="${data.image}">
            <h2>${data.name}</h2>
            <p>${data.bio}</p>
        </div>

        `;
    });
}