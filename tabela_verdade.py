import pandas as pd
import itertools

# V: casa é vermelha
# C: cachorro late
# P: passarinho canta

# Todas as combinações de V, C e P (True/False)
values = list(itertools.product([True, False], repeat=3))
columns = ['V', 'C', 'P']

df = pd.DataFrame(values, columns=columns)

# Proposições
df['¬V'] = ~df['V']
df['¬P'] = ~df['P']
df['¬V → C'] = ~df['¬V'] | df['C']       # ¬V implica C
df['V → ¬P'] = ~df['V'] | df['¬P']       # V implica ¬P
df['P é verdadeira'] = df['P']

# Verificar onde todas as premissas são verdadeiras
df['Premissas válidas'] = df['¬V → C'] & df['V → ¬P'] & df['P']

# Exibir apenas os casos válidos
valid = df[df['Premissas válidas']]

print("Linhas que satisfazem todas as premissas:")
print(df)
