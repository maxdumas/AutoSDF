# import socket
# import getpass

# username = getpass.getuser()

# hostname = socket.gethostname()
import os

current_dir = os.getcwd()

dataroot = os.path.join(current_dir, "data")
logroot = os.path.join(current_dir, "logs")

# if hostname == 'yenchi-pc':
#     dataroot = '/home/yenchi/generative_transformers/data'
#     logroot = '/home/yenchi/generative_transformers/logs'
# elif hostname == 'u110459':
#     dataroot= '/data/datasets/paritosh'
#     logroot= '/data/paritosh/generative_transformers/logs'
#     if username == 'yenchi':
#         dataroot = '/data/yenchi/generative_transformers/data'
#         logroot = '/data/yenchi/generative_transformers/logs'
# elif hostname == 'euclid':
#     if username == 'yenchi':
#         dataroot = '/data/yenchi/generative_transformers/data'
#         logroot = '/data/yenchi/generative_transformers/logs'