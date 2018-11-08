function source_line(source, idx){
    line = document.createElement("input"); // input element for source
    line.type = "checkbox";
    line.value = source;
    line.name = "sourceToDel";
    line.id = idx;

    var label = document.createElement("Label"); // label for input element
    label.htmlFor = idx;
    label.innerHTML= source;

    var div = document.createElement("div"); // capsule to return everything
    div.appendChild(label);
    div.appendChild(line);

    return div;
}

function sources_form(sources){
    var form = document.createElement("form");
    form.method = "put";
    form.action = "settings";

    var formHeader = document.createElement("input");
    formHeader.type = "hidden";
    formHeader.value = "sources";
    formHeader.name = "form-header";

    var s = document.createElement("input"); // Submit button
    s.name = "Submit";
    s.type = "submit";

    // appending parts to the form
    form.appendChild(formHeader);
    for (var i = 0; i < sources.length; i++){
        form.appendChild(source_line(sources[i], i));
    }
    form.appendChild(s);

    // form into html
    document.getElementById('body').appendChild(form);
}