#!/bin/bash

snips-nlu generate-dataset en config.yaml entities/*.yaml intents/*.yaml  > dataset.json ; rm -rf engine; time snips-nlu train dataset.json engine;
