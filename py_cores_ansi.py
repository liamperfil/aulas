# Cores padrão ANSI em python

cor = '\033[1;33;41m'
reset = '\033[m'
print(f'{cor}Olá mundo!{reset} E mais!')

# Experimente \033[7m\033[1m 
# Acima utilizamos 7 para inverter e repete com formatação 1 para negrito

# Style 0, 1, 4 e 7 (reset, negrito, sublinha e inverte)
# Texto/Background
# 30/40 branco
# 31/41 vermelho
# 32/42 verde
# 33/43 amarelo
# 34/44 azul
# 35/45 roxo
# 36/46 azul claro
# 37/47 cinza

# Exemplo: \033[1;33;40m