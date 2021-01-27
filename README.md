# firstline 

Collection of reusable functions

## setup.py 
```    
    install_requires=[
        'firstline'
    ],

    dependency_links=[
        'http://github.com/bezaban/firstline/tarball/master#egg=firstline'
    ]
```

## usage

Helper classes at top level

Standalone functions in helpers.* 


```
import firstline as fl

log = fl.helpers.setuplog(__package__, debug=debug)

config = fl.ConfigHandler('config.json', default_config, interactive)

```
