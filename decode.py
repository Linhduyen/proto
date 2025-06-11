import snappy
import remote_pb2  

with open("test/mess.json", "rb") as f:
    raw_data = f.read()

try:
    decompressed = snappy.decompress(raw_data)
except Exception as e:
    print("Snappy decompress failed:", e)
    exit(1)

msg = remote_pb2.RemoteRecord()
try:
    msg.ParseFromString(decompressed)
    print("Giải mã thành công:")
    print(msg)
except Exception as e:
    print("Protobuf decode failed:", e)
