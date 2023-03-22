from random import choice, randrange
from datetime import datetime


operators = ["+", "-", "/", "*"]
times = 5
init_time = datetime.now()
correct = 0
incorrect = 0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

for i in range(0, times):
  number_1 = randrange(10)
  operator = choice(operators)
  number_2 = randrange(10)

  if operator == "/":
    while number_2 == 0:
      number_2 = randrange(10)      

  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
  result = float (input("resultado: "))

  match operator:
    case "+" :
      trueresult = number_1 + number_2
    case "-" :
      trueresult = number_1 - number_2
    case "/" :
      trueresult = number_1 / number_2
    case "*" :
       trueresult = number_1 * number_2
  if trueresult == result :
    print ("Resultado correcto")
    correct = correct + 1
  else :
    print ("resultado incorrecto")
    incorrect = incorrect + 1


end_time = datetime.now()
total_time = end_time - init_time
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n La cantidad de resultados correctos es de {correct} y la de incorrectos {incorrect}")