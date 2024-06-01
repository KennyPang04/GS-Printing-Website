window.addEventListener("scroll", function() {
    var element = document.querySelector('.scroll-element')
    var position = element.getBoundingClientRect()

    if (position.top < window.innerHeight && position.bottom >= 0) {
        element.classList.add("visible")
    } else {
        element.classList.remove("visible")
    }
})