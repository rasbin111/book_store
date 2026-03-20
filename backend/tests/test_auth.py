import json

from graphene_django.utils.testing import GraphQLTestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationTestCase(GraphQLTestCase):
    GRAPHQL_URL = "/graphql/v1/"

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            email="admin@admin.com",
            password="admin"
        )
    
    def test_login(self):
        response = self.query(
            """
            mutation login($email:String!, $password:String!){
                tokenAuth(email:$email, password:$password){
                    user{
                        id
                        username
                        firstName
                        lastName
                    }
                    token
                }
            }
            """,
            operation_name="login",
            variables={
                "email": self.user.email,
                "password": "admin"
            }
        )

        json.loads(response.content)
        self.assertResponseNoErrors(response)
