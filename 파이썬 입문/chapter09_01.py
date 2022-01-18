# Chapter09-1
# 파일 읽기 및 쓰기
# 읽기 모드 -> r, 쓰기 모드 -> w, 추가 모드 -> a, 텍스트 모드 -> t, 바이너리 모드 -> b
# 상대 경로 ('../, ./'), 절대 경로 ('C:\Django\example..')

# 파일 읽기(Read)
# 예1
f = open('파이썬 입문/resource/it_news.txt', 'rt', encoding='UTF-8')

# 속성 확인
print(dir(f))

# 인코딩 확인
print(f.encoding)

# 파일 이름
print(f.name)

# 모드 확인
print(f.mode)

cts = f.read()
print(cts)
# 반드시 close
f.close()

# 예2
with open('파이썬 입문/resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예3
# read() -> 전체 읽기, read(10) -> 10Byte
# 커서가 내부적으로 동작해서 내가 마지막으로 읽은 부분을 기억하고있다.
with open('파이썬 입문/resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0, 0) # 처음으로 돌아간다
    c = f.read(20)
    print(c)

print()

# 예4
# readline -> 한 줄 씩 읽기
with open('파이썬 입문/resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# 예5
# readlines -> 전체를 읽은 후, 라인 단위로 리스트로 저장
with open('파이썬 입문/resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()

# 파일 쓰기(write)

# 예1
with open('파이썬 입문/resource/contents1.txt', 'w') as f:
    f.write('I love Python\n')

# 예2
with open('파이썬 입문/resource/contents1.txt', 'a') as f:
    f.write('I love Python2\n')

# 예3
# writelines -> 리스트 -> 파일
with open('파이썬 입문/resource/contents2.txt', 'w') as f:
    list = ['orange\n', 'apple\n', 'banana\n', 'melon\n']
    f.writelines(list)

# 예4
# 자주 사용하지않을꺼같다.
with open('파이썬 입문/resource/contents3.txt', 'w') as f:
    print('Test text write!', file=f)
    print('Test text write!', file=f)
    print('Test text write!', file=f)