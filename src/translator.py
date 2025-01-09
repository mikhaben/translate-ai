import warnings
import copy
from transformers import MarianMTModel, MarianTokenizer

# suppress future warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers.tokenization_utils_base")

class Translator:
    def __init__(self, config: dict) -> None:
        self.models = {
            lang: {
                "tokenizer": MarianTokenizer.from_pretrained(model_name),
                "model": MarianMTModel.from_pretrained(model_name)
            }
            for lang, model_name in config.items()
        }

    def translate_str(self, text: str, target_lang: str) -> str:
        if not text.strip():
            return text

        tokenizer = self.models[target_lang]["tokenizer"]
        model = self.models[target_lang]["model"]

        try:
            inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
            translated = model.generate(**inputs, max_length=1024)
            return tokenizer.decode(translated[0], skip_special_tokens=True)
        except Exception as e:
            print(f"Translation error for {target_lang}: {e}")
            return text

    def translate_json(self, data: dict) -> dict:
        result = {}
        try:
            for lang in self.models:
                result[lang] = {
                    key: self.translate_str(str(val), lang)
                    for key, val in data.items()
                }
        except Exception as e:
            print(f"JSON translation error: {e}")
        return result
