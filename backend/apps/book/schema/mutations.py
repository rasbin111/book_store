import graphene


class CreateBookMutation(graphene.Mutation):

    class Arguments:
        title = graphene.String(required=True)
        category = graphene.Int(required=True)
        author = graphene.Int()


class BookMutation():
    pass