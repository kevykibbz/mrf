/*insection observer API */
function observerImages()
{
    var images=document.querySelectorAll('[data-src]'),
    imgOpts={},
    observer=new IntersectionObserver((entries,observer)=>
    {
        entries.forEach((entry)=>
        {
            if(!entry.isIntersecting) return;
            const img=entry.target;
            const newUrl=img.getAttribute('data-src');
            img.src=newUrl;
            observer.unobserve(img);
        });
    },imgOpts);
  
    images.forEach((image)=>
    {
      observer.observe(image)
    });
}
$(document).ready(function ()
{  
    observerImages();
    $('#ownmenu').find('.owl-dots div:first').addClass('first');
    $('#ownmenu').find('.owl-dots div:nth-child(2)').addClass('second');
    $('#ownmenu').find('.owl-dots div:last').addClass('third');
});

$("#ownmenu").owlCarousel(
{
    margin: 20,
    nav: false,
    loop:true,
    responsiveClass: true,
    responsive:
    {
      0:
      {
        items: 1,
        nav: false
      },
      736:
      {
        items:1,
        nav: false
      },
      1000:
      {
        items:1,
        nav: false,
        loop: false
      }
    }
});

$("#awards-showcase").owlCarousel(
{
    nav: false,
    loop:true,
    responsiveClass: true,
    responsive:
    {
      0:
      {
        items: 1,
        nav: true
      },
      736:
      {
        items: 3,
        nav: true
      },
      1000:
      {
        items:3,
        nav: true,
        loop: false
      }
    }
});
$("#topshowcase").owlCarousel(
{
    nav: false,
    loop:false,
    responsiveClass: true,
    responsive:
    {
      0:
      {
        items: 1,
        nav: false
      },
      736:
      {
        items: 1,
        nav: false
      },
      1000:
      {
        items:1,
        nav: false,
        loop: false
      }
    }
});