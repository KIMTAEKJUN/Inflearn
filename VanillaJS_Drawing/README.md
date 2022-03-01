# NomadCoder_VanillaJS

<br/>

> ## **노마드코더 바닐라JS 입문 (그림판)**

<br/>

> #### Link
  + [𝕃𝕀ℕ𝕂]()

<br/>

> #### Preview

<br/>

> ## **강의 들으면서 몰랐던거 구글링해서 메모하기**

<br/>

+ strokeStyle
  + 도형의 윤곽선 색을 설정
``` JS
ctx.strokeStyle = "color";
```
<br/>

+ stroke
 + 윤곽선을 이용하여 도형을 그림
``` JS
ctx.stroke();
```

<br/>

+ lineWidth
  + 현재 선의 두께를 설정, 초기 설정값은 1.0 단위
``` JS
ctx.lineWidth = value;
```

<br/>

+ beginPath
  + 도형을 그리기 시작
``` JS
ctx.beginPath();
```

<br/>

+ moveTo
  + 선이 시작될 좌표를 설정
``` JS
ctx.moveTo(x, y);
```

<br/>

+ lineTo
  + 선이 끝나는 좌표를 설정
``` JS
ctx.lineTo(x, y);
```

<br/>

+ Array.from
 + 유사 배열 객체나 반복 가능한 객체를 얕게 복사해 새로운 배열 객체를 만듬
 + arrayLike : 배열로 변환하고자 하는 유사 배열 객체나 반복 가능한 객체, mapFn : 배열의 모든 요소에 대해 호출할 맵핑 함수, thisArg: mapFn 실행 시에 this로 사용할 값
``` JS
Array.from(arrayLike,[, mapFn],[, thisArg]);
```

<br/>

+ fillStyle
  + 도형을 채우는 색을 설정
``` JS
ctx.fillStyle = "color";
```

<br/>

+ fillRect
 + 색칠된 직사각형을 그림
``` JS
ctx.fillRect(x, y, width, height);
```

<br/>

+ toDataURL
 + 캔버스 영역을 Base64값으로 즉시 반환
 ``` JS
 canvas.toDataURL(type, encoderOptions);
 ```