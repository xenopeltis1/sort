def selection(liste):
    
    for i in range(len(liste)):
        min_idx = i
        for _ in range(i+1, len(liste)):
            if liste[min_idx] > liste[_]:
                min_idx = _
    
        liste[i], liste[min_idx] = liste[min_idx], liste[i]

    return liste

lism = [65, 51, 23, 48]
print(lism)
lims = selection(lism)
print(lism)
