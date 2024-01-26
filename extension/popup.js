// (()=>{

//     chrome.runtime.onMessage.addListener((obj, sender, response) =>{
//         const {url} = obj;
//         console.log(url);
//         // if(type === "NEW"){
//         //     currentEmail = "";
//         //     console.log("New Email Loaded 🤯")
//         //     // newEmailLoaded();
//         // }
//     });
// })()


const submitbtn = document.getElementById("submitbtn")
const inputbox = document.getElementById("query")
let result_div = document.getElementById("result")
submitbtn.addEventListener("click",function(event){
    let url = ""
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        console.log(tabs[0].url);
        url = tabs[0].url;
        console.log(url)


        const data = {
            "url" : url,
            "query" : inputbox.value
        }
        console.log(data)

        fetch("http://127.0.0.1:8000/explain",{
        method : "POST",
        headers : {
            'Content-Type': 'application/json'
        },
        body : JSON.stringify(data)
        }).then(response => response.json())
        .then(data => {
            console.log(data)
            const p_tag = document.createElement("p")
            p_tag.innerText = data["output"]

            result_div.appendChild(p_tag)
        })

    });

    

    
})
