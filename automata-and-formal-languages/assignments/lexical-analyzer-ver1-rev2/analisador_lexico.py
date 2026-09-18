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
    ('S0', 'r'): 'S89',
    ('S89', 'e'): 'S90',
    ('S90', 'c'): 'S91',
    ('S91', 'o'): 'S92',
    ('S92', 'r'): 'S93',
    ('S93', 'd'): 'S94',

    # REPEAT
    ('S90', 'p'): 'S95',
    ('S95', 'e'): 'S96',
    ('S96', 'a'): 'S97',
    ('S97', 't'): 'S98',

    # SET
    ('S0', 's'): 'S99',
    ('S99', 'e'): 'S100',
    ('S100', 't'): 'S101',

    # THEN
    ('S0', 't'): 'S102',
    ('S102', 'h'): 'S103',
    ('S103', 'e'): 'S104',
    ('S104', 'n'): 'S105',

    # TO
    ('S102', 'o'): 'S106',

    # TYPE
    ('S102', 'y'): 'S107',
    ('S107', 'p'): 'S108',
    ('S108', 'e'): 'S109',

    # UNTIL
    ('S0', 'u'): 'S110',
    ('S110', 'n'): 'S111',
    ('S111', 't'): 'S112',
    ('S112', 'i'): 'S113',
    ('S113', 'l'): 'S114',

    # VAR
    ('S0', 'v'): 'S115',
    ('S115', 'a'): 'S116',
    ('S116', 'r'): 'S117',

    # WHILE
    ('S0', 'w'): 'S118',
    ('S118', 'h'): 'S119',
    ('S119', 'i'): 'S120',
    ('S120', 'l'): 'S121',
    ('S121', 'e'): 'S122',

    # WITH
    ('S118', 'i'): 'S123',
    ('S123', 't'): 'S124',
    ('S124', 'h'): 'S125',
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
    'S94': 'record',
    'S98': 'repeat',
    'S101': 'set',
    'S105': 'then',
    'S106': 'to',
    'S109': 'type',
    'S114': 'until',
    'S117': 'var',
    'S122': 'while',
    'S125': 'with',
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
