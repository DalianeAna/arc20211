from errbot import BotPlugin, botcmd


class Example(BotPlugin):
    """
    Apenas uma classe de métodos para aprendizado.
    """

    @botcmd  
    def bomdia(self, msg, args):
        """
        Responde educadamente ao usuário.
        """

        argumentos = args.split(' ')
        return "Bom dia, quinta-feira!"
