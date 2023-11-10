document.addEventListener('DOMContentLoaded', ()=>{

    const plusBtn = document.querySelector('.native .btn-plus'),
    btnClose = document.querySelector('.native .close-btn'),
    allLinkInput = document.querySelectorAll('.native .link-input')

    function addLinkInput (num){
        allLinkInput.forEach((e)=>{
            e.classList.add('d-none')
        })
        for (let i = 0; i < num; i++) {
            if (allLinkInput[i] && allLinkInput[i].classList) {
                allLinkInput[i].classList.remove('d-none');
            }
        }
    }

    let projectNum = 1
    addLinkInput(projectNum)
    plusBtn.addEventListener('click', ()=>{
        projectNum += 1
        if(projectNum<=10){
            addLinkInput(projectNum)
            if(projectNum>=2){
                btnClose.classList.remove('d-none')
            }
            if(projectNum==10){
                plusBtn.classList.add('d-none')
            }
        }

    })

    btnClose.addEventListener('click', ()=>{
        projectNum -= 1
        if(projectNum>=1){
            addLinkInput(projectNum)
            plusBtn.classList.remove('d-none')
            if(projectNum<2){
                btnClose.classList.add('d-none')
            }
        } else{
            projectNum = 1
        }
    })


    
})
