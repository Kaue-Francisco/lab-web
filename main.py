from spyne import Application, rpc, ServiceBase, Integer, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class MathService(ServiceBase):
    @rpc(Float, Float, _returns=Float)
    def soma(ctx, a, b):
        return a + b

    @rpc(Float, Float, _returns=Float)
    def subtracao(ctx, a, b):
        return a - b

    @rpc(Float, Float, _returns=Float)
    def multiplicacao(ctx, a, b):
        return a * b

    @rpc(Float, Float, _returns=Float)
    def divisao(ctx, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a / b

# Criando a aplicação SOAP
application = Application([MathService],
                          tns='math.service',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

# Executando o servidor WSGI
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Servidor SOAP rodando em http://0.0.0.0:8000")
    server.serve_forever()