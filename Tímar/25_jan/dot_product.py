def list_dot(u, v):
    return sum(u[i]*v[i]*u[i] for i in range(len(u)))


a = [1,2,3]
b = [1,-1,2]

result = list_dot(a, b)
print(result)