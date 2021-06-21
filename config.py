from transformers import CamembertModel, CamembertTokenizer

DEVICE = "cuda"
MAX_LEN = 128
TRAIN_BATCH_SIZE = 8
TEST_BATCH_SIZE = 4
EPOCHS = 10
CAMEMBERT_PATH = "camembert-base"
MODEL_PATH = "./model.bin"
TOKENIZER = CamembertTokenizer.from_pretrained(CAMEMBERT_PATH)