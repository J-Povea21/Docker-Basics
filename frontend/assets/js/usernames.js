const usernamesForm = document.querySelector('#usernames-form');

usernamesForm.onsubmit = e =>{
    e.preventDefault(); 

    const username = document.querySelector('#username').value;

    axios({
        method: 'post',
        url: `http://localhost:8000/bloom/users/available/`,
        data:{
            username: username,
        },
    }).then(res => {
        const status = res.data.status;
        const message = res.data.message;

        if(status)
            displaySuccess(message);
        else
            displayError(message);
    });


};

function displayError(message){
    Swal.fire({
        icon: "error",
        title: message,
        text: "This username is already taken! You can't use it :(",
      });
}

function displaySuccess(message){
    Swal.fire({
        icon: "success",
        title: message,
        text: "This username is available. You can use it :)",
      });
}