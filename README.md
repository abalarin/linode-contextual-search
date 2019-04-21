# linode-contextual-search
### Getting Started
```
git clone https://github.com/abalarin/linode-contextual-search.git
cd linode-contextual-search
virtualenv venv

source venv/bin/activate
```

#### Install requirments
```
pip install -r requirments.txt
python -m snips_nlu download

source lintersect/models/build-engine.sh

export FLASK_APP=lintersect

cd lintersect
flask run
```
