from pythools.spam.enviador_de_email import Enviador

def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar('edenbam@gmail.com',
                    'emial@test.com',
                    'Cursos python',
                    'Ultima turma')
    assert 'edenbam@gmail.com' in resultado