var passwordField = document.getElementById('readonly')
var eye = document.getElementById('eye')
var btn = document.getElementById('view')
btn.addEventListener('click',()=>{
    console.log('clicked')
    if (passwordField.className === 'hidden') {
        console.log('reached here')
        passwordField.setAttribute('type','text')
        eye.classList.add('fa-eye-slash')
        passwordField.classList.add('show')
        passwordField.classList.remove('hidden')
        console.log(eye.classList)
        eye.classList.remove('fa-eye')
    }



    else {
        passwordField.setAttribute('type','password')
        passwordField.classList.add('hidden')
        passwordField.classList.remove('show')
        eye.classList.add('fa-eye')
        eye.classList.remove('fa-eye-slash')
    }
})



