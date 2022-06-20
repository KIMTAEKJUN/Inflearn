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

<br>

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