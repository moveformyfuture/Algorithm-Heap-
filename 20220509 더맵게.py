# 1. 우선순위 queue -> import heapq, hq.heapify(list)
# 2. 정답 : cnt, 스코빌 지수를 K이상으로 만드는 최소 횟수
# 3. 스코빌지수 계산을 위해 First, Second 만들기
# 4. 스코빌지수 계산(hq.heappush)
# 5. 스코빌지수 계산될때마다 cnt+1

import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville)
    cnt = 0

    while True:
        First = hq.heappop(scoville)
        if First >= K:
            break
        if len(scoville) == 0:
            return -1
        Second = hq.heappop(scoville)
        hq.heappush(scoville, First + Second * 2)
        cnt += 1

    return cnt