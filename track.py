def track(distance):
    current = 0
    
    mid = distance * 4 / 5
    
    time = 0.01
    
    v = 0
    
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * time
        current += v0 * time + 1 / 2 * a * time * time
        print(current)


if __name__ == '__main__':
    track(100)
