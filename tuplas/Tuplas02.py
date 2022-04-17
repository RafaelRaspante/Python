times = ('Corintinhas', 'Palmeiras', 'Santos', 'Gremio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Acletico', 'Botafogo', 'Acletico-PR', 'Bahia',
        'São Paulo', 'Fluminese', 'Sport Recife',
        'EC Vitoria','Coritiba', 'Avai', 'Ponte Preta',
        'Acletico-GO')
print('-=' * 80)
print(f'Lista de times{times}')
print('-=' * 80)
print(f'Os cincos primeiros sao {times[0:5]}')
print('-=' * 80)
print(f'Os quatos ultimos sao {times[16:]}')
print('-=' * 80)
print(f'times em ordem alfabetica{sorted(times)}')
print('-=' * 80)
print(f'O cruzeiro está na {times.index("Cruzeiro")}º posiçao')