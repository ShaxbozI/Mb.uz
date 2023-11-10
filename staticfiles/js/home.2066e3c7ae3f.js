window.addEventListener('DOMContentLoaded', ()=>{



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


  $(".carousel_teacher").owlCarousel({
      margin: 25,
      loop: true,
      autoplay: true,
      autoplayTimeout: 4000,
      autoplayHoverPause: true,
      dots: false,
      responsive: {
        0:{
          items:1,
          nav: false
        },
        500:{
          items:2,
          nav: false
        },
        800:{
          items:3,
          nav: false
        },
        1024:{
          items:4,
          nav: false
        }
      }
  });

})