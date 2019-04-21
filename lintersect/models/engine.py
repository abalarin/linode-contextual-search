import io
import json

from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

loaded_engine = SnipsNLUEngine.from_path("./engine")
while True:
    query = input('query> ')
    intents = loaded_engine.parse(query, top_n=2)
    print(json.dumps(intents, indent=2))
    # data = {json.dumps(intents, indent=2)}
    # trueint = data[0]
    print("trye: ", intents[0])
    # for item in intents:
    #     print("test" , key)
