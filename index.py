import os
from src.translator import Translator
from src.utils import readJsonFile, writeJsonFile
from src.config import config
from user_config import user_config

# read input file
json_input = readJsonFile(config['input_file'])

# translate
models = {
    lang: config['models'][lang]
    for lang in user_config['languages']
    if lang in config['models']
}
instance = Translator(models)
res_json = instance.translate_json(json_input)

# write to file
for lang in user_config['languages']:
    writeJsonFile(config['output_dir'] + lang + '.json', res_json[lang])
