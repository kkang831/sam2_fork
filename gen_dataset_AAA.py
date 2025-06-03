


import os 
import argparse
import torch
from sam2.sam2_image_predictor import SAM2ImagePredictor












def main(args):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    predictor = SAM2ImagePredictor.from_pretrained("facebook/sam2-hiera-large")
    
    
    
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
    print('Done')