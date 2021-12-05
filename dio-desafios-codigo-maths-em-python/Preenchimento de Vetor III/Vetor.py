x = float(input("Digite o numero:"))
for i in range(0, 100):
    print('N[{}] = '.format(i), '{:.4f}'.format(x))
    x /= 2