
# Dynamic Programming 으로 해결할 수 있다.
def KnapSack(W, weight, val, n, memo):
    if n == 0 or W == 0 : 
        return 0, [] 
    
    if memo[n][W] != None: # 이미 계산된 경우.
        return memo[n][W], []
    
    if weight[n-1] > W: # 현재 item 을 담지 못한다면,
        memo[n][W], items = KnapSack(W, weight, val, n-1, memo) # 다음 item 으로 이동.
        

    else:
        value1, items1 = KnapSack(W - weight[n-1], weight, val, n-1, memo)
        value1 = value1 + val[n-1]

        value2, items2 = KnapSack(W, weight, val, n -1 , memo)

        # 최대값에 해당하는 item 을 선택

        if value1 > value2:
            memo[n][W] = value1
            return value1, items1 + [n-1]
        else:
            memo[n][W] = value2
            return value2, items2


# Example input
val = [60,100,120]
weight = [10,20,30]
W = 50
n = len(val)
memo = [[None]*(W + 1) for _ in range(n+1)]

# W : 담을 수 있는 최대 무게
# val : 해당 보석의 값어치 집합 
# n : 보석 갯수 = len(val)
# memo : 
print(val)
result, items = KnapSack(W, weight, val, n, memo) 
print(result, items)


# Fractional Knapsack Problem - Greedy Alogorithm 으로 해결할 수 있다.

def Fractional_knapSack(capacity, weights, values):
    items = [(values[i] / weights[i], weights[i] ,i) for i in range(len(values))]
    
    # 비율에 따라 내림차순으로 item 정렬
    
    for i in range(len(values)):
        for j in range(i, len(values)):
            if items[i][0] > items[j][0]:
                min = items[j]
                items[j] = items[i]
                items[i] = min
                

    total_value = 0
    knapsack_items = []

    for item in items:
        value_ratio, weight, index = item

        if capacity >= weight:
            total_value = total_value + (weight * value_ratio)
            capacity = capacity - weight
            knapsack_items.append((index + 1 ,1))
        
        else:
            fraction = capacity / weight
            total_value = total_value + (fraction * weight * value_ratio)
            knapsack_items.append((index + 1 , fraction))
            break
    return knapsack_items


result = Fractional_knapSack(55, weight, val)

print(result)
