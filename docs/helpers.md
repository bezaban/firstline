::: {.document}
::: {.documentwrapper}
::: {.bodywrapper}
::: {.body role="main"}
Source code for firstline.helpers.helpers
=========================================

::: {.highlight}
    import os.path
    import logging

    log = logging.getLogger()

    [docs]def getlogconfig(filename, debug=False):

        if os.path.isdir('log'):
            filename = 'log/{0}'.format(filename)

        logging_config = {
            'version': 1,
            'formatters': {
                'standard': {
                    'format': '[%(asctime)s] [%(levelname)s] %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S'
                }
            },

            'handlers': {
                'default': { 
                    'level': 'INFO',
                    'formatter': 'standard',
                    'class': 'logging.FileHandler',
                    'filename': filename,
                    'mode': 'a',
                },
                'debug': { 
                    'level': 'DEBUG',
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://sys.stdout'
                }
            },
            'loggers': { 
                '': {  # root logger
                    'handlers': ['default'],
                    'level': 'INFO',
                    'propagate': False
                }
            }
        }

        if debug:
            logging_config['loggers']['']['handlers'] = ['default', 'debug']
            logging_config['handlers']['default']['level'] = 'DEBUG' 
            logging_config['loggers']['']['level'] = 'DEBUG' 

        return logging_config
:::
:::
:::
:::

::: {.sphinxsidebar role="navigation" aria-label="main navigation"}
::: {.sphinxsidebarwrapper}
[firstline](../../../index.md) {#firstline .logo}
==============================

### Navigation

[Contents:]{.caption-text}

-   [firstline package](../../../firstline.md){.reference .internal}
-   [firstline](../../../modules.md){.reference .internal}

::: {.relations}
### Related Topics

-   [Documentation overview](../../../index.md)
    -   [Module code](../../index.md)
:::

::: {#searchbox style="display: none" role="search"}
### Quick search {#searchlabel}

::: {.searchformwrapper}
:::
:::
:::
:::

::: {.clearer}
:::
:::

::: {.footer}
©2021, Author. \| Powered by [Sphinx 3.5.3](http://sphinx-doc.org/) &
[Alabaster 0.7.12](https://github.com/bitprophet/alabaster)
:::
