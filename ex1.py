def fibonacci(n):
    fib1, fib2 = 0, 1
    
    if n == 0 or n == 1:
        return True
    
    while fib2 <= n:
        if fib2 == n:
            return True
        fib1, fib2 = fib2, fib1 + fib2
    
    return False

numero = int(input("Digite um número: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
