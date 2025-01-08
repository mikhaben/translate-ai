import os
from src.translator import Translator
from src.utils import readJsonFile, writeJsonFile
from src.config import config

output_lang = 'cs'
# init instance
translator = Translator(config['models'][output_lang])
# JSON input
json_input = readJsonFile(config['input_file'])
# translate
translated_json = translator.translate_json(json_input)
# write to file
writeJsonFile(config['output_dir'] + output_lang + '.json', translated_json)
