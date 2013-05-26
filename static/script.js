

function post(){

    // Here is the data we sill send
    var data = {"value": "HURRAY IT WORKED!!"}
    var body = JSON.stringify(data);

    // this is basic version of ajax object, if using IE, you'll have to do some other stuff
    var url = "/poster"
    var xhr = new XMLHttpRequest();

    xhr.open('post', url, true)
    xhr.onreadystatechange=function() {
        if (xhr.readyState==4 && xhr.status==200){
            var response = JSON.parse(xhr.responseText)
            console.log(response);

            // Notice how the json object was set up orignally - "response" is the object
            document.getElementById('originalMessage').textContent = response.value
            document.getElementById('response').textContent = response.serverMessage;
        }
    }

    xhr.setRequestHeader("Content-type","application/json");
    xhr.send(body);
}

