# firstline 

Opinionated collection of reusable functions and classes
Probably not useful 

## setup.py 
```    
    install_requires=[
        'firstline'
    ],

    dependency_links=[
        'http://github.com/bezaban/firstline/tarball/v0.3#egg=firstline'
    ]
```

## usage

Helper classes at top level

Standalone functions in helpers.* 


```
import firstline as fl

LOGGING_CONFIG=fl.helpers.getlogconfig('logfile.log', debug)
logging.config.dictConfig(LOGGING_CONFIG)
log = logging.getLogger()

config = fl.ConfigHandler('config.json', default_config, interactive)

```
