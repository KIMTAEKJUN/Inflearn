const body = document.querySelector("body"); // body 가져오기 
const btn = document.querySelector("button"); // button 가져오기

// 색깔코드를 저장할 배열 선언
const colors = [
    "#ef5777",
    "#575fcf",
    "#4bcffa",
    "#34e7e4",
    "#0be881",
    "#f53b57",
    "#3c40c6",
    "#0fbcf9",
    "#00d8d6",
    "#05c46b",
    "#ffc048",
    "#ffdd59",
    "#ff5e57",
    "#d2dae2",
    "#485460",
    "#ffa801",
    "#ffd32a",
    "#ff3f34"
]; 

function clickBgColor() {
    // 두 개의 색깔코드를 넣을 빈배열 선언
    const randomColor = [];

    // 반복하여 색깔코드를 빈배열에 집어넣는 코드
    for (let i=0; i<2; i++) {
        randomColor.push(colors[Math.floor(Math.random() * colors.length)]); // 아까 선언한 빈배열에 색깔 넣기
        
        // 색깔이 중복되지않게 하는 코드
        for (let j=0; j<i; j++) {
            if (randomColor[i] == randomColor[j]) {
                break;
            }
        }
    }

    // 콘솔창에 출력
    console.log(randomColor); 

    // 랜덤으로 두가지 색을 섞어 그라데이션으로 색변경
    body.style.background = `linear-gradient(to right, ${randomColor})`
}

// 버튼 클릭 시 함수 clickBgColor가 실행됨
btn.addEventListener("click", clickBgColor);