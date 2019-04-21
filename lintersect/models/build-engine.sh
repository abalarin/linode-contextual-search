#!/bin/bash

snips-nlu generate-dataset en lintersect/models/config.yaml lintersect/models/entities/*.yaml lintersect/models/intents/*.yaml  > lintersect/models/dataset.json ; rm -rf engine; time snips-nlu train lintersect/models/dataset.json lintersect/models/engine;
