# Словари
arrows = \
    {'up': '↑',
     'down': '↓',
     'left': '←',
     'right': '→'
     }
print(arrows)   # {'up': '↑', 'down': '↓', 'left': '←', 'right': '→'}
print(arrows['right'])  # →

for k in arrows.keys():
    print(k, end=' ')   # up down left right

print()
for v in arrows.values():
    print(v, end=' ')   # ↑ ↓ ← →

print()
for v in arrows:
    print(v, end=' ')
    print(arrows[v])   # up↑ down↓ left← right→

