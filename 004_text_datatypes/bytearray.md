<!-- wp:paragraph -->
<p>In the previous tutorials the <strong>immutable</strong> string class and byte class were examined. The byte class in particular is an <strong>immutable</strong> Sequence of byte values. Immutable means that once an instance is instantiated, it cannot be modified. The bytearray is a <strong>mutable</strong> Sequence of byte values which means that it can be modified after instantiation. Because the bytearray is a mutable version of the byte, it has consistent data model identifiers to the byte and most of these previously used identifiers can be considered as read only identifiers. The bytearray also has mutable identifiers which can be considered as write identifiers which update the bytearray in place.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Initialisation</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Inputting bytearray() will display the docstring of the initialisation signature of the byte class as a popup balloon. Recall some IDEs such as JupyterLab may require the keypress shift ⇧ and tab ↹ to invoke the docstring:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Init signature:  bytearray(self, /, *args, **kwargs)
Docstring:     
bytearray(iterable_of_ints) -> bytearray
bytearray(string, encoding[, errors]) -> bytearray
bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
bytearray() -> empty bytes array

Construct a mutable bytearray object from:
  - an iterable yielding integers in range(256)
  - a text string encoded using the specified encoding
  - a bytes or a buffer object
  - any object implementing the buffer API.
  - an integer
Type:           type
Subclasses:     </pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p> The initialisation signature of the bytearray is consistent with that of the byte. For simplicity a bytearray will be constructed from an ASCII string and encoding of ASCII:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_r = bytes('Γειά σου Κόσμε!', encoding='UTF-8')\ngreeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_r \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_r = bytes('Γειά σου Κόσμε!', encoding='UTF-8')
greeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_r </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_rw </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Identifiers</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If the identifiers of greeting_r are examined, the following immutable functions are observed. These all return a value:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>capitalize - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>center - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>count - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>decode - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>endswith - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>expandtabs - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>find - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>fromhex - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>hex - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>index - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>isalnum - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>isalpha - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>isascii - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>isdigit - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>islower - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>isspace - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>istitle - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>isupper - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>join - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>ljust - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>lower - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>lstrip - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>maketrans - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>partition - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>removeprefix - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>removesuffix - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>replace - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>rfind - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>rindex - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>rjust - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>rpartition - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>rsplit - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>rstrip - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>split - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>splitlines - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>startswith - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>strip - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>swapcase - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>title - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>translate - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>upper - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>zfill - function</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>If the identifiers of greeting_rw are examined, all the identifiers of greeting_r are seen in addition to the following immutable functions. Most of the mutable functions do not return a value and instead update the bytearray instance in place:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>append - mutable function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>clear - mutable function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>extend - mutable function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>insert - mutable function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>pop - mutable function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>remove - mutable function</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The exception is pop which both returns a value and updates the bytearray in place.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If the identifiers of greeting_r are examined, the following are observed:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>__add__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__bytes__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__class__ - class</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__contains__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__delattr__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__dir__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__doc__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__eq__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__format__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__ge__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__getattribute__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__getitem__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__getnewargs__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__getstate__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__gt__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__hash__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__init__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__init_subclass__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__iter__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__le__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__len__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__lt__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__mod__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__mul__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__ne__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__new__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__reduce__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__reduce_ex__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__repr__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__rmod__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__rmul__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__setattr__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__sizeof__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__str__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__subclasshook__ - function</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>If the data model identifiers of greeting_rw are examined, all the data model identifiers of greeting_r are seen in addition to the following immutable data model identifiers:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>__alloc__ - function</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__delitem__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__setitem__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__iadd__ - instance</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>__imul__ - instance</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>A MutableSequence typically has __setitem__ and __delitem__ which complement __getitem__ from the (immutable) Sequence. A MutableSequence also has the append, reverse, extend, pop, remove identifiers. Finally it has the in place operators such as __iadd__ and __imul__.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Recall that details about each of the identifiers can be seen by using help on the bytearray class:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"help(bytearray)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehelp\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="help(bytearray)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">help</span><span style="color: #24292E">(</span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>Help on class bytearray in module builtins:

class bytearray(object)
 |  bytearray(iterable_of_ints) -> bytearray
 |  bytearray(string, encoding&#91;, errors]) -> bytearray
 |  bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
 |  bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
 |  bytearray() -> empty bytes array
 |  
 |  Construct a mutable bytearray object from:
 |    - an iterable yielding integers in range(256)
 |    - a text string encoded using the specified encoding
 |    - a bytes or a buffer object
 |    - any object implementing the buffer API.
 |    - an integer
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __alloc__(...)
 |      B.__alloc__() -> int
 |      
 |      Return the number of bytes actually allocated.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self&#91;key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self&#91;key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self&lt;=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self&lt;value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |  
 |  __reduce_ex__(self, proto=0, /)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self&#91;key] to value.
 |  
 |  __sizeof__(self, /)
 |      Returns the size of the bytearray object in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  append(self, item, /)
 |      Append a single item to the end of the bytearray.
 |      
 |      item
 |        The item to be appended.
 |  
 |  capitalize(...)
 |      B.capitalize() -> copy of B
 |      
 |      Return a copy of B with only its first character capitalized (ASCII)
 |      and the rest lower-cased.
 |  
 |  center(self, width, fillchar=b' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character.
 |  
 |  clear(self, /)
 |      Remove all items from the bytearray.
 |  
 |  copy(self, /)
 |      Return a copy of B.
 |  
 |  count(...)
 |      B.count(sub&#91;, start&#91;, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of subsection sub in
 |      bytes B&#91;start:end].  Optional arguments start and end are interpreted
 |      as in slice notation.
 |  
 |  decode(self, /, encoding='utf-8', errors='strict')
 |      Decode the bytearray using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding with which to decode the bytearray.
 |      errors
 |        The error handling scheme to use for the handling of decoding errors.
 |        The default is 'strict' meaning that decoding errors raise a
 |        UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
 |        as well as any other name registered with codecs.register_error that
 |        can handle UnicodeDecodeErrors.
 |  
 |  endswith(...)
 |      B.endswith(suffix&#91;, start&#91;, end]]) -> bool
 |      
 |      Return True if B ends with the specified suffix, False otherwise.
 |      With optional start, test B beginning at that position.
 |      With optional end, stop comparing B at that position.
 |      suffix can also be a tuple of bytes to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  extend(self, iterable_of_ints, /)
 |      Append all the items from the iterator or sequence to the end of the bytearray.
 |      
 |      iterable_of_ints
 |        The iterable of items to append.
 |  
 |  find(...)
 |      B.find(sub&#91;, start&#91;, end]]) -> int
 |      
 |      Return the lowest index in B where subsection sub is found,
 |      such that sub is contained within B&#91;start,end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  hex(...)
 |      Create a string of hexadecimal numbers from a bytearray object.
 |      
 |        sep
 |          An optional single character or byte to separate hex bytes.
 |        bytes_per_sep
 |          How many bytes between separators.  Positive values count from the
 |          right, negative values count from the left.
 |      
 |      Example:
 |      >>> value = bytearray(&#91;0xb9, 0x01, 0xef])
 |      >>> value.hex()
 |      'b901ef'
 |      >>> value.hex(':')
 |      'b9:01:ef'
 |      >>> value.hex(':', 2)
 |      'b9:01ef'
 |      >>> value.hex(':', -2)
 |      'b901:ef'
 |  
 |  index(...)
 |      B.index(sub&#91;, start&#91;, end]]) -> int
 |      
 |      Return the lowest index in B where subsection sub is found,
 |      such that sub is contained within B&#91;start,end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the subsection is not found.
 |  
 |  insert(self, index, item, /)
 |      Insert a single item into the bytearray before the given index.
 |      
 |      index
 |        The index where the value is to be inserted.
 |      item
 |        The item to be inserted.
 |  
 |  isalnum(...)
 |      B.isalnum() -> bool
 |      
 |      Return True if all characters in B are alphanumeric
 |      and there is at least one character in B, False otherwise.
 |  
 |  isalpha(...)
 |      B.isalpha() -> bool
 |      
 |      Return True if all characters in B are alphabetic
 |      and there is at least one character in B, False otherwise.
 |  
 |  isascii(...)
 |      B.isascii() -> bool
 |      
 |      Return True if B is empty or all characters in B are ASCII,
 |      False otherwise.
 |  
 |  isdigit(...)
 |      B.isdigit() -> bool
 |      
 |      Return True if all characters in B are digits
 |      and there is at least one character in B, False otherwise.
 |  
 |  islower(...)
 |      B.islower() -> bool
 |      
 |      Return True if all cased characters in B are lowercase and there is
 |      at least one cased character in B, False otherwise.
 |  
 |  isspace(...)
 |      B.isspace() -> bool
 |      
 |      Return True if all characters in B are whitespace
 |      and there is at least one character in B, False otherwise.
 |  
 |  istitle(...)
 |      B.istitle() -> bool
 |      
 |      Return True if B is a titlecased string and there is at least one
 |      character in B, i.e. uppercase characters may only follow uncased
 |      characters and lowercase characters only cased ones. Return False
 |      otherwise.
 |  
 |  isupper(...)
 |      B.isupper() -> bool
 |      
 |      Return True if all cased characters in B are uppercase and there is
 |      at least one cased character in B, False otherwise.
 |  
 |  join(self, iterable_of_bytes, /)
 |      Concatenate any number of bytes/bytearray objects.
 |      
 |      The bytearray whose method is called is inserted in between each pair.
 |      
 |      The result is returned as a new bytearray object.
 |  
 |  ljust(self, width, fillchar=b' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character.
 |  
 |  lower(...)
 |      B.lower() -> copy of B
 |      
 |      Return a copy of B with all ASCII characters converted to lowercase.
 |  
 |  lstrip(self, bytes=None, /)
 |      Strip leading bytes contained in the argument.
 |      
 |      If the argument is omitted or None, strip leading ASCII whitespace.
 |  
 |  partition(self, sep, /)
 |      Partition the bytearray into three parts using the given separator.
 |      
 |      This will search for the separator sep in the bytearray. If the separator is
 |      found, returns a 3-tuple containing the part before the separator, the
 |      separator itself, and the part after it as new bytearray objects.
 |      
 |      If the separator is not found, returns a 3-tuple containing the copy of the
 |      original bytearray object and two empty bytearray objects.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return a single item from B.
 |      
 |        index
 |          The index from where to remove the item.
 |          -1 (the default value) means remove the last item.
 |      
 |      If no index argument is given, will pop the last item.
 |  
 |  remove(self, value, /)
 |      Remove the first occurrence of a value in the bytearray.
 |      
 |      value
 |        The value to remove.
 |  
 |  removeprefix(self, prefix, /)
 |      Return a bytearray with the given prefix string removed if present.
 |      
 |      If the bytearray starts with the prefix string, return
 |      bytearray&#91;len(prefix):].  Otherwise, return a copy of the original
 |      bytearray.
 |  
 |  removesuffix(self, suffix, /)
 |      Return a bytearray with the given suffix string removed if present.
 |      
 |      If the bytearray ends with the suffix string and that suffix is not
 |      empty, return bytearray&#91;:-len(suffix)].  Otherwise, return a copy of
 |      the original bytearray.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  reverse(self, /)
 |      Reverse the order of the values in B in place.
 |  
 |  rfind(...)
 |      B.rfind(sub&#91;, start&#91;, end]]) -> int
 |      
 |      Return the highest index in B where subsection sub is found,
 |      such that sub is contained within B&#91;start,end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      B.rindex(sub&#91;, start&#91;, end]]) -> int
 |      
 |      Return the highest index in B where subsection sub is found,
 |      such that sub is contained within B&#91;start,end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raise ValueError when the subsection is not found.
 |  
 |  rjust(self, width, fillchar=b' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character.
 |  
 |  rpartition(self, sep, /)
 |      Partition the bytearray into three parts using the given separator.
 |      
 |      This will search for the separator sep in the bytearray, starting at the end.
 |      If the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it as new bytearray
 |      objects.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty bytearray
 |      objects and the copy of the original bytearray object.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the sections in the bytearray, using sep as the delimiter.
 |      
 |        sep
 |          The delimiter according which to split the bytearray.
 |          None (the default value) means split on ASCII whitespace characters
 |          (space, tab, return, newline, formfeed, vertical tab).
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splitting is done starting at the end of the bytearray and working to the front.
 |  
 |  rstrip(self, bytes=None, /)
 |      Strip trailing bytes contained in the argument.
 |      
 |      If the argument is omitted or None, strip trailing ASCII whitespace.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the sections in the bytearray, using sep as the delimiter.
 |      
 |      sep
 |        The delimiter according which to split the bytearray.
 |        None (the default value) means split on ASCII whitespace characters
 |        (space, tab, return, newline, formfeed, vertical tab).
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the bytearray, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      B.startswith(prefix&#91;, start&#91;, end]]) -> bool
 |      
 |      Return True if B starts with the specified prefix, False otherwise.
 |      With optional start, test B beginning at that position.
 |      With optional end, stop comparing B at that position.
 |      prefix can also be a tuple of bytes to try.
 |  
 |  strip(self, bytes=None, /)
 |      Strip leading and trailing bytes contained in the argument.
 |      
 |      If the argument is omitted or None, strip leading and trailing ASCII whitespace.
 |  
 |  swapcase(...)
 |      B.swapcase() -> copy of B
 |      
 |      Return a copy of B with uppercase ASCII characters converted
 |      to lowercase ASCII and vice versa.
 |  
 |  title(...)
 |      B.title() -> copy of B
 |      
 |      Return a titlecased version of B, i.e. ASCII words start with uppercase
 |      characters, all remaining cased characters have lowercase.
 |  
 |  translate(self, table, /, delete=b'')
 |      Return a copy with each character mapped by the given translation table.
 |      
 |        table
 |          Translation table, which must be a bytes object of length 256.
 |      
 |      All characters occurring in the optional argument delete are removed.
 |      The remaining characters are mapped through the given translation table.
 |  
 |  upper(...)
 |      B.upper() -> copy of B
 |      
 |      Return a copy of B with all ASCII characters converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The original string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromhex(string, /) from builtins.type
 |      Create a bytearray object from a string of hexadecimal numbers.
 |      
 |      Spaces between two numbers are accepted.
 |      Example: bytearray.fromhex('B9 01EF') -> bytearray(b'\\xb9\\x01\\xef')
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(frm, to, /)
 |      Return a translation table useable for the bytes or bytearray translate method.
 |      
 |      The returned table will be one where each byte in frm is mapped to the byte at
 |      the same position in to.
 |      
 |      The bytes objects frm and to must be of the same length.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading">hash</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Notice under data and other attributes that __hash__ = None. The value of a mutable data type is not fixed and therefore does not have a hash value, because it has no has value it cannot be used as a key in a mapping such as a dictionary:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"colors = {'red': '#ff0000',\n          'green': '#00b050',\n          'blue': '#0070c0'}\n          \ncolors['red']","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ecolors \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e {\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;red\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e: \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;#ff0000\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e          \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;green\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e: \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;#00b050\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e          \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;blue\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e: \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;#0070c0\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e}\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e          \u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ecolors[\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;red\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="colors = {'red': '#ff0000',
          'green': '#00b050',
          'blue': '#0070c0'}
          
colors['red']" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">colors </span><span style="color: #D73A49">=</span><span style="color: #24292E"> {</span><span style="color: #032F62">&#39;red&#39;</span><span style="color: #24292E">: </span><span style="color: #032F62">&#39;#ff0000&#39;</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">          </span><span style="color: #032F62">&#39;green&#39;</span><span style="color: #24292E">: </span><span style="color: #032F62">&#39;#00b050&#39;</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">          </span><span style="color: #032F62">&#39;blue&#39;</span><span style="color: #24292E">: </span><span style="color: #032F62">&#39;#0070c0&#39;</span><span style="color: #24292E">}</span></span>
<span class="line"><span style="color: #24292E">          </span></span>
<span class="line"><span style="color: #24292E">colors[</span><span style="color: #032F62">&#39;red&#39;</span><span style="color: #24292E">]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'#ff0000'</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"colors = {bytes('red', encoding='ascii'): '#ff0000',\n          bytes('green', encoding='ascii'): '#00b050',\n          bytes('blue', encoding='ascii'): '#0070c0'}\n          \ncolors[bytes('red', encoding='ascii')]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ecolors \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e {\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;red\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ascii\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e): \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;#ff0000\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e          \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;green\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ascii\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e): \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;#00b050\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e          \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;blue\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ascii\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e): \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;#0070c0\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e}\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e          \u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ecolors[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;red\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ascii\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="colors = {bytes('red', encoding='ascii'): '#ff0000',
          bytes('green', encoding='ascii'): '#00b050',
          bytes('blue', encoding='ascii'): '#0070c0'}
          
colors[bytes('red', encoding='ascii')]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">colors </span><span style="color: #D73A49">=</span><span style="color: #24292E"> {</span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;red&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ascii&#39;</span><span style="color: #24292E">): </span><span style="color: #032F62">&#39;#ff0000&#39;</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">          </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;green&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ascii&#39;</span><span style="color: #24292E">): </span><span style="color: #032F62">&#39;#00b050&#39;</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">          </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;blue&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ascii&#39;</span><span style="color: #24292E">): </span><span style="color: #032F62">&#39;#0070c0&#39;</span><span style="color: #24292E">}</span></span>
<span class="line"><span style="color: #24292E">          </span></span>
<span class="line"><span style="color: #24292E">colors[</span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;red&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ascii&#39;</span><span style="color: #24292E">)]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'#ff0000'</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"colors = {bytearray('red', encoding='ascii'): '#ff0000',\n          bytearray('green', encoding='ascii'): '#00b050',\n          bytearray('blue', encoding='ascii'): '#0070c0'}\n          \ncolors[bytearray('red', encoding='ascii')]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ecolors \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e {\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;red\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ascii\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e): \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;#ff0000\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e          \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;green\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ascii\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e): \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;#00b050\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e          \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;blue\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ascii\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e): \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;#0070c0\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e}\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e          \u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ecolors[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;red\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ascii\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="colors = {bytearray('red', encoding='ascii'): '#ff0000',
          bytearray('green', encoding='ascii'): '#00b050',
          bytearray('blue', encoding='ascii'): '#0070c0'}
          
colors[bytearray('red', encoding='ascii')]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">colors </span><span style="color: #D73A49">=</span><span style="color: #24292E"> {</span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;red&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ascii&#39;</span><span style="color: #24292E">): </span><span style="color: #032F62">&#39;#ff0000&#39;</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">          </span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;green&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ascii&#39;</span><span style="color: #24292E">): </span><span style="color: #032F62">&#39;#00b050&#39;</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">          </span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;blue&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ascii&#39;</span><span style="color: #24292E">): </span><span style="color: #032F62">&#39;#0070c0&#39;</span><span style="color: #24292E">}</span></span>
<span class="line"><span style="color: #24292E">          </span></span>
<span class="line"><span style="color: #24292E">colors[</span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;red&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ascii&#39;</span><span style="color: #24292E">)]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>TypeError: unhashable type: 'bytearray'</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Mutable Methods</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Supposing the two instances are created:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_r = bytes('Γειά σου Κόσμε!', encoding='UTF-8')\ngreeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')\ngreeting_r\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_r \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_r\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_r = bytes('Γειά σου Κόσμε!', encoding='UTF-8')
greeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')
greeting_r
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_r </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_rw </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_r</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!'

bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>In both cases the 2 bytes corresponding to each Greek letters are shown as escape characters and the bytes corresponding to the ASCII characters ' ' and '!' are automatically decoded and displayed. Notice the formal representation for the bytearray involves the byte, indicating how close these two classes are.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The bytes instance is immutable and can be thought of as being read only while the bytearray instance is mutable and can be thought of as being read write. If the data model method __getitem__ is examined:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:       greeting_rw.__getitem__(key, /)
Call signature:  greeting_rw.__getitem__(*args, **kwargs)
Type:           method-wrapper
String form:    &lt;method-wrapper '__getitem__' of bytearray object at 0x00000201D230E3F0>
Docstring:      Return self[key].</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>The byte at 0 can be indexed from either Sequence using square brackets:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_r[0]\ngreeting_rw[0]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_r[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_r[0]
greeting_rw[0]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_r[</span><span style="color: #005CC5">0</span><span style="color: #24292E">]</span></span>
<span class="line"><span style="color: #24292E">greeting_rw[</span><span style="color: #005CC5">0</span><span style="color: #24292E">]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>206
206</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Recall this is easier to conceptualise in hexadecimal:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">greeting_rw.hex()
hex(greeting_rw[0]).removeprefix('0x')</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ce93ceb5ceb9ceac20cf83cebfcf8520ce9acf8ccf83cebcceb521'
'ce'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>And:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"hex(206)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e206\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="hex(206)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">hex</span><span style="color: #24292E">(</span><span style="color: #005CC5">206</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0xce'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Slicing can also be used to return a slice</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_r[0:2]\ngreeting_rw[0:2]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_r[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_r[0:2]
greeting_rw[0:2]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_r[</span><span style="color: #005CC5">0</span><span style="color: #24292E">:</span><span style="color: #005CC5">2</span><span style="color: #24292E">]</span></span>
<span class="line"><span style="color: #24292E">greeting_rw[</span><span style="color: #005CC5">0</span><span style="color: #24292E">:</span><span style="color: #005CC5">2</span><span style="color: #24292E">]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'\xce\x93'
bytearray(b'\xce\x93')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The bytearray also has the equivalent write data model identifiers __setitem__ and __delitem__:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:       bytearray.__setitem__(self, key, value, /)
Call signature:  bytearray.__setitem__(*args, **kwargs)
Type:           wrapper_descriptor
String form:    &lt;slot wrapper '__setitem__' of 'bytearray' objects>
Namespace:      Python builtin
Docstring:      Set self[key] to value.</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:       bytearray.__delitem__(self, key, /)
Call signature:  bytearray.__delitem__(*args, **kwargs)
Type:           wrapper_descriptor
String form:    &lt;slot wrapper '__delitem__' of 'bytearray' objects>
Namespace:      Python builtin
Docstring:      Delete self[key].</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>This means that the value at index 0 can be reassigned to another byte:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw[0] = 0xde\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e] \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ede\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw[0] = 0xde
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw[</span><span style="color: #005CC5">0</span><span style="color: #24292E">] </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">de</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xde\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>If the bytearray is decoded:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.decode(encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.decode(\u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.decode(encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.decode(</span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ޓειά σου Κόσμε!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The first character corresponding to the two bytes b'xde\xce' is replaced by the character corresponding to the two bytes b'xce\xce'.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Attempting to do the same with the bytes will give a TypeError:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_r[0] = 0xde","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_r[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e] \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ede\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_r[0] = 0xde" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_r[</span><span style="color: #005CC5">0</span><span style="color: #24292E">] </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">de</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>TypeError: 'bytes' object does not support item assignment</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>In the bytearray, an individual byte can also be deleted:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"del greeting_rw[0]\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003edel\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e greeting_rw[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="del greeting_rw[0]
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">del</span><span style="color: #24292E"> greeting_rw[</span><span style="color: #005CC5">0</span><span style="color: #24292E">]</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Note all subsequent bytes will have their index value lowered by 1.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Attempting to decode this gives a UnicodeDecodeError:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.decode(encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.decode(\u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.decode(encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.decode(</span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>UnicodeDecodeError: 'utf-8' codec can't decode byte 0x93 in position 0: invalid start byte</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>If the other byte that originally encoded the first character is also deleted:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"del greeting_rw[0]\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003edel\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e greeting_rw[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="del greeting_rw[0]
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">del</span><span style="color: #24292E"> greeting_rw[</span><span style="color: #005CC5">0</span><span style="color: #24292E">]</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Now the bytearray can be decoded:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.decode(encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.decode(\u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.decode(encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.decode(</span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ειά σου Κόσμε!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The bytearray also has following mutable methods:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>append</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>extend</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>insert</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>remove</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>clear</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>reverse</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>And:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>pop</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The mutable methods above all mutate the original bytearray and have no return value. The exception is pop which mutates the original bytearray and returns a value.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>append is used to append a single integer to the bytearray. The integer must be &lt;256 and corresponds to the byte. Because the input argument is before a /, it must be provided positionally.</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  greeting_rw.append(item, /)
Docstring:
Append a single item to the end of the bytearray.

item
  The item to be appended.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>Supposing the following bytearray is created:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The letter 'a' can be appended using its ordinal value of 97:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.append(97)\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.append(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e97\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.append(97)
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.append(</span><span style="color: #005CC5">97</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!a')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Recall that:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"chr(97)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003echr\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e97\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="chr(97)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">chr</span><span style="color: #24292E">(</span><span style="color: #005CC5">97</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'a'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>And:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"hex(97)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e97\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="hex(97)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">hex</span><span style="color: #24292E">(</span><span style="color: #005CC5">97</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0x61'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>However as the byte 61 is the ASCII character 'a', 'a' displays instead of \x61 in the above.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Notice what happens if the letter 'b' is appended using its ordinal value and assigned to a result:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"result = greeting_rw.append(98)\nresult","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eresult \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e greeting_rw.append(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e98\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eresult\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="result = greeting_rw.append(98)
result" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">result </span><span style="color: #D73A49">=</span><span style="color: #24292E"> greeting_rw.append(</span><span style="color: #005CC5">98</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">result</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code></code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Because the mutable method append has no return value, the value assigned to result is None and this can be seen in the Variable Explorer.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":58135,"sizeSlug":"full","linkDestination":"media"} -->
<figure class="wp-block-image size-full"><a href="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image.png"><img src="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image.png" alt="" class="wp-image-58135"/></a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Unfortunately at the time of writing the bytearray is not fully supported within the Variable Explorer. Its contents can be seen by inputting the instance name into an ipython cell:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!ab')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>It is seen to be updated in place. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A simple custom function can be created with a return value:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"def fun1():\n    return 'hello'","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003edef\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #6F42C1\u0022\u003efun1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e():\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ereturn\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;hello\u0026#39;\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="def fun1():
    return 'hello'" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">def</span><span style="color: #24292E"> </span><span style="color: #6F42C1">fun1</span><span style="color: #24292E">():</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #D73A49">return</span><span style="color: #24292E"> </span><span style="color: #032F62">&#39;hello&#39;</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>If this function is called and assigned to a Variable. The Variable will have the returned value:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting = fun1()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e fun1()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting = fun1()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting </span><span style="color: #D73A49">=</span><span style="color: #24292E"> fun1()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:image {"id":58157,"sizeSlug":"full","linkDestination":"media"} -->
<figure class="wp-block-image size-full"><a href="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-2.png"><img src="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-2.png" alt="" class="wp-image-58157"/></a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If instead the function explicitly has no return value:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"def fun2():\n    return None","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003edef\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #6F42C1\u0022\u003efun2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e():\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ereturn\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eNone\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="def fun2():
    return None" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">def</span><span style="color: #24292E"> </span><span style="color: #6F42C1">fun2</span><span style="color: #24292E">():</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #D73A49">return</span><span style="color: #24292E"> </span><span style="color: #005CC5">None</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>If this function is called and assigned to a Variable. The Variable will have the returned value which is explicitly None:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"empty = fun2()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eempty \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e fun2()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="empty = fun2()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">empty </span><span style="color: #D73A49">=</span><span style="color: #24292E"> fun2()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:image {"id":58161,"sizeSlug":"full","linkDestination":"media"} -->
<figure class="wp-block-image size-full"><a href="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-3.png"><img src="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-3.png" alt="" class="wp-image-58161"/></a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The above function can also implicitly have a None value using:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"def fun2():\n    return","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003edef\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #6F42C1\u0022\u003efun2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e():\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ereturn\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="def fun2():
    return" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">def</span><span style="color: #24292E"> </span><span style="color: #6F42C1">fun2</span><span style="color: #24292E">():</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #D73A49">return</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>Or execute some other lines of code with no return statement:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"def fun2():\n    1 + 2","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003edef\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #6F42C1\u0022\u003efun2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e():\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="def fun2():
    1 + 2" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">def</span><span style="color: #24292E"> </span><span style="color: #6F42C1">fun2</span><span style="color: #24292E">():</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #005CC5">1</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>Some other functions may also use the keyword pass: </p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"def fun2():\n    pass","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003edef\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #6F42C1\u0022\u003efun2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e():\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003epass\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="def fun2():
    pass" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">def</span><span style="color: #24292E"> </span><span style="color: #6F42C1">fun2</span><span style="color: #24292E">():</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #D73A49">pass</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>Note care needs to be made when using reassignment with a method that has no return value. For example in the case below:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw = greeting_rw.append(99)\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e greeting_rw.append(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e99\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw = greeting_rw.append(99)
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw </span><span style="color: #D73A49">=</span><span style="color: #24292E"> greeting_rw.append(</span><span style="color: #005CC5">99</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code></code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":58139,"sizeSlug":"full","linkDestination":"media"} -->
<figure class="wp-block-image size-full"><a href="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-1.png"><img src="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-1.png" alt="" class="wp-image-58139"/></a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>greeting_rw has been reassigned to the return value which was None.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The extend method is used to assign an iterable of integers to the bytearray, this iterable is typically another bytearray however can be a byte or a tuple of integers:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  greeting_rw.extend(iterable_of_ints, /)
Docstring:
Append all the items from the iterator or sequence to the end of the bytearray.

iterable_of_ints
  The iterable of items to append.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>Returning to the original bytearray:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!')</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.extend(b'abc')\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.extend(\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003eb\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;abc\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.extend(b'abc')
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.extend(</span><span style="color: #D73A49">b</span><span style="color: #032F62">&#39;abc&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!abc')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The uppercase letters 'A', 'B' and 'C' have an ordinal value of 65, 66 and 67:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.extend((65, 66, 67))\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.extend((\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e65\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e66\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e67\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e))\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.extend((65, 66, 67))
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.extend((</span><span style="color: #005CC5">65</span><span style="color: #24292E">, </span><span style="color: #005CC5">66</span><span style="color: #24292E">, </span><span style="color: #005CC5">67</span><span style="color: #24292E">))</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!abcABC')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The insert method is similar to the append method. An index value where the item to be inserted is required as the first input argument and the item to be inserted is the second input argument. Because the input arguments are before a /, they must be provided positionally.</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  greeting_rw.insert(index, item, /)
Docstring:
Insert a single item into the bytearray before the given index.

index
  The index where the value is to be inserted.
item
  The item to be inserted.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>A for loop will be used to view the index and value of each byte in the byte array:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"for index, b in enumerate(greeting_rw):\n    print(f'{index}: {hex(b)}')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003efor\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e index, b \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ein\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eenumerate\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greeting_rw):\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eprint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ef\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e{\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eindex\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e}\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e: \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e{hex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(b)\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e}\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="for index, b in enumerate(greeting_rw):
    print(f'{index}: {hex(b)}')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">for</span><span style="color: #24292E"> index, b </span><span style="color: #D73A49">in</span><span style="color: #24292E"> </span><span style="color: #005CC5">enumerate</span><span style="color: #24292E">(greeting_rw):</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #005CC5">print</span><span style="color: #24292E">(</span><span style="color: #D73A49">f</span><span style="color: #032F62">&#39;</span><span style="color: #005CC5">{</span><span style="color: #24292E">index</span><span style="color: #005CC5">}</span><span style="color: #032F62">: </span><span style="color: #005CC5">{hex</span><span style="color: #24292E">(b)</span><span style="color: #005CC5">}</span><span style="color: #032F62">&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0: 0xce
1: 0x93
2: 0xce
3: 0xb5
4: 0xce
5: 0xb9
6: 0xce
7: 0xac
8: 0x20
9: 0xcf
10: 0x83
11: 0xce
12: 0xbf
13: 0xcf
14: 0x85
15: 0x20
16: 0xce
17: 0x9a
18: 0xcf
19: 0x8c
20: 0xcf
21: 0x83
22: 0xce
23: 0xbc
24: 0xce
25: 0xb5
26: 0x21
27: 0x61
28: 0x62
29: 0x63
30: 0x41
31: 0x42
32: 0x43</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The letter 'D' can be inserted at index 6 using its ordinal value of 68:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.insert(6, 68)\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.insert(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e68\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.insert(6, 68)
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.insert(</span><span style="color: #005CC5">6</span><span style="color: #24292E">, </span><span style="color: #005CC5">68</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9D\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!abcABC')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>All bytes at index 6 and subsequent have their index value increased by a value of 1:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"for index, b in enumerate(greeting_rw):\n    print(f'{index}: {hex(b)}')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003efor\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e index, b \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ein\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eenumerate\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greeting_rw):\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eprint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ef\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e{\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eindex\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e}\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e: \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e{hex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(b)\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e}\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="for index, b in enumerate(greeting_rw):
    print(f'{index}: {hex(b)}')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">for</span><span style="color: #24292E"> index, b </span><span style="color: #D73A49">in</span><span style="color: #24292E"> </span><span style="color: #005CC5">enumerate</span><span style="color: #24292E">(greeting_rw):</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #005CC5">print</span><span style="color: #24292E">(</span><span style="color: #D73A49">f</span><span style="color: #032F62">&#39;</span><span style="color: #005CC5">{</span><span style="color: #24292E">index</span><span style="color: #005CC5">}</span><span style="color: #032F62">: </span><span style="color: #005CC5">{hex</span><span style="color: #24292E">(b)</span><span style="color: #005CC5">}</span><span style="color: #032F62">&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0: 0xce
1: 0x93
2: 0xce
3: 0xb5
4: 0xce
5: 0xb9
6: 0x44
7: 0xce
8: 0xac
9: 0x20
10: 0xcf
11: 0x83
12: 0xce
13: 0xbf
14: 0xcf
15: 0x85
16: 0x20
17: 0xce
18: 0x9a
19: 0xcf
20: 0x8c
21: 0xcf
22: 0x83
23: 0xce
24: 0xbc
25: 0xce
26: 0xb5
27: 0x21
28: 0x61
29: 0x62
30: 0x63
31: 0x41
32: 0x42
33: 0x43
</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The hex value of 68 is 0x44 which is seen at index 6:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"hex(68)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e68\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="hex(68)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">hex</span><span style="color: #24292E">(</span><span style="color: #005CC5">68</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0x44</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The bytearray can be decoded to a Unicode string using:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.decode(encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.decode(\u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.decode(encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.decode(</span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ΓειDά σου Κόσμε!abcABC'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The remove method can be used to remove the first occurrence of a value in the bytearray:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  greeting_rw.remove(value, /)
Docstring:
Remove the first occurrence of a value in the bytearray.

value
  The value to remove.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>For example, the letter 'D' can be removed using its ordinal value of 68 and the bytearray can once again be decoded to a Unicode string using UTF-8:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.remove(68)\ngreeting_rw.decode(encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.remove(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e68\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.decode(\u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.remove(68)
greeting_rw.decode(encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.remove(</span><span style="color: #005CC5">68</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting_rw.decode(</span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'Γειά σου Κόσμε!abcABC'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The reverse method can be used to reverse the order of bytes in the bytearray:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  greeting_rw.reverse()
Docstring: Reverse the order of the values in B in place.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>For example the bytearray instance can be examined:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!abcABC')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>And then reversed:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.reverse()\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.reverse()\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.reverse()
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.reverse()</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'CBAcba!\xb5\xce\xbc\xce\x83\xcf\x8c\xcf\x9a\xce \x85\xcf\xbf\xce\x83\xcf \xac\xce\xb9\xce\xb5\xce\x93\xce')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Attempting to decode the reversed bytearray to a Unicode string using UTF-8 will likely result in an UnicodeDecodeError:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.decode(encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.decode(\u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.decode(encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.decode(</span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb5 in position 7: invalid start byte</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The bytearray can be cleared using the clear method:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  greeting_rw.clear()
Docstring: Remove all items from the bytearray.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.clear()\ngreeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.clear()\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.clear()
greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.clear()</span></span>
<span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This returns an empty bytearray. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":58176,"sizeSlug":"full","linkDestination":"media"} -->
<figure class="wp-block-image size-full"><a href="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-4.png"><img src="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-4.png" alt="" class="wp-image-58176"/></a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Notice the subtle difference between this and the type None:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw = greeting_rw.clear()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e greeting_rw.clear()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw = greeting_rw.clear()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw </span><span style="color: #D73A49">=</span><span style="color: #24292E"> greeting_rw.clear()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:image {"id":58178,"sizeSlug":"full","linkDestination":"media"} -->
<figure class="wp-block-image size-full"><a href="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-5.png"><img src="https://dellwindowsreinstallationguide.com/wp-content/uploads/2023/05/image-5.png" alt="" class="wp-image-58178"/></a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>None is a different data type and does not have the methods of a bytearray.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let's recreate the bytearray using:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytearray\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw = bytearray('Γειά σου Κόσμε!', encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytearray</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>The method pop can be used to pop of a value using its index:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  greeting_rw.pop(index=-1, /)
Docstring:
Remove and return a single item from B.

  index
    The index from where to remove the item.
    -1 (the default value) means remove the last item.

If no index argument is given, will pop the last item.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>The default index is -1, which means the last item is popped off by default:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Notice the returned value which is the integer 33:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw.pop()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw.pop()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw.pop()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw.pop()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>33</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Recall that:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"chr(33)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003echr\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e33\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="chr(33)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">chr</span><span style="color: #24292E">(</span><span style="color: #005CC5">33</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The bytearray is also mutated inplace:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting_rw","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting_rw\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting_rw" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting_rw</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The index of each value of the bytearray can be examined using:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"for index, b in enumerate(greeting_rw):\n    print(f'{index}: {hex(b)}')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003efor\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e index, b \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ein\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eenumerate\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greeting_rw):\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eprint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ef\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e{\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eindex\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e}\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e: \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e{hex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(b)\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e}\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="for index, b in enumerate(greeting_rw):
    print(f'{index}: {hex(b)}')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">for</span><span style="color: #24292E"> index, b </span><span style="color: #D73A49">in</span><span style="color: #24292E"> </span><span style="color: #005CC5">enumerate</span><span style="color: #24292E">(greeting_rw):</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #005CC5">print</span><span style="color: #24292E">(</span><span style="color: #D73A49">f</span><span style="color: #032F62">&#39;</span><span style="color: #005CC5">{</span><span style="color: #24292E">index</span><span style="color: #005CC5">}</span><span style="color: #032F62">: </span><span style="color: #005CC5">{hex</span><span style="color: #24292E">(b)</span><span style="color: #005CC5">}</span><span style="color: #032F62">&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0: 0xce
1: 0x93
2: 0xce
3: 0xb5
4: 0xce
5: 0xb9
6: 0xce
7: 0xac
8: 0x20
9: 0xcf
10: 0x83
11: 0xce
12: 0xbf
13: 0xcf
14: 0x85
15: 0x20
16: 0xce
17: 0x9a
18: 0xcf
19: 0x8c
20: 0xcf
21: 0x83
22: 0xce
23: 0xbc
24: 0xce
25: 0xb5</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Normally the popped value is assigned to a variable name. The value at index 6 can for example be popped and assigned to a new variable name:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"popped_value = greeting_rw.pop(6)\npopped_value","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003epopped_value \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e greeting_rw.pop(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003epopped_value\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="popped_value = greeting_rw.pop(6)
popped_value" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">popped_value </span><span style="color: #D73A49">=</span><span style="color: #24292E"> greeting_rw.pop(</span><span style="color: #005CC5">6</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">popped_value</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>172</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This has a hex value of:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"hex(popped_value)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(popped_value)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="hex(popped_value)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">hex</span><span style="color: #24292E">(popped_value)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0xce'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>And the original bytearray is mutated:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"for index, b in enumerate(greeting_rw):\n    print(f'{index}: {hex(b)}')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003efor\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e index, b \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ein\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eenumerate\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greeting_rw):\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eprint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ef\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e{\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eindex\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e}\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e: \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e{hex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(b)\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e}\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="for index, b in enumerate(greeting_rw):
    print(f'{index}: {hex(b)}')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">for</span><span style="color: #24292E"> index, b </span><span style="color: #D73A49">in</span><span style="color: #24292E"> </span><span style="color: #005CC5">enumerate</span><span style="color: #24292E">(greeting_rw):</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #005CC5">print</span><span style="color: #24292E">(</span><span style="color: #D73A49">f</span><span style="color: #032F62">&#39;</span><span style="color: #005CC5">{</span><span style="color: #24292E">index</span><span style="color: #005CC5">}</span><span style="color: #032F62">: </span><span style="color: #005CC5">{hex</span><span style="color: #24292E">(b)</span><span style="color: #005CC5">}</span><span style="color: #032F62">&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0: 0xce
1: 0x93
2: 0xce
3: 0xb5
4: 0xce
5: 0xb9
6: 0x20
7: 0xcf
8: 0x83
9: 0xce
10: 0xbf
11: 0xcf
12: 0x85
13: 0x20
14: 0xce
15: 0x9a
16: 0xcf
17: 0x8c
18: 0xcf
19: 0x83
20: 0xce
21: 0xbc
22: 0xce
23: 0xb5
</code></pre>
<!-- /wp:code -->