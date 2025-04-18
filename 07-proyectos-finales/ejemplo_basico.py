# Mini API REST simulada
class API:
    def get(self): return {'mensaje': 'Hola mundo'}
print(API().get())