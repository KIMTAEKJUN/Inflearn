# 강의 내용 정리

### 19. 변수 & 상수
> JavaScript 변수 정의
> ```JS
> // A "data container" / "data > storage"
> let userName = 'Max';
> 
> // where the value can change!
> userName = 'Menu';
> ```

<br>

> JavaScript 상수 정의
> ```JS
> // A "data container" / "data > storage"
> const totalUsers = 15;
> 
> // where the value must not change!
> totalUsers = 20;
> ```
> **let**으로 생성한 변수는 변할 수 있고, **const**로 생성한 변수는 변할 수 없다.  
> **상수**를 최대한 사용하는 게 좋다.  
> 다른 사람이 여러분의 코드를 쉽게 이해할 수 있도록 해줍니다.

<br><br>

### 20. 변수 선언 & 정의
> 허용되는 이름
> ```JS
> // Best Practice : camelCase
> let userName
> 
> // Only letters and digits
> let ageGroup5
>
> // Starting with $ is allowed
> let $kindOfSpecial
>
> // Starting with _ is allowed
> let _internalValue
> ```
> 변수 이름 내에서의 대소문자 구분이 굉장히 중요하다는 점,  
> 변수 이름에는 어떤 글자나 숫자도 사용이 가능하다.

<br>

> 허용되지 않는 이름
> ```JS
> // Allowed but bad practice!
> let user_name
>
> // Starting digits not allowed
> let 21Players
>
> // No special characters!
> let user-b
>
> // Keywords not allowed
> let let
> ```
> 변수와 상수의 이름은 숫자로 시작해선 안되고,  
> 변수 이름의 어느 위치에든 $와 _를 사용할 수 있지만,   
> 그 외의 모든 특수 문자는 어느 위치에서든 사용이 불가능합니다.  
> let과 const 같은 키워드들을 이름으로 사용하는 것 또한 허용되지 않습니다.

<br><br>

### 21. 변수 & 연산자
> Operators  
> ```JS
> // Add two numbers
> +
>
> // Subtract two numbers
> -
>
> // Multiply two numbers
> *
>
> // Divide two numbers
> / 
>
> // Divide two numbers, yield remainder
> %
>
> // Exponentiation (2 ** 3 = 8)
> **
>
> // Assign value to variable
> =


<br><br>

### 23. 자료형: 숫자 & 문자열(텍스트)
> Data Types
> ```JS
> // 2, -3, 22.956
> // Important for calculations and code where you need to "work with a numbers"
> Numbers
>
> // 'Hi', "Hi", `Hi`
> // Important for outputting results, gathering input
> Strings (Text)
> ```

<br><br>

### 26. 함수
> Functions
> ```JS
> // (1) Define Function
> // You can (but don't have to) use parameters (name) and you can (but don't have to) return values (via return)
> function greetUser(name) {
>     alert('Hi' + name);
> }
> ```

<br>

> ```JS
> // (2) Call Function
> // As often as you want, passing in (different) parameters values!
> // Every function execution then runs independent from (possible) other executions.
> greetUser('Max');
> ```
> 함수를 이용함으로써, 훨씬 더 융통적인 작업이 가능하다는 게 가장 큰 장점이다.

<br><br>

### 28. 코드 스타일, 컨벤션 & 구문
> 올바른 코드의 작성(예: 구문 오류 방지)과 올바른 형식의 읽기 쉬운 코드의 
> 작성에는 차이가 있습니다.
>
> 다음은 구문 오류 예시입니다.
> ```JS
> function greetUser {
>   alert('Hi there!');
> }
> ```
> 문제가 무엇일까요?
>
> 이 함수는 매개변수 목록 (즉 ())이 없습니다. 
> 아래와 같이 변경되어야 합니다.
> ```JS
> function greetUser() {
>   alert('Hi there!');
> }
> ```
>이 강의 과정을 통해 올바른 구문을 배우시게 됩니다 - 함수를 정의하는 방법, 변수를 선언하는 방법 등을 알려 드립니다. 하지만 당연히 읽기 쉬운 코드도 작성하려 노력하고 있죠.
>
>아래의 예시를 살펴보겠습니다:
>
> ```JS
> function greetUser() {alert('Hi there!');}
> ```
> 이 코드 스니펫은 유효합니다!
> 
> 공백, 줄 바꿈과 들여쓰기는 모두 선택 사항입니다! 필수가 아닙니다!
>
>하지만 당연히 아래의 코드가 더 읽기 쉽겠죠.
> ```JS
> function greetUser() {
>  alert('Hi there!');
> } 
> ```
>변수 정의도 마찬가지입니다.
> ```JS
> let userName='Max';
> ```
> 는 유효한 코드입니다. 그리고 물론 읽을 수도 있죠.
>
> 하지만
> ```JS
>let userName = 'Max';
> ```
>가 더 읽기 쉽습니다 - 변수 이름의 끝과 값이 시작되는 위치가 어딘지 더 쉽게 알 수 있죠.
>
> 따라서 일반적으로 구문 오류를 생성하지 않는 한 공백, 줄 바꿈 및 들여쓰기 추가는 선택 사항입니다. 예를 들어 functiongreet(){}는 function 키워드가 더 이상 식별 되지 않으므로 잘못된 코드입니다.
>
>또한 여러 줄에 걸쳐 긴 표현식을 구조화하여 더 읽기 쉽게 만들 수도 있습니다. 예를 들면 다음과 같습니다.
> ```JS
>let someResult = 5 + 10 - 3 + 22 - 10000 + 5.344 * 1200;
> ```
> 는 아래와 같이 재작성될 수 있습니다.
> ```JS
> let someResult = 5 + 10 - 3 +  
>                 22 - 10000 + 5.344 * 
>                 1200;
> ```
> 긴 문자열 연결도 마찬가지입니다.
> ```JS
> let someLongString = 'Hi, this is going to be a bit > longer, ' +
>                    'so maybe split it across multiple lines by ' +
>                     'concatenating multiple strings!';
> ```
> 다음은 유효하지 않아 구문 오류가 뜰 겁니다.
> ```JS
> let someLongString = 'Hi, this is going to be a bit longer, 
>                       so maybe split it across multiple lines by 
>                       concatenating multiple strings!';
> ```
그 이유는 무엇일까요? JavaScript는 첫 번째 줄 문자열의 끝을 찾을 수 없고 - 다른 줄에서는 찾지 않기 때문입니다. 문자열은 항상 한 줄에 있어야 합니다. (또는 여러 문자열로 분할되어 +을 통해 연결되어야 합니다).

세미콜론은 어떨까요?

일반적으로 작성한 모든 표현식 뒤에 배치해야 합니다. 예외는 {} 을 사용하는 함수와 비슷한 코드 스니펫입니다(이 규칙의 예외: 객체!).

함수 뒤에 세미콜론을 추가하는 것에는 문제가 없으며, 오류가 발생하지 않습니다. 그러나 함수에는 세미콜론을 추가하지 않는 것이 일반적입니다.