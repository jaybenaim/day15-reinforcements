def draw_shape(options):
    shape = ""

    for r in range(options['rows']):
        for c in range(options['cols']):
            shape += options['char']

        shape += "\n"


    return shape


star_grid = {
'rows':4,
'cols':4, 
'char': '*'
}

print(draw_shape(star_grid))

zero_grid = {
'rows':3,
'cols':9, 
'char': '0'
}

print(draw_shape(zero_grid))