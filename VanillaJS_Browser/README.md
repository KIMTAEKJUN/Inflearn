# NomadCoder_VanillaJS

<br/>

> ## **노마드코더 바닐라JS 입문 (브라우저 홈 구현)**

<br/>

> #### Link
  + [𝕃𝕀ℕ𝕂](https://js-browser.netlify.app)

<br/>

> #### Preview

<br/>

![KakaoTalk_Photo_2022-01-25-19-16-28](https://user-images.githubusercontent.com/86834898/150960648-3907e14c-2a44-4627-96cc-c32400bc1ade.png)

<br/>

> ## **강의 들으면서 몰랐던거 구글링해서 메모하기**

<br/>

+ .padStart 
  + 주어진 길이를 만족하는 새로운 문자열을 채움 (왼쪽부터 채움)
``` JS
.padStart(targetLength, padString) 
``` 

+ localStorage.setItem
  + 키에 데이터 쓰기
``` JS
localStorage.setItem("key", value)
```

+ localStorage.getItem
  + 키로 부터 데이터 읽기
``` JS
localStorage.getItem("key")
```

+ JSON.stringify
  + JS값이나 객체를 JSON 문자열로 변환
``` JS
JSON.stringify(value)
```

+ JSON.parse
  + JSON 문자열을 JS값이나 객체로 생성
``` JS
JSON.parse(value)
```

+ .filter
  + 모든 요소를 모아 새로운 배열로 반환
    + element : 요소값, index, 요소의 인덱스, array : 사용되는 배열 객체
``` JS
.filter(callbackFunc(element, index, array), thisArg)
```

+ typeof()
  + 변수의 데이터 타입을 반환하는 연산자
``` JS
typeof
```

+ navigator.gelocation.getCurrentPosition
  + 장치의 현재 위치를 가져옴
``` JS
navigator.geolocation.getCurrentPosition(success, error)
```
> #### fetch(url) → URL을 통해 네트워크 요청을 해주는 API (NodeJS의 API 중 하나다.)
> #### .then() → 비동기 처리에 사용되는 객체 
> (JS의 비동기 처리 → 특정 코드의 실행이 완료될 때까지 기다리지 않고 다음 코드를 먼저 수행하는 자바스크립트의 특성) 출처 : [[𝕃𝕀ℕ𝕂]](https://joshua1988.github.io/web-development/javascript/promise-for-beginners/)
> #### .toFixed() → 소수점 자리수 지정 자르기