function addNew() {
    let newSticker = document.createElement('div')
    newSticker.classList.add('sticker')
    let container = document.getElementById('container')
    container.appendChild(newSticker)
}