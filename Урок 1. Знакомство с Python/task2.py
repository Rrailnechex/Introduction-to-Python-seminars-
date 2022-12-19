

""" 
Напишите программу для. 
проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
для всех значений предикат.
 """

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(f"x = {x} and y = {y} or z = {z} = x and y or z")
