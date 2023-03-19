### <strong>Assignment</strong>

과제 정리 폴더

1. **HW-1**
   > Bubble Sort & Quick Sort

### <strong>Practice</strong>

실습 정리 폴더

#### <Strong> 3/7 - Sieve of Eratosthenes Alogirthm </Strong>

> Sieve of Eratoshenes (에라토스테네스의 체) : **소수**를 찾아내는 방법론  
> **대칭으로 인해 숫자의 제곱근**까지만 약수를 찾으면 된다.

> 예시 (25까지의 소수 찾기.)
>
> 1. 범위 설정  
>    시작 : 2 (1은 제외) & 끝 : root(25) = 5
> 2. 반복문

```python
import math

arr = [True] * 26 # 1 ~ 25 까지의 인덱스를 위해서.
for i in range(2, (int)math.sqrt(25)):
   for j in range(i, math.sqrt(25)):
      if (arr[j*i] == True):
         arr[j*i] = False # 소수가 아니다.
```

#### <Strong> 3/14 - Insertion Sort & NxN Matrix - Multiplication </Strong>

- Insertion Sort
  > 삽입 정렬(Insertion Sort) 란 :
- NxN Matrix - Multiplication <br>
  일반화하기.
