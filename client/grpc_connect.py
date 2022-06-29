import grpc

from client.authorization_pb2 import RegisterRequest, LoginRequest
from client.authorization_pb2_grpc import GreeterStub


class AuthorizationServerConnector:
    """Class for connect with gRPC authorization server"""

    def __init__(self, address_authorization_server: str):

        self.authorization_server = address_authorization_server
        self.authorization_channel = grpc.insecure_channel(self.authorization_server)
        self.authorization_stub = GreeterStub(self.authorization_channel)

    def registration_request(self, user_name: str, passwd: str):
        """Request to authorization server for registration"""

        response = self.authorization_stub.Register(RegisterRequest(
            user_name=user_name,
            user_passwd=passwd
        ))

        return response.code

    def authorization_request(self, user_name: str, passwd: str):
        """Reqeust to authorization server for login"""

        response = self.authorization_stub.Login(LoginRequest(
            user_name=user_name,
            user_passwd=passwd
        ))

        return response.code

    def connection_close(self):
        """Method to close connect after ended all operations"""

        self.authorization_channel.close()
