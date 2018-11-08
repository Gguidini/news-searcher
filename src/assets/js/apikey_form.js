function api_key_form(key){
    var form = document.createElement("form");
    form.setAttribute('method',"post");
    form.setAttribute('action',"settings");

    var formHeader = document.createElement("input"); // Form header input
    formHeader.type = "hidden";
    formHeader.name = "form-header";
    formHeader.value = "apikey";

    var key_input = document.createElement("input"); // API key input
    key_input.setAttribute('type',"text");
    key_input.setAttribute('name',"apikey");
    key_input.value = key;

    var s = document.createElement("input"); // Submit button
    s.name = "Submit";
    s.type = "submit";

    // Create the form itself
    form.appendChild(formHeader);
    form.appendChild(key_input);
    form.appendChild(s);

    // Put form in html body
    document.getElementById('body').appendChild(form);
}