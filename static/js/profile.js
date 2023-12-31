document.addEventListener('DOMContentLoaded', ()=>{

    const switchBtn = document.querySelectorAll('.switch-btn span')
    const infoCard = document.querySelectorAll('.info-card')
    const profileEditBtn = document.querySelector('.profile-edit')
    const profileEditcard = document.querySelector('.personal-info-edit')
    switchBtn.forEach((button, index) => {
        button.addEventListener('click', () => {
            profileEditcard.classList.add('d-none')
            // Barcha elementlarni yopish ("d-none" qo'shish)
            infoCard.forEach(element => {
                element.classList.add('d-none');
            });
            switchBtn.forEach(element => {
                element.classList.remove('text-warning');
            });
            // Faqat tanlangan elementni ochish ("d-block" qo'shish)
            infoCard[index].classList.remove('d-none');
            switchBtn[index].classList.add('text-warning');
        });
    });

    if(profileEditBtn){
        profileEditBtn.addEventListener('click', ()=>{
            profileEditcard.classList.remove('d-none')
            infoCard.forEach(element => {
                element.classList.add('d-none');
            });
        })
    }


    // delete blog
    const deleteBtn = document.querySelectorAll('.delete_btn')
    const deleteMenu = document.querySelectorAll('.delete_info')
    const closeBtn = document.querySelectorAll('.exit_btn')
    deleteBtn.forEach((button, index) => {
        button.addEventListener('click', () => {
            deleteMenu[index].classList.remove('d-none')
            button.classList.add('d-none')
        });
    });
    closeBtn.forEach((button, index) => {
        button.addEventListener('click', () => {
            deleteMenu[index].classList.add('d-none')
            deleteBtn[index].classList.remove('d-none')
        });
    });

})