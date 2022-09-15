import hashlib
from tqdm import tqdm

name="Aaron"
goalHash='7f4986da7d7b52fa81f98278e6ec9dcb'


for y in tqdm(range(1900,2022)):
    for m in range(1,13):
        d=1
        while d<32:
            guess=name+f'{y:04d}'+f'{m:02d}'+f'{d:02d}'
            if hashlib.md5(guess.encode()).hexdigest()==goalHash:
                print(guess)
                exit()
            d+=1
