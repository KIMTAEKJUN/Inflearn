const body = document.querySelector("body"); // body 가져오기

function handleReSize() {
    // 윈도우 창 크기를 알 수있게 변수 선언
    let windowReSize = window.innerWidth;
    // 윈도우 창 크기를 콘솔창에 출력
    console.log(windowReSize);

    // 윈도우 창이 400보다 작으면
    if (windowReSize < 400) {
        body.classList.remove("bg1", "bg3"); // body에 있는 class .bg1, .bg3을 삭제
        body.classList.add("bg2"); // body에 class .bg2를 추가
    // 윈도우 창이 400보다 크거나 같고 동시에 윈도우 창이 800보다 작으면
    } else if (windowReSize >= 400 && windowReSize < 800) {
        body.classList.remove("bg3", "bg2"); // body에 있는 class .bg3, .bg2을 삭제
        body.classList.add("bg1"); // body에 class .bg1를 추가
    // 윈도우 창이 800보다 크거나 같으면
    } else if (windowReSize >= 800) {
        body.classList.remove("bg2", "bg1"); // body에 있는 class .bg2, .bg1을 삭제
        body.classList.add("bg3"); // body에 class .bg3를 추가
    }
}

// 윈도우 창 크기가 변하면 함수 handleReSize가 실행됨
window.addEventListener("resize", handleReSize);
