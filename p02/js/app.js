const images = [...document.querySelectorAll('.image')];
//popup

const popup = document.querySelector('.popup');
const closeBtn  = document.querySelector('.close-btn');
const imageName  = document.querySelector('.image-name');
const largeImage  = document.querySelector('.large-image');
const imageIndex  = document.querySelector('.index');
const leftArrow  = document.querySelector('.left-arrow');
const rightArrow  = document.querySelector('.right-arrow');

let index= 0; //para saber en que imagen estamos

images.forEach((item, i) => {
    item.addEventListener('click', () => {
        updateImage(i);
        popup.classList.toggle('active');
    })
    
})
var getAllImages = document.getElementsByClassName('image');

const updateImage = (i) => {
    // let path = `${i+1}.png`;
    let path = `${getAllImages[i].getAttribute('src')}`;
    largeImage.src = path;
    imageName.innerHTML = path;
    imageIndex.innerHTML = `${getAllImages[i].getAttribute('src')}`;
    index = i;
}

closeBtn.addEventListener('click', () =>{
    popup.classList.toggle('active');
})

leftArrow.addEventListener('click', () =>{
    if(index > 0){
        updateImage(index - 1);
    }
})

rightArrow.addEventListener('click', () =>{
    if(index < images.length -1){
        updateImage(index + 1);
    }
})