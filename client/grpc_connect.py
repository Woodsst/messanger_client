from client.base import ConnectGRPC
from client.authorization_api.authorization_pb2 import RegisterRequest, LoginRequest, RegisterReply, LoginReply
from client.authorization_api.authorization_pb2_grpc import AuthorizationStub
from client.messanger_api.messanger_pb2 import AddFriendRequest, Response, RemoveFriendRequest
from client.messanger_api.messanger_pb2_grpc import MessangerStub


class AuthorizationServerConnector(ConnectGRPC):
    """Class for connect with gRPC authorization_api server"""

    def __init__(self, authorization_server_address: str):
        ConnectGRPC.__init__(self, authorization_server_address)
        self.stub = AuthorizationStub(self.channel)

    def registration_request(self, user_name: str, passwd: str) -> RegisterReply:
        """Request to authorization_api server for registration"""

        response = self.stub.Register(RegisterRequest(
            user_name=user_name,
            user_passwd=passwd
        ))
        return response

    def authorization_request(self, user_name: str, passwd: str) -> LoginReply:
        """Reqeust to authorization_api server for login"""

        response = self.stub.Login(LoginRequest(
            user_name=user_name,
            user_passwd=passwd
        ))
        return response


class MessangerServerConnector(ConnectGRPC):
    """Class for connect with gRPC messanger server"""

    def __init__(self, messanger_server_address: str):
        ConnectGRPC.__init__(self, messanger_server_address)
        self.stub = MessangerStub(self.channel)

    def add_friend(self, friend_name: str, token: str) -> Response:
        """Request to add a friend"""

        response = self.stub.AddFriend(
            AddFriendRequest(
                friend=friend_name,
                credentials=token
            )
        )

        return response

    def remove_friend(self, friend_name: str, token: str) -> Response:
        """Request to remove friend"""

        response = self.stub.RemoveFriend(
            RemoveFriendRequest(
                friend=friend_name,
                credentials=token
            )
        )

        return response
