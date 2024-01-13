const menu=document.getElementById('menu')
const overlay=document.getElementById('overlay')
const link_wrapper=document.getElementById('link_wrapper')
const searchIcon=document.getElementById('searchIcon')
const search_div=document.getElementById('search_div')
const closeIcon=document.querySelector('#search_div #closeIcon')
const btn =document.querySelector('#search_div button')
const input=document.querySelector('#search_div input')



let openmenu=false


function openingMenu(){
    openmenu=true
    link_wrapper.style.width='230px'
    overlay.style.display='block'
    overlay.style.background='rgba(0,0,0,0.9)'
}

function closingMenu(){
    openmenu=false
    link_wrapper.style.width='0vw'
    overlay.style.display='none'
}
menu.addEventListener('click', function(){
    if (!openmenu) {
        openingMenu()
    }
})
overlay.addEventListener('click', function(){
    if (openmenu) {
        closingMenu()
    }
})

let openSearch=false
function showSearch(){
    openSearch=true
    search_div.style.display='flex'
    overlay.style.display='block'
    overlay.style.background='rgba(200,200,200,1)'


}
function hideSearch(){
    openSearch=false
    search_div.style.display='none'
    overlay.style.display='none'


}
searchIcon.addEventListener('click',function(){
    if (!openSearch){
        showSearch()
    }
})
closeIcon.addEventListener('click',function(){
    if (openSearch){
        hideSearch()
    }
})

h


btn.addEventListener('click',function(){
    var searchText=input.value
    console.log(searchText);
})
