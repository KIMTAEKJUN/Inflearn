const clock = document.querySelector("h3"); // h3 가져오기

function getTime() {
    const date1 = new Date().getTime(); // 오늘 기준 날짜 가져오기, getTime 메서드를 사용해서 밀리초의 값으로 가져온다.
    const date2 = new Date("December 25, 2021, 0:00:00").getTime(); // 크리스마스 날짜 가져오기, getTime 메서드를 사용해서 밀리초의 값으로 가져온다.
    // const date2 = new Date(2021, 11, 25) // 월은 0부터 시작하기때문에 -1 하기
    const christmas = date2 - date1; // 크리스마스까지 남은 날짜

    const day = Math.floor(christmas/(1000*60*60*24)); //일
    const hours = Math.floor((christmas/(1000*60*60))%24); //시
    const minutes = Math.floor(((christmas/1000)*60)%60); //분
    const seconds = Math.floor((christmas/1000)%60); //초

    const text = `${day}d ${hours}h ${minutes}m ${seconds}s`; // 일,시,분,초를 가져오기위해 변수 선언
    clock.innerText = text; // h3에 text 넣기
}

function init() {
    getTime(); // 함수 getTime를 실행
    setInterval(getTime, 1000); // setInterval 함수를 이용해 함수 getTime을 1초마다 실행
}

// 함수 init 실행
init();