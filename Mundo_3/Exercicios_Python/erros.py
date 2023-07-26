try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados informados')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as error:
    print(f'Problema encontrado foi {error.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')