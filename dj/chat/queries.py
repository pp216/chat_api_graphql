import graphene
from .object_types import *

class GetChat(graphene.ObjectType):
    dialog = graphene.Field(DialogType,id=graphene.Int())
    user=graphene.Field(UserType)

    def resolve_dialog(self, info, id):
        current_user = info.context.user
        id = current_user.get('id')
        if id:
            dialog = Dialog.objects.get(id=id)
            if dialog.user1 != current_user or dialog.user2 != current_user:
                dialog = None
        return dialog

    def resolve_user(self, info):
        return User.objects.all()

