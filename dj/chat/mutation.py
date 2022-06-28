import graphene
from .models import *
from .object_types import *



class SaveMessage(graphene.Mutation):
    
    message = graphene.Field(MessageType)

    class Arguments:
        text = graphene.String()
        dialog_id = graphene.Int()
        user_id = graphene.Int()

    def mutate(root, info, text, dialog_id=None, user_id=None):
        current_user = info.context.user
        if not text:
            raise Exception("please enter message")
        dialog = Dialog.objects.filter(id=dialog_id).first()
        if not dialog and not user_id:
            raise Exception("To create dialog should be second user")
        elif user_id and not dialog:
            user2 = User.objects.filter(id=user_id).first()
            if not user2:
                raise Exception("User not fountd: {}'.format(user_id)")
            dialog = Dialog.objects.create(user1=current_user, user2=user2)
        instance = Message.objects.create(
            user=info.context.user,
            text=text,
            dialog=dialog
        )
        return SaveMessage(
            message=instance
        )

class CreateMessage(graphene.ObjectType):
    create_message=SaveMessage.Field()