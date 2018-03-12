var startScriptInput = document.getElementById('newStartScript');
var addStartScriptButton = document.getElementById('addStartScriptButton');
var scriptList = document.getElementById('startScripts');

var addScript = function () {
    var text = startScriptInput.value;
    var li = document.createElement('li');
    li.innerHTML = "<input type='checkbox'>" +
                   "<label>" + text + "</label>" + 
                   "<button class='delete'>Delete</button>";
    scriptList.appendChild(li);
}

addStartScriptButton.onclick = addScript;