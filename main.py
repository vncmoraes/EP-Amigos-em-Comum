pares = {}
lista_amigos = {}

while True:
    nome = input()
    if nome == "--": break
    lista_amigos[nome] = []

for primeiro_nome in lista_amigos:
    for segundo_nome in lista_amigos:
        if primeiro_nome != segundo_nome:
            novo_par = sorted([primeiro_nome, segundo_nome])
            pares[novo_par[0] + " " + novo_par[1]] = []

while True:
    par = input()
    if par == "--": break
    par_ordenado = sorted(par.split())
    pares[par_ordenado[0] + " " + par_ordenado[1]] = []

    lista_amigos[par_ordenado[0]].append(par_ordenado[1])
    lista_amigos[par_ordenado[1]].append(par_ordenado[0])

for p in pares.keys():
    amigos = p.split()
    for amigo in lista_amigos.keys():
        if (amigo not in amigos) and (amigos[0] in lista_amigos[amigo]) and (amigos[1] in lista_amigos[amigo]):
            pares[p].append(amigo)

for p in sorted(pares.keys()):
    amigos_comum = " " + ", ".join(sorted(pares[p]))
    if amigos_comum == " ": amigos_comum = ""
    print(p + " :" + amigos_comum)



