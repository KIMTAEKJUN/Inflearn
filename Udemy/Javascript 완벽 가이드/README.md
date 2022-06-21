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
>
> // Perform calculation and re-assign result to variable
> +=, -=, *= . . .
>
> // Increment / Decrement variable value + re-assgin
> ++, --


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
> 
> // True, False
> // Important for conditional code and situations where you only have 2 options
> Booleans
>
> // { name: 'Max', age: 31}
> // Important for grouped / related data, helps you with organizing data
> Objects
>
> // [1, 3, 5]
> // Important for list data, unknown amounts of data
> Arrays

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
>이 강의 과정을 통해 올바른 구문을 배우시게 됩니다 - 함수를 정의하는 방법, 변수를 선언하는 방법 등을 알려 드립니다.  
> 하지만 당연히 읽기 쉬운 코드도 작성하려 노력하고 있죠.
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
> 하지만 당연히 아래의 코드가 더 읽기 쉽겠죠.
> ```JS
> function greetUser() {
>  alert('Hi there!');
> } 
> ```
> 변수 정의도 마찬가지입니다.
> ```JS
> let userName='Max';
> ```
> 는 유효한 코드입니다. 그리고 물론 읽을 수도 있죠.
>
> 하지만
> ```JS
>let userName = 'Max';
> ```
> 가 더 읽기 쉽습니다 - 변수 이름의 끝과 값이 시작되는 위치가 어딘지 더 쉽게 알 수 있죠.
>
> 따라서 일반적으로 구문 오류를 생성하지 않는 한 공백, 줄 바꿈 및 들여쓰기 추가는 선택 사항입니다.  
> 예를 들어 functiongreet(){}는 function 키워드가 더 이상 식별 되지 않으므로 잘못된 코드입니다.
>
>또한 여러 줄에 걸쳐 긴 표현식을 구조화하여 더 읽기 쉽게 만들 수도 있습니다. 예를 들면 다음과 같습니다.
> ```JS
>let someResult = 5 + 10 - 3 + 22 - 10000 + 5.344 * 1200;
> ```
> 는 아래와 같이 재작성될 수 있습니다.
> ```JS
> let someResult = 5 + 10 - 3 +  
>                  22 - 10000 + 5.344 * 
>                  1200;
> ```
> 긴 문자열 연결도 마찬가지입니다.
> ```JS
> let someLongString = 'Hi, this is going to be a bit longer, ' +
>                      'so maybe split it across multiple lines by ' +
>                      'concatenating multiple strings!';
> ```
> 다음은 유효하지 않아 구문 오류가 뜰 겁니다.
> ```JS
> let someLongString = 'Hi, this is going to be a bit longer, 
>                       so maybe split it across multiple lines by 
>                       concatenating multiple strings!';
> ```
> 그 이유는 무엇일까요? JavaScript는 첫 번째 줄 문자열의 끝을 찾을 수 없고 - 다른 줄에서는 찾지 않기 때문입니다.  
> 문자열은 항상 한 줄에 있어야 합니다. (또는 여러 문자열로 분할되어 +을 통해 연결되어야 합니다).
>
> 세미콜론은 어떨까요?
>
> 일반적으로 작성한 모든 표현식 뒤에 배치해야 합니다.  
> 예외는 {} 을 사용하는 함수와 비슷한 코드 스니펫입니다(이 규칙의 예외: 객체!).
>
>함수 뒤에 세미콜론을 추가하는 것에는 문제가 없으며, 오류가 발생하지 않습니다.  
> 그러나 함수에는 세미콜론을 추가하지 않는 것이 일반적입니다.

<br><br>

### 32. 그림자(Shadow) 함수
> 로컬("함수 내부") 변수와 전역 변수에 대해 배웠습니다.
>
> 다음의 코드를 실행하면 어떻게 될까요?
> ```JS
>let userName = 'Max';
> function greetUser(name) {
>  let userName = name;
>  alert(userName);
> }
> userName = 'Manu';
>greetUser('Max');
> ```
> 사실 이 코드를 실행하면 'Max'('Manu'가 아닌)라는 경고가 표시될 겁니다.
> 
> userName을 두 번 이상 사용하고 선언해서 오류가 발생한 것이라 > 생각하셨을 수도 있습니다 - 그리고 배우신 바와 같이, 이는 허용되지 않죠.
> 
> 이는 실제로 동일한 수준/동일한 범위에서는 허용되지 않습니다.
> 
> 다음의 코드도 작동하지 않을 겁니다.
> ```JS
> let userName = 'Max';
> let userName = 'Manu';
> ```
> 왜 처음 코드 스니펫은 작동을 했을까요?
> 
> 아래의 코드로
>
> 먼저 전역 변수 userName을 생성하기 때문입니다.
> ```JS
> let userName = 'Max';
> ```
> 그러나 그런 다음에는, 전역 수준에서는 이를 다시 선언하지 않습니다(허용되지 않음).
> 
> 함수 내에서만 다른 변수를 선언하죠.  
> 그러나 함수의 변수는 자체 범위를 갖기 때문에 JavaScript는 "섀도잉"이라는 작업을 수행합니다.
>
> 이 작업은 다른 범위에 새 변수를 생성합니다 - 이런 변수는 전역 변수를 덮어쓰거나 제거하지 않습니다 - 둘은 공존하죠.
>
> 그러면 greetUser 함수 내에서 userName을 참조할 때 항상 로컬 섀도우 변수를 참조합니다.  
> JavaScript는 해당 지역 변수가 존재하지 않는 경우에만 전역 변수로 폴백합니다. 

<br><br>

### 35. 간접적 & 직접적 함수 실행 - 요약
> 함수를 실행하는 데에 두 가지 방법이 있는 것으로 보여 혼란스러우실 수 있습니다.
> ```JS
> function add() {
>   something = someNum + someOtherNum;
> }
> ```
> add() vs add
>
> 왜 이러한 "두 가지 방법"이 있는지를 이해하는 것이 중요합니다!
>
> 보통, 이름으로 정의된 함수(예: add)를 호출할 때 괄호를 추가합니다. (함수가 필요한 모든 매개변수가 괄호 안에 들어가거나 위의 예시처럼 매개변수가 필요하지 않은 경우 빈 괄호를 추가합니다).
> ```JS
> => add()
> ```
> 이게 바로 코드의 함수를 실행하는 방법입니다.  
> JavaScript는 이 문장이 나올 때마다 함수의 코드를 실행합니다. 이상입니다!
>
> 하지만 가끔은, 함수를 바로 실행하고 싶지 않을 때가 있습니다. JavaScript에 미래의 어느 시점에(예: 일부 이벤트가 발생할 때) 어떤 기능이 실행되길 원할 수도 있습니다.
>
> 이 경우에 함수를 직접 호출하는 대신 JavaScript에 함수 이름을 제공합니다.
> ```JS
> => someButton.addEventListener('click', add);
> ```
>이 스니펫은 JavaScript에게 이렇게 지시합니다. "이 버튼이 클릭되면 add를 실행해.".
> ```JS
> someButton.addEventListener('click', add()); 
> ```
> 는 이 경우에는 오답이 될 겁니다.
>
> 그 이유는 무엇일까요? JavaScript는 스크립트를 분석/실행하고 이벤트 리스너를 등록하는 즉시 add를 실행하기 때문입니다 - 괄호를 추가했기 때문이죠 => 위를 참조해 주세요. "함수를 실행해!".
>
> 아래와 같이 코드의 어딘가에 add를 추가하는 것만으로는 아무 효과가 없습니다.
> ```JS
> let someVar = 5;
> add
>alert('Do something else...');
> ```
> Why?
>
>왜냐하면 함수의 이름만 있고 JavaScript에 다른 정보를 제공하지 않았기 때문입니다.  
> 그러면 JavaScript는 그 함수 이름으로 무엇을 해야 하는지 알지 못해서("클릭이 발생할 때 실행해야 하나요? 어느 정도의 시간이 지나면? 모르겠습니다...") 그리고 결과적으로 JavaScript는 이 문장을 무시하게 됩니다.

<br><br>

### 37. 숫자 & 문자열 섞기
> JavaScript에서 아래와 같이 숫자와 "텍스트 숫자"가 추가되는 예를
> ```JS
> 3 + '3' => '33'
> ```
>보셨습니다.
>
>이는 + 연산자가 문자열(정확히는 문자열 접합)을 제공하기 때문에 생길 수 있습니다.
>
> 산술 연산자 중에서 유일하게 문자열을 지원합니다. 가령 아래의 코드는 작동하지 않습니다:
> ```JS
>'hi' - 'i' => NaN
> ``
>곧 NaN 을 배우실 테지만, 여기서 가장 중요한 점은 위의 코드로는 문자열 ‘h’를 발생시킬 수 없다는 겁니다. + 만 문자열과 숫자를 모두 지원합니다.
>
> 고맙게도 JavaScript는 매우 똑똑하므로 아래의 코드를 처리할 수 있습니다.
> ```JS
> 3 * '3' => 9
> ```
> 참고. 위의 코드는 숫자를 산출합니다 (!) 문자열 '9'가 아닌 9을 산출합니다!
>
> 비슷하게 아래의 연산도 모두 작동합니다.
> ```JS
> 3 - '3' => 0
> 
> 3 / '3' => 1
> ```
> 3 + '3' 만 '33' 을 산출합니다.  
> 여기서 JavaScript가 + 연산자가 텍스트를 결합할 수 있다는 특성을 사용하여, 숫자 대신 문자열을 생성합니다.