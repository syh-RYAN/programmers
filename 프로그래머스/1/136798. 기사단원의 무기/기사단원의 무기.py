def get_divisor_count(n):
    counts = []

    for i in range(1, n + 1):
        count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
                if j != i // j:  
                    count += 1
        counts.append(count)

    return counts

def solution(number, limit, power):
    answer = 0
    divisor_counts = get_divisor_count(number)
    
    for count in divisor_counts:
        if count > limit:
            count = power
        answer += count
        
    return answer