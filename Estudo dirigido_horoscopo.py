# Exercício 6: Faça um programa que solicita o ano de nascimento do usuário e retorna o seu signo no horóscopo chinês.

#### Dica: Para descobrir o seu signo no horóscopo chinês, você precisará conhecer o ano do seu nascimento de acordo com o calendário chinês. O horóscopo chinês é baseado em um ciclo de 12 anos, cada ano representado por um animal do zodíaco chinês. Aqui estão os 12 animais do zodíaco chinês e os anos correspondentes:
def horoscopo():
    rato = [2020, 2008, 1996, 1984, 1972, 1960]
    boi_bufalo = [2021, 2009, 1997, 1985, 1973, 1961]
    tigre = [2010, 1998, 1986, 1974, 1962, 1950]
    coelho_gato = [2011, 1999, 1987, 1975, 1963, 1951]
    dragao = [2012, 2000, 1988, 1976, 1964, 1952]
    serpente = [2013, 2001, 1989, 1977, 1965, 1953]
    cavalo = [2014, 2002, 1990, 1978, 1966, 1954]
    cabra_ovelha = [2015, 2003, 1991, 1979, 1967, 1955]
    macaco = [2016, 2004, 1992, 1980, 1968, 1956]
    galo_galinha = [2017, 2005, 1993, 1981, 1969, 1957]
    cao = [2018, 2006, 1994, 1982, 1970, 1958]
    porco = [2019, 2007, 1995, 1983, 1971, 1959]
    
    ano_nascimento = int(input('Digite o seu ano de nascimento e descubra o seu signo baseado no horóscopo chinês: '))
    if ano_nascimento in rato:
        print('Seu Signo é rato.')
    elif ano_nascimento in boi_bufalo:
        print('Seu signo é boi ou bufalo.')
    elif ano_nascimento in tigre:
        print('Seu signo é tigre.')
    elif ano_nascimento in coelho_gato:
        print('Seu Signo é coelho ou gato')
    elif ano_nascimento in dragao:
        print('Seu Signo é DRAGÃO.')
    elif ano_nascimento in serpente:
        print('Seu Signo é SERPENTE.')
    elif ano_nascimento in cavalo:
        print('Seu Signo é VACALO.')
    elif ano_nascimento in cabra_ovelha:
        print('Seu Signo é Cabra ou Ovelha.')
    elif ano_nascimento in macaco:
        print('Seu Signo é Masqueiko.')
    elif ano_nascimento in galo_galinha:
        print('Seu Signo é Galozé ou zéGalinha.')
    elif ano_nascimento in cao:
        print('Seu Signo é Cão.')
    else:
        print('Seu signo é porco.')
horoscopo()