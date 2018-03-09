# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?
total_pence = 200


def brute_force_approach(total_pence1):
    cnt = 0
    for a in range(total_pence1, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                cnt += 1
    print("Total number of ways:", cnt)


def compact_approach(total_pence1):
    coin_size = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (total_pence1+1)
    ways[0] = 1

    for i in range(len(coin_size)):
        for j in range(coin_size[i], total_pence1+1):
            ways[j] += ways[j-coin_size[i]]
    print("Total number of ways:", ways[len(ways)-1])


brute_force_approach(total_pence)
compact_approach(total_pence)
