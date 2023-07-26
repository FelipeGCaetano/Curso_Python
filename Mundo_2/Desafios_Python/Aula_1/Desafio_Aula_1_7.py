
s1=float(input('Primeiro segmento: '))
s2=float(input('Segundo segmento: '))
s3=float(input('Terceiro segmento: '))

if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print(f'Os segmentos acima podem formar um triângulo ', end='++')
    if s1==s2==s3:
        print(f'EQUILATERO')
    elif s1!=s2!=s3!=s1:
        print(f'ESCALENO')
    else:
        print(f'ISÓCELES')
else:
    print(f'Os segmentos acima não podem formar um triângulo.')
