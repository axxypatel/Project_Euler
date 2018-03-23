# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
limit = 1000


def brute_force_approach():
    all_numb = {}
    max_pair = 0

    def is_right_angle_pair(first, second, third):
        tri_status = False
        temp_pair = [first, second, third]
        for j in range(0, 3):
            if j < 2:
                if temp_pair[j] ** 2 == temp_pair[j+1] ** 2 + temp_pair[j-1] ** 2:
                    tri_status = True
                    break
            else:
                if temp_pair[j] ** 2 == temp_pair[j-1] ** 2 + temp_pair[j-2] ** 2:
                    tri_status = True
                    break
        return tri_status

    for temp in range(limit, 10, -2):
        total_pair = 0
        a = int(temp/2)
        while a > 0:
            b = a - 1
            while b > 0:
                c = temp - a - b
                if is_right_angle_pair(a, b, c) and a > b > c:
                    total_pair += 1
                    break
                b -= 1
            a -= 1
        if total_pair >= max_pair:
            max_pair = total_pair
            all_numb[temp] = total_pair

    print(all_numb)


def arithmetic_approach():
    parameter = 0
    total_pair = 0
    for p in range(limit, 1, -2):
        total_cnt1 = 0
        for a in range(2, int(p/3)):
            b = int((p * (p - 2*a)) / (2 * (p - a)))
            if(p * (p - 2*a)) % (2 * (p - a)) == 0 and a < b:
                total_cnt1 += 1
        if total_cnt1 > total_pair:
            total_pair = total_cnt1
            parameter = p
    print("Parameter with highest pair:", parameter, total_pair)


brute_force_approach()
arithmetic_approach()
