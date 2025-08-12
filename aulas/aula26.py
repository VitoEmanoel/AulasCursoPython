"""
Formatação basica de strings
s - string
d - int 
f - float
<numero de digitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda 
< - Direita 
^ - Centro
= - força o numero a aparecer antes do zero 
Sinal - + ou -
Ex.: 0>-100,.1f
conversion flags - !r !S !a
"""
variavel = "ABC"
print (f"{variavel}")
print (f"{variavel: >10}")
print (f"{variavel: <10}.")
print (f"{variavel: ^10}.")
print (f"{1000.47384738230:0=+10,.1f}")
print (f"o Hexadecimal de 1500 é {1500:08X}")
print (f"{variavel!r}")