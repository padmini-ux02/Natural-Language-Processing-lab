import nltk
from nltk.tokenize import word_tokenize
from transformers import AutoTokenizer
nltk.download("punkt")
nltk.download("punkt_tab")
text = "Tokenization without transformers is straightforward with tools like NLTK."

tokens = word_tokenize(text)

print("NLTK Tokens:")
print(tokens)                                        

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

tokens_transformers = tokenizer(
    text,
    return_tensors="pt"
)

print("\nTransformers Output:")
print(tokens_transformers)

input_ids = tokens_transformers["input_ids"][0]

tokens_transformers_list = tokenizer.convert_ids_to_tokens(
    input_ids.tolist()
)

print("\nTransformers Tokens (List):")
print(tokens_transformers_list)

decoded_text = tokenizer.decode(
    input_ids,
    skip_special_tokens=True
)

print("\nDecoded Text:")
print(decoded_text)
