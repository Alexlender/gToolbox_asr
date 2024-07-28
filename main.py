import nemo.collections.asr as nemo_asr
import grpc
import gTB_ASR_pb2
import gTB_ASR_pb2_grpc
from concurrent import futures

from random import choice
import os
import string

import socket

asr_model = nemo_asr.models.EncDecHybridRNNTCTCBPEModel.from_pretrained(model_name="nvidia/stt_ru_fastconformer_hybrid_large_pc")


if not os.path.exists("tmp"): 
    os.makedirs("tmp")

def randSeq(n : int) -> str:
    b = ""
    for _ in range(n):
        b += choice(string.ascii_letters)
    return b


def genFilename() -> str:
    return randSeq(10) + ".wav"


def saveData(data : bytes) -> str:
    filename = "tmp/" + genFilename()
    with open(filename, mode='wb') as f:
        f.write(data)
        
    return filename

def transcribe(file):
    r = asr_model.transcribe([file])
    return r[0][0]


class gTB_ASR_Srv(gTB_ASR_pb2_grpc.gTB_ASRServicer):
    def ASRFile(self, request : gTB_ASR_pb2.FilenameRequest, context):
        r = transcribe(request.name)
        return gTB_ASR_pb2.ASRReply(text = r)
    
    def ASRWav(self, request : gTB_ASR_pb2.WavRequest, context):
        filename = saveData(request.wav)
        r= transcribe(filename) 
        os.remove(filename)
        
        return gTB_ASR_pb2.ASRReply(text = r)

def serve():
    port = "50501"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options = [
        ('grpc.max_receive_message_length', 104857600)
    ])
    gTB_ASR_pb2_grpc.add_gTB_ASRServicer_to_server(gTB_ASR_Srv(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
    

if __name__ == '__main__':
    # c = consulate.Consul()
    # c.agent.service.register("asr",
    #                         port=50501,
    #                         tags=["12"],
    #                         ttl="60s")
    channel = grpc.insecure_channel(f'{os.environ["SERVER"]}:50501')
    stub = gTB_ASR_pb2_grpc.gTB_ASRStub(channel)
    stub.ASRAddAgent(gTB_ASR_pb2.AddAgentRequest(agent_ip=socket.gethostbyname(socket.gethostname())))

    serve()
    