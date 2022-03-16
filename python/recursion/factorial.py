def fact(x):
    if x == 1:  # Base Case - Na recursividade é necessário para saida da recursao, evitando o looping infinito e o famoso stackoverflow
        return 1
    else:
        return x * fact(x - 1) # Recursive case


print(fact(6))
