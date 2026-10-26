txt_index = 'Your Ruffier Index is:'
txt_workheart = 'Cardiac performance:'
txt_nodata = 'there isnt any data for this age'
txt_res = []
txt_res.append('low. \nConsult the doctor NOW!!!')
txt_res.append('satisfactory. \nYou should really consult the doctor!')
txt_res.append('average. \nConsult the doctor if you want.')
txt_res.append('above average. \nNo need to Consult the doctor.')
txt_res.append('high. \nThe doctor should consult YOU!.')

def ruffier_index(P1, P2, P3):
    return (4 * (P1+P2+P3) - 200) / 10

def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2
    result = 21 - norm_age * 1.5
    return result

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level = level - 4
    if r_index >= level:
        return 1
    level = level - 5
    if r_index >= level:
        return 2
    level = level - 5.5
    if r_index >= level:
        return 3
    return 4

def test(P1, P2, P3, age):
    if age < 7:
        return (txt_index + '0', txt_nodata)
    else:
        ruff_index = ruffier_index(P1, P2, P3)
        result = txt_res[ruffier_result(ruff_index, neud_level(age))]
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        return res
