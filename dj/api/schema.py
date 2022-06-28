from webbrowser import get
import graphene
from chat.queries import GetChat
from chat.mutation import CreateMessage


class Query(GetChat):
    pass

class Mutation(CreateMessage):
    pass




schema = graphene.Schema(query=Query, mutation=Mutation)
