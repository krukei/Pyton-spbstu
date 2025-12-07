# TODO Найдите количество книг, которое можно разместить на дискете

volume_MB = 1.44
book = [100, 50, 25, 4]

volume_B = volume_MB * 1024 * 1024
volume_book = book[0] * book[1] * book[2] * book[3]
n_book = round(volume_B / volume_book)

print("Количество книг, помещающихся на дискету:", n_book)
