function sendRequest() {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            reject("Request rejected due to sever error");
        }, 2000);
    });
}

async function getUserName() {
    try{
        let username = await sendRequest();
        console.log(username);
    }catch (message) {
        console.log(`Error: ${message}`)
    }
}

getUserName();