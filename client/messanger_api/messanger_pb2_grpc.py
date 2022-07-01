# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import client.messanger_api.messanger_pb2 as messanger__pb2


class MessangerStub(object):
    """Server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InformationRequest = channel.unary_unary(
                '/Messanger/InformationRequest',
                request_serializer=messanger__pb2.RequestSelfInfo.SerializeToString,
                response_deserializer=messanger__pb2.ClientInfo.FromString,
                )
        self.SendMessage = channel.unary_unary(
                '/Messanger/SendMessage',
                request_serializer=messanger__pb2.Message.SerializeToString,
                response_deserializer=messanger__pb2.Response.FromString,
                )
        self.AddFriend = channel.unary_unary(
                '/Messanger/AddFriend',
                request_serializer=messanger__pb2.AddFriendRequest.SerializeToString,
                response_deserializer=messanger__pb2.Response.FromString,
                )
        self.RemoveFriend = channel.unary_unary(
                '/Messanger/RemoveFriend',
                request_serializer=messanger__pb2.RemoveFriendRequest.SerializeToString,
                response_deserializer=messanger__pb2.Response.FromString,
                )
        self.CreateRoom = channel.unary_unary(
                '/Messanger/CreateRoom',
                request_serializer=messanger__pb2.CreateRoomRequest.SerializeToString,
                response_deserializer=messanger__pb2.Response.FromString,
                )
        self.JoinRoom = channel.unary_unary(
                '/Messanger/JoinRoom',
                request_serializer=messanger__pb2.JoinRoomRequest.SerializeToString,
                response_deserializer=messanger__pb2.Response.FromString,
                )
        self.RoomEscape = channel.unary_unary(
                '/Messanger/RoomEscape',
                request_serializer=messanger__pb2.EscapeRoomRequest.SerializeToString,
                response_deserializer=messanger__pb2.Response.FromString,
                )


class MessangerServicer(object):
    """Server
    """

    def InformationRequest(self, request, context):
        """Method for getting information about changes in client data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Method for handle and write client message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddFriend(self, request, context):
        """Method for handle client request for add friend
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveFriend(self, request, context):
        """Method for handle client request for remove friend
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRoom(self, request, context):
        """Method for handle client request for create new room
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinRoom(self, request, context):
        """Method for handle client request for join room
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RoomEscape(self, request, context):
        """Method for handle client request for to leave room
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessangerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InformationRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.InformationRequest,
                    request_deserializer=messanger__pb2.RequestSelfInfo.FromString,
                    response_serializer=messanger__pb2.ClientInfo.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=messanger__pb2.Message.FromString,
                    response_serializer=messanger__pb2.Response.SerializeToString,
            ),
            'AddFriend': grpc.unary_unary_rpc_method_handler(
                    servicer.AddFriend,
                    request_deserializer=messanger__pb2.AddFriendRequest.FromString,
                    response_serializer=messanger__pb2.Response.SerializeToString,
            ),
            'RemoveFriend': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveFriend,
                    request_deserializer=messanger__pb2.RemoveFriendRequest.FromString,
                    response_serializer=messanger__pb2.Response.SerializeToString,
            ),
            'CreateRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRoom,
                    request_deserializer=messanger__pb2.CreateRoomRequest.FromString,
                    response_serializer=messanger__pb2.Response.SerializeToString,
            ),
            'JoinRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinRoom,
                    request_deserializer=messanger__pb2.JoinRoomRequest.FromString,
                    response_serializer=messanger__pb2.Response.SerializeToString,
            ),
            'RoomEscape': grpc.unary_unary_rpc_method_handler(
                    servicer.RoomEscape,
                    request_deserializer=messanger__pb2.EscapeRoomRequest.FromString,
                    response_serializer=messanger__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Messanger', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Messanger(object):
    """Server
    """

    @staticmethod
    def InformationRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Messanger/InformationRequest',
            messanger__pb2.RequestSelfInfo.SerializeToString,
            messanger__pb2.ClientInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Messanger/SendMessage',
            messanger__pb2.Message.SerializeToString,
            messanger__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddFriend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Messanger/AddFriend',
            messanger__pb2.AddFriendRequest.SerializeToString,
            messanger__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveFriend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Messanger/RemoveFriend',
            messanger__pb2.RemoveFriendRequest.SerializeToString,
            messanger__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Messanger/CreateRoom',
            messanger__pb2.CreateRoomRequest.SerializeToString,
            messanger__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Messanger/JoinRoom',
            messanger__pb2.JoinRoomRequest.SerializeToString,
            messanger__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RoomEscape(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Messanger/RoomEscape',
            messanger__pb2.EscapeRoomRequest.SerializeToString,
            messanger__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)