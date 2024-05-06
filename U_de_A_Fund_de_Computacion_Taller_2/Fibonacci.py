n = int(input('Ingrese el valor de N:\n'))

f0 = 1
f1 = 1
fn = 0

print(f'n_1: {f0}')
print(f'n_2: {f1}')

for i in range(2,n-1):
    fn = f0 + f1

    print(f'n_{i+2}: {fn}')

    f0 = f1
    f1 = fn