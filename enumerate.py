listanum = []
mai = 0
men = 0
for c in range ( 0, 5):
    listanum.append(int(input(f'dogote um valor apara a Posição {c}')))
    if c == 0:
     mai = men = listanum[c]
    else:
      if listanum[c] > mai :
       mai = listanum[c]
      if listanum[c] < men :
       men = listanum[c]
print('='*30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai}nas posições', end = "")
for i, v in enumarate(listanum):
   if v == mai:
      print(f'{i}.... ',  end= '')
print()
print(f'o menor valor digitado foi {men}nas posições' end = )
for i, v in enumarate(listanum):
  if v == men :
print()