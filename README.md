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
> 2. 반복문을 통해 2의 배수를 제거하고, 이후 3의 배수를 제거하고 마지막으로 5의 배수까지 제거한다. 이 때 2*3 과 3*2 는 대칭이므로, 6의 배수로 넘어갈 필요가 없다.  
>    **[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]**  
>    **[1,2,3,5,7,9,11,13,15,17,19,21,23,25]**  
>    **[1,2,3,5,7,11,13,17,19,23,25]**  
>    **[1,2,3,5,7,11,13,17,19,23]**

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
  > 삽입 정렬(Insertion Sort):
- NxN Matrix - Multiplication <br>
  일반화하기.
