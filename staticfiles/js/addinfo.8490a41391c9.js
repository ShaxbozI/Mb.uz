// HTML-dagi tugmalarni olish
const buttons = document.querySelectorAll('.open-btn');
// HTML-dagi elementlarni olish
const elements = document.querySelectorAll('.open-element');

const infoCard = document.querySelector('.info-card')
const message = document.querySelector('.message')
if(message){
    setTimeout(()=>{
        message.classList.add('d-none')
    }, 5000)
}

// Har bir tugmani eshitish qo'shish
buttons.forEach((button, index) => {
    button.addEventListener('click', () => {
        // Barcha elementlarni yopish ("d-none" qo'shish)
        infoCard.classList.add('d-none')
        elements.forEach(element => {
            element.classList.add('d-none');
            element.classList.remove('d-block');
        });
        buttons.forEach(element => {
            element.classList.add('btn-outline-primary');
            element.classList.remove('btn-primary');
        });
        // Faqat tanlangan elementni ochish ("d-block" qo'shish)
        elements[index].classList.add('d-block');
        elements[index].classList.remove('d-none');
        buttons[index].classList.add('btn-primary');
        buttons[index].classList.remove('btn-outline-primary');
    });
});
