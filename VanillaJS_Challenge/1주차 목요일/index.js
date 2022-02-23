// mouseenter, mouseleave, resize, contextmenu
const h2 = document.querySelector("h2"); // h2 가져오기
const colors = ["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"]; // // 색깔코드를 저장할 수 있는 배열 선언

const superEventHandler = {
    handleMouseEnter: function () {
        h2.innerText = "The mouse is here!"; // 함수 실행시킬 시 "The mouse is here!"을 넣음
        h2.style.color = colors[0]; // 색깔은 colors 배열에 첫번째
    },
    handelMouseLeave: function () {
        h2.innerText = "The mouse is gone!"; // 함수 실행시킬 시 "The mouse is gone!"을 넣음
        h2.style.color = colors[1]; // 색깔은 colors 배열에 두번째
    },
    windowReSize: function () {
        h2.innerText = "You just resized!"; // 함수 실행시킬 시 "You just resized!"을 넣음
        h2.style.color = colors[2]; // 색깔은 colors 배열에 세번째
    },
    handleMouseRight: function () {
        h2.innerText = "That was a right back!"; // 함수 실행시킬 시 "That was a right back!"을 넣음
        h2.style.color = colors[4]; // 색깔은 colors 배열에 다섯번째
    }
};

h2.addEventListener("mouseenter", superEventHandler.handleMouseEnter); // 마우스가 h2를 클릭 시 함수 handleMouseEnter가 실행됨
h2.addEventListener("mouseleave", superEventHandler.handelMouseLeave); // 마우스가 h2를 벗어날 시 함수 handleMouseLeave가 실행됨
window.addEventListener("contextmenu", superEventHandler.handleMouseRight); // 마우스를 오른쪽 클릭할 시 함수 handleMouseRight가 실행됨
window.addEventListener("resize", superEventHandler.windowReSize); // 윈도우 창 크기를 변화시킬 시 함수 windowResize가 실행됨