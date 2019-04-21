from prance import ResolvingParser
import json
parser = ResolvingParser('./openapi.yaml')

spec = parser.specification

paths = spec.get('paths');
components = spec.get('components')
schemas = components.get('schemas')

for path, data in paths.iteritems() : 
    print path
    for method, data in data.iteritems() :
        if 'operationId' in data: 
            print data.get('operationId')
            try:
                resp = data.get('responses').get('200').get('content').get('application/json').get('schema').get('properties')
                if resp and 'data' in resp:
                    print resp.get('data').get('items')
            except:
                continue
