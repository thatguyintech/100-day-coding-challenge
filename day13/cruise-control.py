def maxSpeed(horses, totalDist):
    # for n horses, find the times of all horses,
    # then get the slowest time and divide totalDist by that time
    largestTime = 0.0

    for horse in horses:
        start, speed = horse
        time = (totalDist-start)*1.0/speed

        largestTime = max(time, largestTime)

    return totalDist/largestTime

def main():
    assert maxSpeed([(2400,5)], 2525) == 101.0
    assert maxSpeed([(120, 60), (60, 90)], 300) == 100.0
    assert maxSpeed([(80,100),(70,10)], 100) == 100.0/3

if __name__ == "__main__":
    main()
