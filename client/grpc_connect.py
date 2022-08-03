import time

from client.base import ConnectGRPC
from client.authorization_api.authorization_pb2 import RegisterRequest, LoginRequest, RegisterReply, LoginReply
from client.authorization_api.authorization_pb2_grpc import AuthorizationStub
from client.messanger_api.messanger_pb2 import RequestSelfInfo, AddFriendRequest, Response, RemoveFriendRequest, \
    CreateRoomRequest, EscapeRoomRequest, RemoveRoomReqeust, ClientInfo, JoinRoomRequest, Message, MessagesUpdateRequest
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

    def create_room(self, room: str, token: str) -> Response:
        """Request to create room"""

        response = self.stub.CreateRoom(
            CreateRoomRequest(
                room=room,
                credentials=token
            )
        )
        return response

    def leave_room(self, room: str, token: str) -> Response:
        """Request to leave a room"""

        response = self.stub.RoomEscape(
            EscapeRoomRequest(
                room=room,
                credentials=token
            )
        )
        return response

    def delete_room(self, room: str, token: str) -> Response:
        """Request to delete a room"""

        response = self.stub.RemoveRoom(
            RemoveRoomReqeust(
                room=room,
                credentials=token
            )
        )
        return response

    def update_data(self, token: str, time_: int) -> ClientInfo:
        """Request to update data"""

        client_info = self.stub.InformationRequest(
            RequestSelfInfo(
                credentials=token,
                time=time_
            )
        )
        return client_info

    def join_room(self, room: str, token: str) -> Response:
        """Reqeust to join room"""

        response = self.stub.JoinRoom(
            JoinRoomRequest(
                room=room,
                credentials=token
            )
        )

        return response

    def send_message(self, message: str, token: str, address: str) -> Response:
        """Request to send message"""

        response = self.stub.SendMessage(
            Message(
                message=message,
                addressee=address,
                credentials=token
            )
        )

        return response

    def update_messages(self, token: str, unit: str, last_update_time: int):
        """Request to receive new messages"""

        response = self.stub.MessagesUpdate(
            MessagesUpdateRequest(
                credentials=token,
                update=unit,
                time=last_update_time
            )
        )

        return response
