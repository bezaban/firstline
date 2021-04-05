<div class="document">

<div class="documentwrapper">

<div class="body" role="main">

<div id="module-firstline" class="section">

<span id="firstline-package"></span>

# firstline package[¶](#module-firstline "Permalink to this headline")

<div id="subpackages" class="section">

## Subpackages[¶](#subpackages "Permalink to this headline")

<div class="toctree-wrapper compound">

  - [firstline.helpers package](firstline.helpers.md)
      - [Submodules](firstline.helpers.md#submodules)
      - [firstline.helpers.helpers
        module](firstline.helpers.md#module-firstline.helpers.helpers)

</div>

</div>

<div id="submodules" class="section">

## Submodules[¶](#submodules "Permalink to this headline")

</div>

<div id="module-firstline.confighandler" class="section">

<span id="firstline-confighandler-module"></span>

## firstline.confighandler module[¶](#module-firstline.confighandler "Permalink to this headline")

  - *<span class="pre">class</span>*
    `firstline.confighandler.ConfigHandler`<span class="sig-paren">(</span>*<span class="n"><span class="pre">configfile</span></span>*,
    *<span class="n"><span class="pre">default\_config</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*,
    *<span class="n"><span class="pre">interactive</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span>[¶](#firstline.confighandler.ConfigHandler "Permalink to this definition")  
    Bases: `object`
    
      - `add_path_entry`<span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*,
        *<span class="n"><span class="pre">Path</span></span>*<span class="sig-paren">)</span>[¶](#firstline.confighandler.ConfigHandler.add_path_entry "Permalink to this definition")
    
    <!-- end list -->
    
      - `get_hostname`<span class="sig-paren">(</span><span class="sig-paren">)</span>[¶](#firstline.confighandler.ConfigHandler.get_hostname "Permalink to this definition")
    
    <!-- end list -->
    
      - `get_kv`<span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span>[¶](#firstline.confighandler.ConfigHandler.get_kv "Permalink to this definition")
    
    <!-- end list -->
    
      - `set_kv`<span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*,
        *<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span>[¶](#firstline.confighandler.ConfigHandler.set_kv "Permalink to this definition")
    
    <!-- end list -->
    
      - `set_list`<span class="sig-paren">(</span><span class="sig-paren">)</span>[¶](#firstline.confighandler.ConfigHandler.set_list "Permalink to this definition")
    
    <!-- end list -->
    
      - `set_list_item`<span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*,
        *<span class="n"><span class="pre">value</span></span>*<span class="sig-paren">)</span>[¶](#firstline.confighandler.ConfigHandler.set_list_item "Permalink to this definition")

</div>

<div id="module-firstline.pidfile" class="section">

<span id="firstline-pidfile-module"></span>

## firstline.pidfile module[¶](#module-firstline.pidfile "Permalink to this headline")

  - *<span class="pre">class</span>*
    `firstline.pidfile.Pidfile`<span class="sig-paren">(</span>*<span class="n"><span class="pre">pidfile</span></span>*<span class="sig-paren">)</span>[¶](#firstline.pidfile.Pidfile "Permalink to this definition")  
    Bases: `object`
    
      - `getpid`<span class="sig-paren">(</span><span class="sig-paren">)</span>[¶](#firstline.pidfile.Pidfile.getpid "Permalink to this definition")
    
    <!-- end list -->
    
      - `remove`<span class="sig-paren">(</span><span class="sig-paren">)</span>[¶](#firstline.pidfile.Pidfile.remove "Permalink to this definition")

</div>

</div>

</div>

</div>

<div class="clearer">

</div>

</div>

<div class="footer">

©2021, Paul Bergene | Powered by
[Sphinx 3.5.3](https://www.sphinx-doc.org/),
[pandoc](https://pandoc.org), GNU Make with a sprinkle of duct tape.

</div>
