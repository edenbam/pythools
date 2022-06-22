from pythools.spam.enviador_de_email import Enviador
from pythools.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails('edenbam@gmail.com','Curso','Confira os módulos fantásticos')