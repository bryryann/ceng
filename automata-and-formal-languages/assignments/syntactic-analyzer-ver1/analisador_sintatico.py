# Atividade - Linguagens formais e automatos

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
    ('S71', 'r'): 'S77',
    ('S77', 'o'): 'S78',
    ('S78', 'c'): 'S79',
    ('S79', 'e'): 'S80',
    ('S80', 'd'): 'S81',
    ('S81', 'u'): 'S82',
    ('S82', 'r'): 'S83',
    ('S83', 'e'): 'S84',

    # PROGRAM
    ('S78', 'g'): 'S85',
    ('S85', 'r'): 'S86',
    ('S86', 'a'): 'S87',
    ('S87', 'm'): 'S88',

    # RECORD
    ('S77', 'e'): 'S89',
    ('S89', 'c'): 'S90',
    ('S90', 'o'): 'S91',
    ('S91', 'r'): 'S92',
    ('S92', 'd'): 'S93',

    # REPEAT
    ('S89', 'p'): 'S94',
    ('S94', 'e'): 'S95',
    ('S95', 'a'): 'S96',
    ('S96', 't'): 'S97',

    # SET
    ('S0', 's'): 'S98',
    ('S98', 'e'): 'S99',
    ('S99', 't'): 'S100',

    # THEN
    ('S0', 't'): 'S101',
    ('S101', 'h'): 'S102',
    ('S102', 'e'): 'S103',
    ('S103', 'n'): 'S104',

    # TO
    ('S101', 'o'): 'S105',

    # TYPE
    ('S101', 'y'): 'S106',
    ('S106', 'p'): 'S107',
    ('S107', 'e'): 'S108',

    # UNTIL
    ('S0', 'u'): 'S109',
    ('S109', 'n'): 'S110',
    ('S110', 't'): 'S111',
    ('S111', 'i'): 'S112',
    ('S112', 'l'): 'S113',

    # VAR
    ('S0', 'v'): 'S114',
    ('S114', 'a'): 'S115',
    ('S115', 'r'): 'S116',

    # WHILE
    ('S0', 'w'): 'S117',
    ('S117', 'h'): 'S118',
    ('S118', 'i'): 'S119',
    ('S119', 'l'): 'S120',
    ('S120', 'e'): 'S121',

    # WITH
    ('S117', 'i'): 'S122',
    ('S122', 't'): 'S123',
    ('S123', 'h'): 'S124',
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
    'S67': 'not',
    'S69': 'of',
    'S70': 'or',
    'S76': 'packed',
    'S84': 'procedure',
    'S88': 'program',
    'S93': 'record',
    'S97': 'repeat',
    'S100': 'set',
    'S104': 'then',
    'S105': 'to',
    'S108': 'type',
    'S113': 'until',
    'S116': 'var',
    'S121': 'while',
    'S124': 'with',
}

class AnalisadorLexico:
    def __init__(self, trn, res):
        self.trn = trn
        self.res = res

    def palavra_reservada(self, palavra):
        estado = 'S0'

        for caractere in palavra.lower():
            transicao = (estado, caractere)
            if transicao not in self.trn:
                return False
            estado = self.trn[transicao]

        return estado in self.res

    def identificador(self, palavra):
        if not palavra:
            return False

        if not palavra[0].isalpha():
            return False

        for c in palavra[1:]:
            if not (c.isalpha() or c.isdigit() or c == '_'):
                return False

        return True

    def numero(self, palavra):
        return palavra.isdigit()

    def analisar(self, codigo):
        tokens = []

        i = 0
        linha = 1

        operadores = {
            '+': 'SOMA',
            '-': 'SUBTRACAO',
            '*': 'MULTIPLICACAO',
            '/': 'DIVISAO',
            '=': 'IGUAL',
            '<': 'MENOR',
            '>': 'MAIOR',
            '<=': 'MENOR_IGUAL',
            '>=': 'MAIOR_IGUAL',
            '<>': 'DIFERENTE',
            ':=': 'ATRIBUICAO'
        }

        delimitadores = {
            ';': 'PONTO_E_VIRGULA',
            ',': 'VIRGULA',
            '.': 'PONTO',
            ':': 'DOIS_PONTOS',
            '(': 'ABRE_PARENTESE',
            ')': 'FECHA_PARENTESE',
            '[': 'ABRE_COLCHETE',
            ']': 'FECHA_COLCHETE'
        }

        while i < len(codigo):
            c = codigo[i]

            if c.isspace():
                if c == '\n':
                    linha += 1

                i += 1
                continue

            if c == '{':
                inicio = i
                i += 1

                while i < len(codigo) and codigo[i] != '}':
                    if codigo[i] == '\n':
                        linha += 1
                    i += 1

                if i >= len(codigo):
                    tokens.append((
                        'ERRO',
                        'Comentário não fechado',
                        linha
                    ))
                    break

                i += 1
                continue

            if c.isalpha() or c == '_':
                inicio = i

                while (
                    i < len(codigo)
                    and (
                        codigo[i].isalnum()
                        or codigo[i] == '_'
                    )
                ): i += 1

                palavra = codigo[inicio:i]
                if self.palavra_reservada(palavra):
                    tokens.append((
                        'PALAVRA_RESERVADA',
                        palavra.lower(),
                        linha
                    ))
                else:
                    tokens.append((
                        'IDENTIFICADOR',
                        palavra,
                        linha
                    ))
                continue

            if c.isdigit():
                inicio = i
                while i < len(codigo) and codigo[i].isdigit():
                    i += 1

                numero = codigo[inicio:i]
                tokens.append((
                    'NUMERO',
                    numero,
                    linha
                ))
                continue

            if c == "'":
                inicio = i
                i += 1
                while i < len(codigo) and codigo[i] != "'":
                    if codigo[i] == '\n':
                        linha += 1
                    i += 1
                if i >= len(codigo):
                    tokens.append((
                        'ERRO',
                        'String não fechada',
                        linha
                    ))

                    break

                i += 1

                string = codigo[inicio:i]
                tokens.append((
                    'STRING',
                    string,
                    linha
                ))

                continue

            if i + 1 < len(codigo):
                op = codigo[i:i + 2]
                if op in operadores:
                    tokens.append((
                        operadores[op],
                        op,
                        linha
                    ))
                    i += 2

                    continue

            if c in operadores:
                tokens.append((
                    operadores[c],
                    c,
                    linha
                ))
                i += 1

                continue

            if c in delimitadores:
                tokens.append((
                    delimitadores[c],
                    c,
                    linha
                ))
                i += 1

                continue

            tokens.append((
                'ERRO',
                c,
                linha
            ))

            i += 1

        return tokens

lexer = AnalisadorLexico(trn, res)

codigo = """
program exemplo;

var
    x, y: integer;

begin
    x := 10;
    y := x + 20;

    if y > 20 then
        y := y - 1;

    while x < y do
        x := x + 1;
end.
"""

tokens = lexer.analisar(codigo)

for tipo, valor, linha in tokens: 
    print(f"Linha {linha:<3} | {tipo:<20} | {valor}")
