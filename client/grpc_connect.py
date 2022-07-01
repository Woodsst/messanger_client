from client.base import ConnectGRPC
from client.authorization_api.authorization_pb2 import RegisterRequest, LoginRequest, RegisterReply, LoginReply
from client.authorization_api.authorization_pb2_grpc import AuthorizationStub


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
