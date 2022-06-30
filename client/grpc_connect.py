from client.base import ConnectGRPC
from client.authorization_pb2 import RegisterRequest, LoginRequest


class AuthorizationServerConnector(ConnectGRPC):
    """Class for connect with gRPC authorization server"""

    def registration_request(self, user_name: str, passwd: str):
        """Request to authorization server for registration"""

        response = self.stub.Register(RegisterRequest(
            user_name=user_name,
            user_passwd=passwd
        ))

        return response.code

    def authorization_request(self, user_name: str, passwd: str):
        """Reqeust to authorization server for login"""

        response = self.stub.Login(LoginRequest(
            user_name=user_name,
            user_passwd=passwd
        ))

        return response.code
