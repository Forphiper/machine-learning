# Machine Learning Homeworks

## HW1: Regression
* Solve a regression problem with deep neural networks (DNN).
* Understand basic DNN training tips e.g. hyper-parameter tuning, feature selection, regularization, ... 
* Given survey results in the past 3 days in a specific state in U.S., then predict the percentage of new tested positive cases in the 3rd day. 
## HW2: Classification
* Solve a classification problem with deep neural networks (DNNs).
* Understand recursive neural networks (RNNs).
* Multiclass Classification: Framewise phoneme prediction from speech.
* Dataset - LibriSpeech (subset of train-clean-100)
    * Training: 3429 preprocessed audio features w/ labels (total 2116794 frames)
    * Testing: 857 preprocessed audio features w/o labels (total 527364 frames)
    * Label: 41 classes, each class represents a phoneme
## HW3: CNN
* Solve image classification with convolutional neural networks(CNN).
* Dataset
    * The images are collected from the food-11 dataset splitted into 11 classes.
    * Training set: 10000 labeled images
    * Validation set: 3643 labeled images
    * Testing set: 3000 images without labeled
## HW4: Self-attention
* Multiclass Classification: Predict speaker class from given speech.
* Dataset - VoxCeleb2
    * Training: 56666 processed audio features with labels.
    * Testing: 4000 processed audio features (public & private) without labels.
    * Label: 600 classes in total, each class represents a speaker.
## HW5: Transformer
* In this homework, we’ll translate English to Traditional Chinese. Since sentences are with different length in different languages, the seq2seq framework is applied to this task.
* Training datasets
    * Paired data
        * TED2020: TED talks with transcripts translated by a global community of volunteers to more than 100 language
        * We will use (en, zh-tw) aligned pairs
    * Monolingual data
        * More TED talks in traditional Chinese
## HW6: Generative Model
* Input: random number
* Output: Anime face
* Implementation requirement: Diffusion Model
* Target: generate 1000 anime face images
## HW7: BERT
* Extractive Question Answering
* Traditional Chinese Reading Comprehension Dataset
    * DRCD: 台達閱讀理解資料集 Delta Reading Comprehension Dataset
    * ODSQA: Open-Domain Spoken Question Answering Dataset
    * train: DRCD + DRCD-backtrans
        * 15329 paragraphs, 26918 questions
    * dev: DRCD + DRCD-backtrans
        * 1255 paragraphs, 2863 questions
    * test: DRCD + ODSQA
        * 1606 paragraphs, 3504 questions
## HW8: Auto-encoder
* Unsupervised anomaly detection: Training a model to determine whether the given image is similar with the training data.
* Data
    * Training data
        * 100000 human faces
    * Testing data
        * About 10000 from the same distribution with training data (label 0)
        * About 10000 from another distribution (anomalies, label 1) 
## HW9: Explainable AI
* Why we need Explainable AI?
    * Correct answers ≠ Intelligent
    * We can improve ML model based on explanation
    * Make people comfortable since people need reasons 
## HW10: Attack
* Choose any proxy network to attack the black box model from TA
* Implement non-targeted adversarial attack method
    * FGSM
    * I-FGSM
    * MI-FGSM
* Increase attack transferability by Diverse input (DIM)
* Attack more than one proxy model - Ensemble attack
