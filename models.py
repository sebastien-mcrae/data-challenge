from transformers import CamembertModel
import torch.nn as nn
import config


class CAMEMBERTBase(nn.Module):
    def __init__(self):
        super(CAMEMBERTBase, self).__init__()
        self.bert = CamembertModel.from_pretrained(config.CAMEMBERT_PATH)
        self.bert_drop = nn.Dropout(p=0.3)
        self.linear = nn.Linear(768, 3) # 3 classes

    def forward(self, ids, mask, token_type_ids):
        outputs = self.bert(ids,attention_mask=mask,token_type_ids=token_type_ids)
        # sequence_output has the following shape: (batch_size, sequence_length, 768),
        # which contains output for all tokens in the last layer of the BERT model.
        sequence_output = outputs[0]
        # pooled_output has the following shape: (batch_size, 768) with representations for the entire input sequences.
        pooled_output = outputs[1]
        bert_output = self.bert_drop(pooled_output)
        output = self.linear(bert_output)
        return output
