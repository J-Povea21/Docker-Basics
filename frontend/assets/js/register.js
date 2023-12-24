const registerForm = document.querySelector('#register-form');

registerForm.onsubmit = e =>{
    e.preventDefault();

    const username = document.querySelector('#username').value;
    const password = document.querySelector('#password').value;

    axios({
        method: 'post',
        url: `http://localhost:8000/bloom/users/add`,
        data: {
            username,
            password,
        },
    }).then(res =>{
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
        title: 'Error creating account',
        text: message,
      });
}

function displaySuccess(message){
    Swal.fire({
        icon: "success",
        title: message,
        text: "Your account has been created :)",
      });
}
