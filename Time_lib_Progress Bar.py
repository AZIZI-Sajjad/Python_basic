  # Ref : https://stackoverflow.com/questions/3160699/python-progress-bar
from time import sleep
from tqdm import tqdm
for i in tqdm(range(10)):
    sleep(3)
