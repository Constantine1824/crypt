const btnN = document.getElementById('btn')

const modal = document.getElementById('exampleModal')

const closeBtn = document.getElementById('close')
const closeBtn2 = document.getElementById('close2')

btnN.addEventListener('click',()=> {
    modal.style.display = 'flex'
})

closeBtn.addEventListener('click',()=>{
    modal.style.display = 'none'
})
closeBtn2.addEventListener('click',()=>{
    modal.style.display = 'none'
})

function view(id) {
    const passwordField = document.getElementById(id)
    if (passwordField.type === 'password') {
        passwordField.type = 'text'
    }
    else {
        passwordField.type = 'password'
    }
}

// const popupBtn = document.getElementById("open-btn")

// console.log(popupBtn)

// var formPopup = document.getElementById("formPopup")

// popupBtn.addEventListener("click", ()=> {
//     formPopup.style.display = 'block'
// })