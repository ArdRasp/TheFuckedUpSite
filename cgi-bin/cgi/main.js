var first_name = document.getElementById('id_first_name').innerText;
var last_name = document.getElementById("id_last_name").innerText;
var email = document.getElementById("id_email").innerText;
var gender = document.getElementById("select_gender");
var phone_number = document.getElementById("id_phone_number").innerText;
var country = document.getElementById("id_country").innerText;

// Randomize option selection
var select = document.getElementById("select_gender");
var gender_index = Math.floor(Math.random() * 9);       // select a random number 0 - 8
var options = select.options;                           // Get all the options of the select element
select.selectedIndex = gender_index;                    //Select an option from the index choosen

let export_data = () => {
    let form =
        'First Name: ' + first_name + '\n' +
        'Last Name: ' + last_name + '\n' +
        'E-mail: ' + email + '\n' +
        'Gender: ' + gender.value + '\n' +
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