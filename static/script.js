async function sendQuestion(){

    let question = document.getElementById("question").value;

    let response = await fetch("/ask",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            question:question
        })
    });

    let data = await response.json();

    document.getElementById("response").innerHTML = data.answer;
}
