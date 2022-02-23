const num1 = document.querySelector('.nums');
const num2 = document.querySelector('.guess');
const play = document.querySelector('.play');
const div = document.querySelector('div');
const chose = document.querySelector('#chose');
const win = document.querySelector('.win');
const lose = document.querySelector('.lose');

if(num1.value != null && num2.value != null){
    play.addEventListener('click', function(e){
        e.preventDefault();
        let random = Math.floor(Math.random() * (parseInt(num1.value) + 1));
        chose.innerText = `You chose ${num2.value}, the machine chose ${random}`
        chose.classList.remove("hidden")
        if(random == num2.value){
            win.innerText = 'You Win!';
            win.classList.remove("hidden");
            lose.classList.add("hidden");
        }else{
            lose.innerText = 'You Lost!';
            lose.classList.remove("hidden");
            win.classList.add("hidden");
        }
        
    })
}