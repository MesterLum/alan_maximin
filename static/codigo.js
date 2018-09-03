
var nodo;
var obj1;
var arr1 = [];

const URL = 'http://localhost'
const PORT = 5000

function generar() {
    var x = document.getElementById("x").value;
    var y = document.getElementById("y").value;
    x = parseInt(x) + 1;
    if (x <= 0 || y <= 0) {
        alert("Ingrese un número mayor a 0 en los campos");
    } else {
        let tabla = document.getElementById("tabla");
        let txt = "";
        for (let i = 0; i < y; i++) {
            txt += "<tr>";
            for (let m = 0; m < x; m++) {
                /*if (m=0)
                    txt += `<td><input type="text" id="${m}o${i}"></td> placeholder="Nombre"`
                else
                    txt += `<td><input type="text" id="${m}o${i}" placeholder="value"></td>`*/
                txt += `<td><input type="text" id="${m}o${i}"></td>`
                
            }
            txt += "</tr>";
        }
        tabla.innerHTML = txt;
    }
}

function printResolution(data){
    var divForTable = ''
    divForTable+= '<table class="table table-dark">'
    /*divForTable+= `
    <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
    `*/
    
    data.map(element => {
        divForTable+=`

        <tbody>
        <tr>
          <td>${element.name}</td>
        `
        element.values.forEach(value => {
            divForTable+=`
                <td>${value}</td>
            `
        })
        divForTable+='</tr>'
    })
    divForTable+='</table>'
    document.getElementById('resolucion').innerHTML = divForTable
}

function resolveProblem(data, typeProblem = 'maximin') {
    const dat = {
         data
    }
    if (typeProblem === 'optimist_pesimist')
       dat['valueP'] = Number(document.getElementById('valueP').value)
    var headers = new Headers()
    headers.append('content-type', 'application/json')
    headers.append('accept', 'application/json')
    fetch(`${URL}:${PORT}/${typeProblem}`, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(dat)
    })
    .then(data => data.json())
    .then(data => printResolution(data))
}

function resolver() {
    var data = [];
    var correct = true;
    var x = document.getElementById("x").value;
    var y = document.getElementById("y").value;
    x = parseInt(x) + 1;
    for (let i = 0; i < y; i++) {
        obj1 = document.getElementById("0o" + i).value;
        for (let m = 0; m < x; m++) {
            if (m > 0) {
                nodo = document.getElementById(m + "o" + i);
                if (!isNaN(Number(nodo.value)) && nodo.value !== ''){
                    arr1.push(Number(nodo.value));
                }else{
                    nodo.classList.add('surround')
                    correct = false
                }
            }
        }
        data.push({ 'name': obj1, 'values': arr1 });
        arr1 = [];

    }
    if (correct){
        resolveProblem(data, document.getElementById('type').value);
    }
    else
        alert('Soluciona los problemas');
}