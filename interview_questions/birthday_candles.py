def birthday_cake_candles(candles):
    tally = 0
    print(candles)

    candles.sort()

    print(candles)

    for i in range(len(candles)):
        if candles[i] == candles[-1]:
            tally += 1
            print(tally)

    return tally


birthday_candles = [3, 2, 1, 3]
birthday_cake_candles(birthday_candles)