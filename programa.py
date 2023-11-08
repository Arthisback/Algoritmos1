funci= int (input("Quantos funcionarios tem na empresa?"))
i=0
while i<funci:
  i=i+1
  valor = float(input("Qual o seu salario"))
  print(f"Seu valor com reajuste de 7,5% é:{valor+(valor*0.075)}")