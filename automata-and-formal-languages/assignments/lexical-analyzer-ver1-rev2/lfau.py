# Atividade - Linguagens formais e automatos

#
#
trn = {
    # AND
    ('S0', 'a'): 'S1',
    ('S1', 'n'): 'S2',
    ('S2', 'd'): 'S3',

    # ARRAY
    ('S1', 'r'): 'S4',
    ('S4', 'r'): 'S5',
    ('S5', 'a'): 'S6',
    ('S6', 'y'): 'S7',

    # BEGIN
    ('S0', 'b'): 'S8',
    ('S8', 'e'): 'S9',
    ('S9', 'g'): 'S10',
    ('S10', 'i'): 'S11',
    ('S11', 'n'): 'S12',

    # CASE
    ('S0', 'c'): 'S13',
    ('S13', 'a'): 'S14',
    ('S14', 's'): 'S15',
    ('S15', 'e'): 'S16',

    # CONST
    ('S13', 'o'): 'S17',
    ('S17', 'n'): 'S18',
    ('S18', 's'): 'S19',
    ('S19', 't'): 'S20',
    
    # DIV
    ('S0', 'd'): 'S21',
    ('S21', 'i'): 'S22',
    ('S22', 'v'): 'S23',

    # DO
    ('S21', 'o'): 'S24',

    # DOWNTO
    ('S24', 'w'): 'S25',
    ('S25', 'n'): 'S26',
    ('S26', 't'): 'S27',
    ('S27', 'o'): 'S28',

    # ELSE
    ('S0', 'e'): 'S29',
    ('S29', 'l'): 'S30',
    ('S30', 's'): 'S31',
    ('S31', 'e'): 'S32',

    # END
    ('S29', 'n'): 'S33',
    ('S33', 'd'): 'S34',

    # FILE
    ('S0', 'f'): 'S35',
    ('S35', 'i'): 'S36',
    ('S36', 'l'): 'S37',
    ('S37', 'e'): 'S38',

    # FOR
    ('S35', 'o'): 'S39',
    ('S39', 'r'): 'S40',

    # FUNCTION
    ('S35', 'u'): 'S41',
    ('S41', 'n'): 'S42',
    ('S42', 'c'): 'S43',
    ('S43', 't'): 'S44',
    ('S44', 'i'): 'S45',
    ('S45', 'o'): 'S46',
    ('S46', 'n'): 'S47',

    # GOTO
    ('S0', 'g'): 'S48',
    ('S48', 'o'): 'S49',
    ('S49', 't'): 'S50',
    ('S50', 'o'): 'S51',

    # IF
    ('S0', 'i'): 'S52',
    ('S52', 'f'): 'S53',

    # IN
    ('S52', 'n'): 'S54',

    # LABEL
    ('S0', 'l'): 'S55',
    ('S55', 'a'): 'S56',
    ('S56', 'b'): 'S57',
    ('S57', 'e'): 'S58',
    ('S58', 'l'): 'S59',

    # MOD
    ('S0', 'm'): 'S60',
    ('S60', 'o'): 'S61',
    ('S61', 'd'): 'S62',

    # NIL
    ('S0', 'n'): 'S63',
    ('S63', 'i'): 'S64',
    ('S64', 'l'): 'S65',

    # NOT
    ('S63', 'o'): 'S66',
    ('S66', 't'): 'S67',

    # OF
    ('S0', 'o'): 'S68',
    ('S68', 'f'): 'S69',

    # OR
    ('S68', 'r'): 'S70',

    # PACKED
    ('S0', 'p'): 'S71',
    ('S71', 'a'): 'S72',
    ('S72', 'c'): 'S73',
    ('S73', 'k'): 'S74',
    ('S74', 'e'): 'S75',
    ('S75', 'd'): 'S76',

    # PROCEDURE

    # PROGRAM
     
    # RECORD

    # REPEAT

    # SET

    # THEN
    
    # TO

    # TYPE

    # UNTIL

    # VAR

    # WHILE

    # WITH
}

res = {
    'S3': 'and',
    'S7': 'array',
    'S12': 'begin',
    'S16': 'case',
    'S20': 'const',
    'S23': 'div',
    'S24': 'do',
    'S28': 'downto',
    'S32': 'else',
    'S34': 'end',
    'S38': 'file',
    'S40': 'for',
    'S47': 'function',
    'S51': 'goto',
    'S53': 'if',
    'S54': 'in',
    'S59': 'label',
    'S62': 'mod',
    'S65': 'nil',
    'S67': 'not', # six seven
    'S69': 'of', # six nine
    'S70': 'or',
    'S76': 'packed',
}

class Entrada:
    valor: str
    linha: int
    classe: str

    def __init__(self, valor, linha, classe):
        self.valor = valor
        self.linha = linha
        self.classe = classe

    def __str__(self):
        return f'Linha: {self.linha} - {self.valor} | {self.classe}'


def ler_arquivo(nome_arquivo: str):
    palavras = []

    arquivo = open(nome_arquivo, "r")
    for linha in arquivo:
        p = linha.strip()
        palavras.append(p)
    arquivo.close()

    return palavras


def is_simbolo(c: str):
    if len(c) != 1:
        return False

    return (33 <= ord(c) <= 47 or
            58 <= ord(c) <= 64 or
            91 <= ord(c) <= 96 or
            123 <= ord(c) <= 126)


if __name__ == '__main__':
    print('lendo sintaxe.txt...')
    reservadas = ler_arquivo("sintaxe.txt")
    matriz = []
    linha = 1

    while True:
        inp_linha = input()

        if inp_linha == 'end':
            break

        for w in inp_linha.split():
            entrada = Entrada()
            entrada.valor = w
            entrada.linha = linha

            if w in reservadas:
                entrada.classe = 'Reservado'
            elif w.isnumeric():
                entrada.classe = 'Número'
            elif w == '=':
                entrada.classe = 'Atribuição'
            elif is_simbolo(w):
                entrada.classe = 'Símbolo'
            else:
                entrada.classe = 'Variável'

            matriz.append(entrada)

        linha += 1

    print("análise léxica: ")
    for entrada in matriz:
        print(entrada)
