import sys
N = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
stations = list(map(int, sys.stdin.readline().split()))
current_station = stations[0]
current_roads_len = roads[0]
answer = 0
for idx in range(N-1):
    if idx == N-2:
        answer += current_station * current_roads_len
        print(answer)
        break
    if current_station > stations[idx+1]:
        answer += current_station * current_roads_len
        current_station = stations[idx+1]
        current_roads_len = roads[idx+1]
    else:
        current_roads_len+=roads[idx+1]