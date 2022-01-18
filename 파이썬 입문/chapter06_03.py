# chapter06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py -> Python 3.3 부터는 없어도 패캐지로 인식 -> 단, 하위 호환을 위해 작성을 추천한다.
# 절대경로 -> ..(부모 디렉토리) / .(현재 디렉토리) -> 모듈 내부에서만 사용

# 예제1
import sub.sub1.module1 # sub 파일 안에 있는 sub2에서 module1를 가져왔다.
import sub.sub2.module2 # sub 파일 안에 있는 sub2에서 module2를 가져왔다.

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # alias / 별명

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예3
from sub.sub1 import * # 왠만하면 *는 쓰지마라, 사용할 것만 가져와서 써라
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

