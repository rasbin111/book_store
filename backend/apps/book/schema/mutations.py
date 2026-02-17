import graphene


class CreateBookMutation(graphene.Mutation):

    class Arguments:
        title = graphene.String(required=True)
        


class BookMutation():
    pass