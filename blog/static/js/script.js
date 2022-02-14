// Left Heading - User Icon - Click Event
const iconUser = document.querySelector(".user-icon")
const itemUser = document.querySelector(".user-items")
iconUser.addEventListener("click", function(){
     itemUser.classList.toggle("open")
})