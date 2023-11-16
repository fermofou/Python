def MagCube(ene):
    cube = [[[0 for _ in range(ene)] for _ in range(ene)] for _ in range(ene)]

    l, r, c = 0, ene // 2, ene // 2

    for num in range(1, ene**3 + 1):
        cube[l][r][c] = num

        l = (l - 1 + ene) % ene
        c = (c - 1 + ene) % ene

        if cube[l][r][c] != 0:
            l = (l - 1 + ene) % ene
            r = (r - 1 + ene) % ene

        if cube[l][r][c] != 0:
            l = (l + 2) % ene

    return cube


print("Magic Cube!!!")
while True:
    inp = input("Da valor de n, para hacer el cuadro mágico n x n : ")
    try:
        n = int(inp)
    except ValueError:
        print("da numero impar igual o mayor a 3.")
        continue
    if n >= 3 and n % 2 == 1:
        break
    else:
        print("da numero impar igual o mayor a 3.")
cubo = MagCube(n)

for layer in cubo:
    for row in layer:
        print(row)
    print()
