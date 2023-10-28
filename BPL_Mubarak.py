def output(balls):
    ballCount = 0
    overCount = 0
    ign = "WND"
    cal = "0123456O"
    for j in range(0, len(balls)):
        if str(balls[j]) in cal:
            ballCount = ballCount + 1
            if ballCount >= 6:
                overCount = overCount + 1
                ballCount = 0
    if overCount > 1:
        print(f"{overCount} OVERS ", end="")
        if ballCount > 1:
            print(f"{ballCount} BALLS")
        if ballCount == 1:
            print(f"{ballCount} BALL")
    elif overCount == 1:
        print(f"{overCount} OVER ", end="")
        if ballCount > 1:
            print(f"{ballCount} BALLS")
        if ballCount == 1:
            print(f"{ballCount} BALL")
    elif overCount == 0:
        if ballCount > 1:
            print(f"{ballCount} BALLS")
        if ballCount == 1:
            print(f"{ballCount} BALL")


num = input()
for i in range(0, num):
    balls = input()
    output(balls)
