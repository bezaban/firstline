::: {.document}
::: {.documentwrapper}
::: {.bodywrapper}
::: {.body role="main"}
Source code for firstline.pidfile
=================================

::: {.highlight}

    import os
    import logging

    [docs]class Pidfile:

        def __init__(self, pidfile):

            self.log = logging.getLogger()
            self.pidfile = pidfile

            self.pid = str(os.getpid()) 
        
            self.log.debug('Writing pid %s to pidfile %s' % (self.pid, self.pidfile))
            
            self.pidfilehandler = open(self.pidfile, 'w')
            self.pidfilehandler.write(self.pid)
            self.pidfilehandler.close()

    [docs]    def remove(self):
            self.log.debug('Removing pidfile %s' % self.pidfile)
            os.remove(self.pidfile)

    [docs]    def getpid(self):
            return self.pid
:::
:::
:::
:::

::: {.sphinxsidebar role="navigation" aria-label="main navigation"}
::: {.sphinxsidebarwrapper}
[firstline](../../index.md) {#firstline .logo}
===========================

### Navigation

[Contents:]{.caption-text}

-   [firstline package](../../firstline.md){.reference .internal}
-   [firstline](../../modules.md){.reference .internal}

::: {.relations}
### Related Topics

-   [Documentation overview](../../index.md)
    -   [Module code](../index.md)
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
