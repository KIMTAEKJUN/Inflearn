# NomadCoder_VanillaJS

<br/>

> ## **노마드코더 바닐라JS 입문 (브라우저 홈 구현)**

<br/>

> #### Link
  + [𝕃𝕀ℕ𝕂](https://js-browser.netlify.app)

<br/>

> #### Preview

<br/>

![browser-img](https://user-images.githubusercontent.com/86834898/150960648-3907e14c-2a44-4627-96cc-c32400bc1ade.png)

<br/>

> ## **강의 들으면서 몰랐던거 구글링해서 메모하기**

<br/>

+ padStart 
  + 주어진 길이를 만족하는 새로운 문자열을 채움 (왼쪽부터 채움)
``` JS
.padStart(targetLength, padString) 
``` 

<br/>

+ localStorage.setItem
  + 키에 데이터 쓰기
``` JS
localStorage.setItem("key", value)
```

<br/>

+ localStorage.getItem
  + 키로 부터 데이터 읽기
``` JS
localStorage.getItem("key")
```

<br/>

+ JSON.stringify
  + JS값이나 객체를 JSON 문자열로 변환
``` JS
JSON.stringify(value)
```

<br/>

+ JSON.parse
  + JSON 문자열을 JS값이나 객체로 생성
``` JS
JSON.parse(value)
```

<br/>

+ filter
  + 모든 요소를 모아 새로운 배열로 반환
  + element : 요소값, index : 요소의 인덱스, array : 배열
``` JS
.filter(callbackFunc(element, index, array), thisArg)

// 첫번째 예시
array.filter(function(list) {
  return list.length >= 6;
})

// 두번째 예시
list.filter(list => list.length >= 6);

// 세번째 예시
function callbackFunc(list) {
  return list.length >=6;
}
array.filter(callbackFunc);
```

<br/>

+ typeof
  + 변수의 데이터 타입을 반환하는 연산자
``` JS
typeof(value)
```

<br/>

+ navigator.gelocation.getCurrentPosition
  + 장치의 현재 위치를 가져옴
``` JS
navigator.geolocation.getCurrentPosition(success, error)
```

<br/>

+ fetch
  + URL을 통해 네트워크 요청을 해주는 API (NodeJS의 API 중 하나다.)
``` JS
fetch(url)
```

<br/>

+ then
  + 비동기 처리에 사용되는 객체
  + JS의 비동기 처리 → 특정 코드의 실행이 완료될 때까지 기다리지 않고 다음 코드를 먼저 수행하는 자바스크립트의 특성
``` JS
.then((value) => {
  
})

// 예시
p.then(onFulfilled[, onRejected]);
// onFulfilled → Promise가 수행될 때 호출되는 Func, onRejected → Promise가 거부될 때 호출되는 Func

p.then((value) => {
  // 이행
  // 이행 값(fulfillment value) 하나를 인수로 받음
}, (reason) => {
  // 거부
  // 거부 이유(rejection reason) 하나를 인수로 받음
});
```

<br/>

+ toFixed
  + 소수점 자리수 지정 자르기
  + 인자명 : digits, 데이터형 : number, 설명 : 0~20까지의 정수, 생략하면 0과 같음
``` JS
.toFixed(digits)
```