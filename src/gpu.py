
import torch
import logging

def print_gpu_info():
    print("Number of available GPUs:", torch.cuda.device_count())
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")

def set_all_gpus():
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        device = torch.device("cpu")
        print("Using CPU")
    return device

def set_gpu(device_id: int = 0):
    device = torch.device(f"cuda:{device_id}" if torch.cuda.is_available() else "cpu")
    logger = logging.getLogger(__name__)
# !export CUDA_VISIBLE_DEVICES=1
# !export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

def print_memory_usage():
    for i in range(torch.cuda.device_count()):
        allocated = torch.cuda.memory_allocated(i)
        reserved = torch.cuda.memory_reserved(i)
        print(f"GPU {i} - Allocated memory: {allocated / 1024 ** 2:.2f} MB")
        print(f"GPU {i} - Reserved memory: {reserved / 1024 ** 2:.2f} MB")