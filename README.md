# Retry call of gRPC stub

The implement of code inspiration from [google-cloud-python#2583](https://github.com/GoogleCloudPlatform/google-cloud-python/issues/2583)

Tested OK with `grpcio==1.3.0`


```py
from grpc_retry import retrying_stub_methods

channel = grpc.insecure_channel('localhost:50051')
stub = helloworld_pb2_grpc.GreeterStub(channel)

# os.setenv('GRPC_RETRY_UNAVAILABLE', 5)
# os.setenv('GRPC_RETRY_DEADLINE_EXCEEDED', 4)
retrying_stub_methods(stub)

response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
print("Greeter client received: " + response.message)

```
