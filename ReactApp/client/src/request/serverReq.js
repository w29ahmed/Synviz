const axios = require('axios').default;

const log = console.log
export const processFile = (fileName) => {
    const data = {fileName: fileName}
    // axios({
    //     method: 'post',
    //     url: 'http://17eadbde.ngrok.io/',
    //     data: data
    //   });
    //Create our request constructor with all the parameters we need
    const request = new Request("http://17eadbde.ngrok.io/", {
        method: "post",
        body: data, // BUG?
        headers: {
            'Content-Type': 'application/json',
        },
    });
    log("created post request")
    // Send the request with fetch()
    fetch(request)
        .then(res => {
            if (res.status === 200) {
                log("success!")
            }
        })
        .catch(error => {
            log("error")
            console.log(error);
        });
};