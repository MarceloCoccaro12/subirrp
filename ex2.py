def contar(string):
    quantidade = string.lower().count('a')
    
    print(f"A letra 'a' aparece {quantidade} vezes na string." if quantidade > 0 else "A letra 'a' não aparece na string.")


texto = input("Digite uma string: ")
contar(texto)