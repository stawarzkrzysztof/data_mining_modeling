#  imports
import numpy as np
import librosa
import os
from sklearn.mixture import GaussianMixture
from typing import List
import argparse

CLASS_MAPPER = {
    1: "Kizo",
    2: "Sanah",
    3: "Holownia"
}
N_MFCC = 5
N_COMPONENTS = 5
RANDOM_STATE = 0
def get_gmms(train_paths: List[str], 
             n_mfcc: int = N_MFCC, 
             n_components: int = N_COMPONENTS) -> List[object]:

    gmm_list: List[object] = list()
    for voice_file in train_paths:
        y, sr = librosa.load(voice_file)
        m = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        gm = GaussianMixture(n_components=n_components, random_state=RANDOM_STATE).fit(np.transpose(m))
        gmm_list.append(gm)

    return gmm_list


def predict_proba(test_file: str, 
                  models: List[object], 
                  n_mfcc: int = N_MFCC) -> List[float]:

    y, sr = librosa.load(test_file)
    m = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    log_lklhd_scores = {
        CLASS_MAPPER[label+1]: gmm.score(np.transpose(m)) 
        for label, gmm in enumerate(models)}
    max_score = max(log_lklhd_scores.values())
    predicted_class = list(log_lklhd_scores.values()).index(max_score) + 1

    return log_lklhd_scores, predicted_class


def main(train_p: str, 
         test_p: str,
         n_mfcc: int,
         n_components: int) -> None:

    train_files = [os.path.join(train_p, file) for file in os.listdir(train_p)]
    train_files.sort()

    test_files = [os.path.join(test_p, file) for file in os.listdir(test_p)]
    test_files.sort()

    for test_file in test_files:
        print(test_file)
        scores, pred_class = predict_proba(test_file=test_file,
                                           models=get_gmms(train_files,
                                                           n_mfcc=n_mfcc,
                                                           n_components=n_components),
                                           n_mfcc=n_mfcc)
        print(scores)
        print(f"Predicted voice: {CLASS_MAPPER[pred_class]}", end="\n\n")
        
if __name__ == "__main__":
    
    # creating command line argument parser
    parser = argparse.ArgumentParser(
        description="Give me recording of your voice and I'll tell you who you are...")

    parser.add_argument("--train_folder_path",
                        type=str,
                        help="Path to a folder with recordings to train on",
                        default="glosy/train")

    parser.add_argument("--test_folder_path",
                        type=str,
                        help="Path to a folder with recordings to test on",
                        default="glosy/test")
    
    parser.add_argument("--number_of_MFCC",
                        type=int,
                        help="Number of MFCC",
                        default=N_MFCC)
        
    parser.add_argument("--number_of_GMM_components",
                        type=int,
                        help="Number of GMM components",
                        default=N_COMPONENTS)

    args = parser.parse_args()
    main(args.train_folder_path, 
         args.test_folder_path,
         args.number_of_MFCC,
         args.number_of_GMM_components)

    quit()