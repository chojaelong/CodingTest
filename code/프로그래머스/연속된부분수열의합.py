def solution(sequence, k):
    l = len(sequence)
    a_start, a_end = 1, 1000
    ml = 10e9
    answer = [a_start, a_end]
    end = 0
    interval_sum = 0
    
    for start in range(l):
        while interval_sum < k and end < l:
            interval_sum += sequence[end]
            end += 1
            
        if interval_sum == k:
            length = end - 1 - start
            if ml > length:
                ml = length
                answer = [start, end - 1]
        
        interval_sum -= sequence[start]
    
    return answer

# def solution(sequence, k):
#     length = len(sequence)
#     max_L = 10e9
#     prefix_sum = [0] * (length + 1)
#     answer = [1, 1000]
    
#     for i in range(length):
#         prefix_sum[i + 1] = prefix_sum[i] + sequence[i]
    
#     start, end = 1, 1
    
#     while start <= end and end <= length:
#         value = prefix_sum[end] - prefix_sum[start - 1]
        
#         if value == k:
#             if max_L > end - start:
#                 max_L = end - start
#                 answer = [start - 1, end - 1]
#             end += 1
#         elif value < k:
#             end += 1
#         else:
#             start += 1
            
#     return answer
            
solution([1, 1, 1, 2, 3, 4, 5], 5)