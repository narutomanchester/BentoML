# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bentoml.grpc.v1alpha1 import service_test_pb2 as bentoml_dot_grpc_dot_v1alpha1_dot_service__test__pb2


class TestServiceStub(object):
    """Use for testing interceptors per RPC call.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Execute = channel.unary_unary(
                '/bentoml.testing.v1alpha1.TestService/Execute',
                request_serializer=bentoml_dot_grpc_dot_v1alpha1_dot_service__test__pb2.ExecuteRequest.SerializeToString,
                response_deserializer=bentoml_dot_grpc_dot_v1alpha1_dot_service__test__pb2.ExecuteResponse.FromString,
                )


class TestServiceServicer(object):
    """Use for testing interceptors per RPC call.
    """

    def Execute(self, request, context):
        """Unary API
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Execute': grpc.unary_unary_rpc_method_handler(
                    servicer.Execute,
                    request_deserializer=bentoml_dot_grpc_dot_v1alpha1_dot_service__test__pb2.ExecuteRequest.FromString,
                    response_serializer=bentoml_dot_grpc_dot_v1alpha1_dot_service__test__pb2.ExecuteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bentoml.testing.v1alpha1.TestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestService(object):
    """Use for testing interceptors per RPC call.
    """

    @staticmethod
    def Execute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bentoml.testing.v1alpha1.TestService/Execute',
            bentoml_dot_grpc_dot_v1alpha1_dot_service__test__pb2.ExecuteRequest.SerializeToString,
            bentoml_dot_grpc_dot_v1alpha1_dot_service__test__pb2.ExecuteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)