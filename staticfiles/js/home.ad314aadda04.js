

/*   up to top   */
const toTop = document.querySelector('.to-top')
window.addEventListener('scroll', ()=>{
    if(window.pageYOffset > 200){
        toTop.classList.add('active')
    } else{
        toTop.classList.remove('active')
    }
})



const tagsSelect = document.querySelector('.tags-select')
if(tagsSelect){
    tagsSelect.classList.add('row');
    tagsSelect.classList.add('row-cols-2');
    tagsSelect.classList.add('row-cols-md-3');
    tagsSelect.classList.add('g-2');
    tagsSelect.classList.add('p-2');
}
/*  teachers card   */

const leftNavigate = document.querySelector('.navigate-left')
const rightNavigate = document.querySelector('.navigate-right')
const teacherCard = document.querySelector('.teacher-card div')
let pixel = 0
// rightNavigate.addEventListener('click', ()=>{
//     pixel -= 18.6
//     if(pixel >= -18.6*8){
//         teacherCard.style.transform = `translateX(${pixel}rem)`
//     } else{
//         pixel = -18.6*7
//     }
// })
// console.log(pixel)
// leftNavigate.addEventListener('click', ()=>{
//     console.log(pixel)
//     if(pixel <= -18.6){
//         pixel += 18.6
//         teacherCard.style.transform = `translateX(${pixel}rem)`
//     }
// })


// const technologiesElement = document.querySelector('.technologies');

// window.addEventListener('scroll', () => {
//   const scrollPosition = window.pageYOffset || document.documentElement.scrollTop;

//   // Yoki yuqoridagi qator o'rniga, .technologies elementning ustida bo'lishi kerakligini aniqlang
//   const shouldStick = scrollPosition >= 100; // 50px - .technologies ustida bo'lishi kerak

//   if (shouldStick) {
//     technologiesElement.style.position = 'fixed';
//     technologiesElement.style.top = '100px';
//   } else {
//     technologiesElement.style.top = 'inherit';
//   }
// });
