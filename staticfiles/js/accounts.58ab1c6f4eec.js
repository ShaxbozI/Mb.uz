document.addEventListener('DOMContentLoaded', ()=>{

    const loginBtn = document.querySelector('.login-btn')
    const registerBtn = document.querySelector('.register-btn')
    const login = document.querySelector('.login')
    const register = document.querySelector('.register')
    const loginMessage = document.querySelector('.message-login')
    const registerMessage = document.querySelector('.message-register')

    if(registerBtn){
        if (registerBtn.classList.contains('auto-press')){
            loginBtn.classList.remove('btn-primary')
            loginBtn.classList.add('btn-outline-primary')
            registerBtn.classList.add('btn-primary')
            registerBtn.classList.remove('btn-outline-primary')
            login.classList.add('d-none')
            register.classList.remove('d-none')
            loginMessage.classList.add('d-none')
            setTimeout(()=>{
                registerMessage.classList.add('d-none')
            }, 3000)
        } else if(! registerBtn.classList.contains('auto-press')){
            registerMessage.classList.add('d-none')
        }

        registerBtn.addEventListener('click', ()=>{
            loginBtn.classList.remove('btn-primary')
            loginBtn.classList.add('btn-outline-primary')
            registerBtn.classList.add('btn-primary')
            registerBtn.classList.remove('btn-outline-primary')
            login.classList.add('d-none')
            register.classList.remove('d-none')
        })
    }

    if(loginBtn){
        loginBtn.addEventListener('click', ()=>{
            loginBtn.classList.add('btn-primary')
            loginBtn.classList.remove('btn-outline-primary')
            registerBtn.classList.remove('btn-primary')
            registerBtn.classList.add('btn-outline-primary')
            login.classList.remove('d-none')
            register.classList.add('d-none')
        })
        
    }

    // Test passwords
    const resetConfrim = document.querySelector('.reset_confrim')
    let password1 = ''
    let password2 = ''
    if(resetConfrim){
        password1 = document.querySelector('.register #id_new_password1')
        password2 = document.querySelector('.register #id_new_password2')
    } else{
        password1 = document.querySelector('.register #id_password')
        password2 = document.querySelector('.register #id_password_2')
    }
    const registerFormBtn = document.querySelector('.register .register_form')
    const passwordMessage = document.querySelector('.register .message')

    password1.addEventListener('input', () => {
        setTimeout(()=>{
            if (password1.value === password2.value) {
                registerFormBtn.removeAttribute('disabled');
                    passwordMessage.innerHTML = `Kalit so'zlar mosligi tasdiqlandi<i class="bi bi-check-square ms-2"></i>`
                    passwordMessage.classList.add('text-secondary') 
                    passwordMessage.classList.remove('text-danger') 
            } else {
                registerFormBtn.setAttribute('disabled', 'disabled');
                    passwordMessage.innerHTML = "Kalit so'zlar bir-briga mos emas"
                    passwordMessage.classList.remove('text-secondary') 
                    passwordMessage.classList.add('text-danger')  
            }
        }, 800)
    });

    password2.addEventListener('input', () => {
        setTimeout(()=>{
            if (password1.value === password2.value) {
                registerFormBtn.removeAttribute('disabled');
                    passwordMessage.innerHTML = `Kalit so'zlar mosligi tasdiqlandi<i class="bi bi-check-square ms-2"></i>`
                    passwordMessage.classList.add('text-secondary') 
                    passwordMessage.classList.remove('text-danger') 
            } else {
                registerFormBtn.setAttribute('disabled', 'disabled');
                    passwordMessage.innerHTML = "Kalit so'zlar bir-briga mos emas"
                    passwordMessage.classList.remove('text-secondary') 
                    passwordMessage.classList.add('text-danger')  
            }
        }, 800)
    });


















})