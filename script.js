function saveNote() {

    let note = document.getElementById("noteInput").value;

    fetch("/add_note", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            note: note
        })
    })
    .then(response => response.json())
    .then(data => {

        document.getElementById("noteInput").value = "";

        loadNotes();
    });
}

function loadNotes() {

    fetch("/get_notes")
    .then(response => response.json())
    .then(notes => {

        let container =
            document.getElementById("notesContainer");

        container.innerHTML = "";

        notes.forEach(note => {

            container.innerHTML += `
                <div class="note">
                    ${note[1]}
                </div>
            `;
        });
    });
}

loadNotes();