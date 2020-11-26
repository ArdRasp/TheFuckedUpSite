let export_data = () => {
    first_name = document.getElementById('id_first_name').innerText;
    const last_name = document.getElementById("id_last_name").innerText;
    const email = document.getElementById("id_email").innerText;
    const gender = document.getElementById("select_gender").value;
    const phone_number = document.getElementById("id_phone_number").innerText;
    const country = document.getElementById("id_country").innerText;

    let form =
        'First Name: ' + first_name + '\n' +
        'Last Name: ' + last_name + '\n' +
        'E-mail: ' + email + '\n' +
        'Gender: ' + gender + '\n' +
        'Phone Number: ' + phone_number + '\n' +
        'Country: ' + country;

    const text_to_blob = new Blob([form], { type: 'text/plain' });
    let dl_link = document.createElement("a");
    dl_link.download = "I can now remember my name.txt";

    if (window.webkitURL != null)
        dl_link.href = window.webkitURL.createObjectURL(text_to_blob);
    else {
        dl_link = window.URL.createObjectURL(text_to_blob);
        dl_link.style.display = "none";
        document.body.appendChild(dl_link);
    }
    dl_link.click();
}