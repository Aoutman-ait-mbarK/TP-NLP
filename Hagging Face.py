# Hagging Face
#!pip install transformers
from transformers import pipeline

get_ipython().system('pip install flair')
from transformers import AutoTokenizer
from flair.data import Sentence
from flair.models import SequenceTagger