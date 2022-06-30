# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import client.authorization_pb2 as authorization__pb2


class GreeterStub(object):
    """Server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/Greeter/Register',
                request_serializer=authorization__pb2.RegisterRequest.SerializeToString,
                response_deserializer=authorization__pb2.RegisterReply.FromString,
                )
        self.Login = channel.unary_unary(
                '/Greeter/Login',
                request_serializer=authorization__pb2.LoginRequest.SerializeToString,
                response_deserializer=authorization__pb2.LoginReply.FromString,
                )


class GreeterServicer(object):
    """Server
    """

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=authorization__pb2.RegisterRequest.FromString,
                    response_serializer=authorization__pb2.RegisterReply.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=authorization__pb2.LoginRequest.FromString,
                    response_serializer=authorization__pb2.LoginReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Server
    """

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/Register',
            authorization__pb2.RegisterRequest.SerializeToString,
            authorization__pb2.RegisterReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/Login',
            authorization__pb2.LoginRequest.SerializeToString,
            authorization__pb2.LoginReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)