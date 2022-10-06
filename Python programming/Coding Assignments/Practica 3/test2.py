sigo = {' manolo' :[' morenus' ,' saladeida' ,' sarasanchopanza'] ,
' maria' :[' tigremesi' ,' morenus' ,' inesrio'] ,
' lidia' :[' saladeida' ,' inesrio'] }

def cuantossigo(dicc):
    d = {}
    for key, values in dicc.items():
        for persona in values:
            if persona not in d:
                d[persona] = 1
            else:
                d[persona] += 1



    return d

print(cuantossigo(sigo))