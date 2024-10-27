from pickle import PROTO


def collinearity(vector_x_1, vector_x_2, vector_y_1, vector_y_2):
    vector_1 = vector_x_1 * vector_y_2
    vector_2 = vector_x_2 * vector_y_1

    return vector_1 == vector_2

testes = [(1,1,1,1),
          (1,2,2,4),
          (1,1,6,1),
          (1,2,-1,-2),
          (1,2,1,-2),
          (4,0,11,0),
          (0,1,6,0),
          (4,4,0,4),
          (0,0,0,0),
          (0,0,1,0),
          (5,7,0,0)]

results = [True,True,False,True,False,True,False,False,True,True,True]
results_testes = []


for count, item in enumerate(testes):
    x1, x2, y1, y2 = item

    collinear = collinearity(x1, x2, y1, y2) # Result: True

    results_testes.append(collinear)

    print(f'[{count+1}] Collinearity:\n'
          f'x1 = {x1}  |  y1 = {y1}\n'
          f'x2 = {x2}  |  y2 = {y2}\n'
          f'Are theses collinear vectors?\n'      
          f'Result: {collinear}')
print('---' * 10)
print(f'The results DO {'' if results_testes == results else 'NOT'} MATCH!')
print(f'Results         = {results}')
print(f'Results testes  = {results_testes}')
print('---' * 10)