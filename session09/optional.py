def how_often_reverse(age_difference):
    a = 0
    b = a + age_difference
    count_how_often = 0
    for i in range(100-age_difference):
        if str(a).zfill(2)[:1] == str(b).zfill(2)[1:] and str(b).zfill(2)[:1] == str(a).zfill(2)[1:]:
            print(f"{str(a).zfill(2)} and {str(b).zfill(2)}")
            count_how_often += 1
        a += 1
        b += 1
    return count_how_often

# print(how_often_reverse(36))

def first_match(freq):
    age_difference = 16
    for i in range(63):
        if how_often_reverse(age_difference) == freq:
            return f"Are the {freq} reversing ages if the mother had her child at age {age_difference}"
        else:
            age_difference += 1
    return f"No starting_age reverses that many times"

print(first_match(8))
# print(first_match(5)) # Fix all ages showing when have more time
# print(first_match(7))



# def how_often_all():
#     age_difference = 16
#     for i in range (63):
#         print(f"{age_difference} reverses {how_often_reverse(age_difference)} times")
#         age_difference +=1

# how_often_all()