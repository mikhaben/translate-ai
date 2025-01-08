import warnings
import copy
from transformers import MarianMTModel, MarianTokenizer

# suppress future warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers.tokenization_utils_base")

class Translator:
    def __init__(self, model_name: str) -> None:
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)
        print(f"Model initialized: {model_name}")

    def translateStr(self, text: str) -> str:
        # Tokenize the text
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        # Generate translation
        translated = self.model.generate(**inputs)
        # Decode the translation
        return self.tokenizer.decode(translated[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)

    def translate_json(self, json: dict) -> dict:
        print("Translating JSON...")
        json_copy = copy.deepcopy(json)
        for key, val in json_copy.items():
            val["message"] = self.translateStr(val["message"])
        return json_copy
        print("Translation complete")
