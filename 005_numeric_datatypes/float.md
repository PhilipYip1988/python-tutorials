<!-- wp:paragraph -->
<p>Previously whole numbers known as integers were examined. However not all physical numbers are whole numbers and have a fractional component... </p>
<!-- /wp:paragraph -->

<!-- wp:advanced-gutenberg-blocks/summary -->
<div class="wp-block-advanced-gutenberg-blocks-summary"><p class="wp-block-advanced-gutenberg-blocks-summary__title">Table of contents</p><div class="wp-block-advanced-gutenberg-blocks-summary__fold"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-up"><polyline points="18 15 12 9 6 15"></polyline></svg></div><ol role="directory" class="wp-block-advanced-gutenberg-blocks-summary__list"><li><a href="#method-resolution-order-and-consistency">Method Resolution Order and Consistency</a><ol></ol></li><li><a href="#decimal-numbering-system">Decimal Numbering System</a><ol><li><a href="#scientific-notation">Scientific Notation</a><ol></ol></li><li><a href="#recursive-rounding-issues">Recursive Rounding Issues</a><ol></ol></li></ol></li><li><a href="#binary-encoding">Binary Encoding</a><ol><li><a href="#recursive-rounding-issues">Recursive Rounding Issues</a><ol></ol></li><li><a href="#iee-754-binary-scientific-notation">IEE-754 (Binary Scientific Notation)</a><ol></ol></li></ol></li><li><a href="#rounding-data-model-identifiers">Rounding Data Model Identifiers</a><ol></ol></li><li><a href="#casting-data-model-identifiers">Casting Data Model Identifiers</a><ol></ol></li><li><a href="#binary-comparison-data-model-identifiers">Binary Comparison Data Model Identifiers</a><ol></ol></li></ol></div>
<!-- /wp:advanced-gutenberg-blocks/summary -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="method-resolution-order-and-consistency">Method Resolution Order and Consistency</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In the previous tutorials, the integer and float classes were examined which corresponded to whole numbers. When the method resolution order of the bool class was examined it was seen to be a child class of the integer class. The method resolution order of the float class shows that it is independent from the int class and is a direct subclass of object:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"float.mro()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003efloat\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e.mro()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="float.mro()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">float</span><span style="color: #24292E">.mro()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>&#91;float, object]</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>If help on the float class is examined:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"help(float)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehelp\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003efloat\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="help(float)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">help</span><span style="color: #24292E">(</span><span style="color: #005CC5">float</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Help on class float in module builtins:

class float(object)
 |  float(x=0, /)
 |  
 |  Convert a string or number to a floating point number, if possible.
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __ceil__(self, /)
 |      Return the ceiling as an Integral.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(self, /)
 |      Return the floor as an Integral.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Formats the float according to format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __le__(self, value, /)
 |      Return self&lt;=value.
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
 |  __neg__(self, /)
 |      -self
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __round__(self, ndigits=None, /)
 |      Return the Integral closest to x, rounding half toward even.
 |      
 |      When an argument is passed, work like built-in round(x, ndigits).
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(self, /)
 |      Return the Integral closest to x between 0 and x.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original float
 |      and with a positive denominator.
 |      
 |      Raise OverflowError on infinities and a ValueError on NaNs.
 |      
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |  
 |  conjugate(self, /)
 |      Return self, the complex conjugate of any float.
 |  
 |  hex(self, /)
 |      Return a hexadecimal representation of a floating-point number.
 |      
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |  
 |  is_integer(self, /)
 |      Return True if the float is an integer.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __getformat__(typestr, /) from builtins.type
 |      You probably don't want to use this function.
 |      
 |        typestr
 |          Must be 'double' or 'float'.
 |      
 |      It exists mainly to be used in Python's test suite.
 |      
 |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
 |      little-endian' best describes the format of floating point numbers used by the
 |      C type named by typestr.
 |  
 |  fromhex(string, /) from builtins.type
 |      Create a floating-point number from a hexadecimal string.
 |      
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  real
 |      the real part of a complex number</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>Despite being independent from the int class, it can be seen that a large number of data model identifiers are consistent between the int and float classes. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Moreover interaction between a float instance and an int instance, automatically casts the int into a float instance. For example:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"num1 = 1\nnum2 = 2.1\nnum3 = num1 + num2\nnum3","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum1 \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum2 \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2.1\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum3 \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e num1 \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e num2\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum3\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="num1 = 1
num2 = 2.1
num3 = num1 + num2
num3" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">num1 </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">1</span></span>
<span class="line"><span style="color: #24292E">num2 </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">2.1</span></span>
<span class="line"><span style="color: #24292E">num3 </span><span style="color: #D73A49">=</span><span style="color: #24292E"> num1 </span><span style="color: #D73A49">+</span><span style="color: #24292E"> num2</span></span>
<span class="line"><span style="color: #24292E">num3</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>3.1</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"type(num3)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003etype\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(num3)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="type(num3)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">type</span><span style="color: #24292E">(num3)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>float</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="decimal-numbering-system">Decimal Numbering System</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The typical numbering system employed by humans is the decimal numbering system which is a result of a human having 10 fingers.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Often in physics, the physical unit of measurement is not quantised. And in many cases is not comparable to the physical object being measured. Take length for example. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If length is measured in metres. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The radius of a hydrogen atom:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0.00000000012</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The radius of a human:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>1</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The radius of the sun:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>695700000</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading" id="scientific-notation">Scientific Notation</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>As the large number of leading or trailing zeros become quite hard to transcribe for a human, scientific notation is preferred. Essentially the value is made comparable to a unit in the form of a mantissa and this mantissa is raised to an exponent power of 10.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The radius of a hydrogen atom becomes:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>1.2e-10</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The radius of a sun becomes:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>6.957e8</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Generally the interaction between a large number and a small number leaves the large number unchanged for addition and subtraction. The sun for example is made up of a very large number of hydrogen atoms and the difference of one hydrogen atoms length is insignificant in comparison to the error in the suns radius.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For operations such as multiplication, the mantissas are multiplied and then the exponents are added. In the case of division, the mantissas are divided and then the exponents are subtracted. The number of hydrogen atoms along the radius of the sun is therefore:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(6.957 / 1.2) e (8-(-10))</code></pre>
<!-- /wp:code -->

<!-- wp:code -->
<pre class="wp-block-code"><code>5.7975e18</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading" id="recursive-rounding-issues">Recursive Rounding Issues</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In the decimal system, the concept of a 1/3 can be examined using integer division:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"10 // 3","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e10\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e//\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e3\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="10 // 3" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">10</span><span style="color: #24292E"> </span><span style="color: #D73A49">//</span><span style="color: #24292E"> </span><span style="color: #005CC5">3</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>3</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"10 % 3","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e10\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e%\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e3\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="10 % 3" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">10</span><span style="color: #24292E"> </span><span style="color: #D73A49">%</span><span style="color: #24292E"> </span><span style="color: #005CC5">3</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>1</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>If the remainder is multiplied by 10 to get to the next unit, the calculation recurs:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"(10 % 3) * 10","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e10\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e%\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e3\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e) \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e10\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="(10 % 3) * 10" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">(</span><span style="color: #005CC5">10</span><span style="color: #24292E"> </span><span style="color: #D73A49">%</span><span style="color: #24292E"> </span><span style="color: #005CC5">3</span><span style="color: #24292E">) </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">10</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>10</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This means that 1/3 cannot be perfectly represented in a system with only 10 unique digits and ultimately there will be a recursive rounding error due to a limit in the number of digits specified.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>3.333333333...</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="binary-encoding">Binary Encoding</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In Python the floating point number is used to represent a decimal number. Although the representation of the number is displayed in decimal, under the hood the number is stored in a form of binary scientific notation because the computers fundamental unit of storage is a bit. This leads to some unexpected recursive rounding issues.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading" id="recursive-rounding-issues">Recursive Rounding Issues</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Because the binary system only has 2 unique characters opposed to 10 in decimal, this recursive rounding error occurs far more frequently. Moreover due to the floating point number being encoded in binary but displayed in decimal, some of these recursive rounding issues can be unexpected for those who are used to working with decimal. Care needs to be taken using comparison operators in particular:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"0.1 + 0.2 == 0.3","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e==\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.3\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="0.1 + 0.2 == 0.3" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">0.1</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> </span><span style="color: #005CC5">0.2</span><span style="color: #24292E"> </span><span style="color: #D73A49">==</span><span style="color: #24292E"> </span><span style="color: #005CC5">0.3</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>False</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>If the left hand is examined:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"0.1 + 0.2","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.2\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="0.1 + 0.2" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">0.1</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> </span><span style="color: #005CC5">0.2</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0.30000000000000004</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>A recursive rounding error is shown which is why the two sides of the is equal to statement are different.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading" id="iee-754-binary-scientific-notation">IEE-754 (Binary Scientific Notation)</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The pickle module is used to serialise Python objects into a byte string. The dumps function can be used to retrieve the pickled bytes string for 0.1:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"import pickle\npickle.dumps(0.1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003eimport\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e pickle\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003epickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="import pickle
pickle.dumps(0.1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">import</span><span style="color: #24292E"> pickle</span></span>
<span class="line"><span style="color: #24292E">pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xb9\x99\x99\x99\x99\x99\x9a.'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>pickles adds a prefix and suffix which can be removed using slicing:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"pickle.dumps(0.1)[12:20]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003epickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="pickle.dumps(0.1)[12:20]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'?\xb9\x99\x99\x99\x99\x99\x9a'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This byte can be viewed in hex:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"pickle.dumps(0.1)[12:20].hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003epickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="pickle.dumps(0.1)[12:20].hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'3fb999999999999a'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This string can then be cast into an integer using the base 16:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"int(pickle.dumps(0.1)[12:20].hex(), base=16)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(pickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex(), \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="int(pickle.dumps(0.1)[12:20].hex(), base=16)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">int</span><span style="color: #24292E">(pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex(), </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">16</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>4591870180066957722</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The bin function can be used to view this in binary:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bin(int(pickle.dumps(0.1)[12:20].hex(), base=16))","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(pickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex(), \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e))\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bin(int(pickle.dumps(0.1)[12:20].hex(), base=16))" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">int</span><span style="color: #24292E">(pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex(), </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">16</span><span style="color: #24292E">))</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0b11111110111001100110011001100110011001100110011001100110011010'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The prefix can be removed using the string method removeprefix:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(pickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex(), \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">int</span><span style="color: #24292E">(pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex(), </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">16</span><span style="color: #24292E">)).removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>bin(int(pickle.dumps(0.1)&#91;12:20].hex(), base=16)).removeprefix('0b')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Finally the string method zfill can be used to zero fill to 64 binary characters including leading zeros:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(pickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex(), \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e64\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">int</span><span style="color: #24292E">(pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex(), </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">16</span><span style="color: #24292E">)).removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">64</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0011111110111001100110011001100110011001100110011001100110011010'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The 0th bit corresponds to the sign:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[0]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(pickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex(), \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e64\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[0]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">int</span><span style="color: #24292E">(pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex(), </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">16</span><span style="color: #24292E">)).removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">64</span><span style="color: #24292E">)[</span><span style="color: #005CC5">0</span><span style="color: #24292E">]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The 1st-12th bit corresponds to the biased exponent:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[1:12]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(pickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex(), \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e64\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[1:12]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">int</span><span style="color: #24292E">(pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex(), </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">16</span><span style="color: #24292E">)).removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">64</span><span style="color: #24292E">)[</span><span style="color: #005CC5">1</span><span style="color: #24292E">:</span><span style="color: #005CC5">12</span><span style="color: #24292E">]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'01111111011'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The remaining bits corresponds to the fraction:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[12:]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(pickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex(), \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e64\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[12:]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">int</span><span style="color: #24292E">(pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex(), </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">16</span><span style="color: #24292E">)).removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">64</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'1001100110011001100110011001100110011001100110011010'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The IEEE-754 representation is a form of binary scientific notation that has been optimised to be more memory efficient. It has a 1 bit sign, 11 bit biased exponent and 52 bit fraction.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For the sign bit, 0 is positive and 1 is negative; this number is positive and the sign is 0.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The biased exponent can be converted to an int using string concatenation for the binary prefix and using a base of 2:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"int('0b'+bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[1:12],\n    base=2)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(pickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex(), \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e64\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e],\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="int('0b'+bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[1:12],
    base=2)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">int</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #D73A49">+</span><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">int</span><span style="color: #24292E">(pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex(), </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">16</span><span style="color: #24292E">)).removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">64</span><span style="color: #24292E">)[</span><span style="color: #005CC5">1</span><span style="color: #24292E">:</span><span style="color: #005CC5">12</span><span style="color: #24292E">],</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">2</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>1019</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The exponent is biased so all negative numbers are encoded by a positive value. The actual 0 is at 1023 so this gives an unbiased exponent of -4.</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"1023 - int('0b'+bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[1:12], base=2)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1023\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e-\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(pickle.dumps(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].hex(), \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e64\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e], \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003ebase\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="1023 - int('0b'+bin(int(pickle.dumps(0.1)[12:20].hex(), base=16)).removeprefix('0b').zfill(64)[1:12], base=2)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">1023</span><span style="color: #24292E"> </span><span style="color: #D73A49">-</span><span style="color: #24292E"> </span><span style="color: #005CC5">int</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #D73A49">+</span><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">int</span><span style="color: #24292E">(pickle.dumps(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E">)[</span><span style="color: #005CC5">12</span><span style="color: #24292E">:</span><span style="color: #005CC5">20</span><span style="color: #24292E">].hex(), </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">16</span><span style="color: #24292E">)).removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">64</span><span style="color: #24292E">)[</span><span style="color: #005CC5">1</span><span style="color: #24292E">:</span><span style="color: #005CC5">12</span><span style="color: #24292E">], </span><span style="color: #E36209">base</span><span style="color: #D73A49">=</span><span style="color: #005CC5">2</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>-4</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>To get 0.1 to be a number of the magnitude of a unit and taking binary as the power of 2:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"0.1 * 2 #-1","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #6A737D\u0022\u003e#-1\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="0.1 * 2 #-1" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">0.1</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #6A737D">#-1</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0.2</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"0.1 * 2 * 2 #-2","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #6A737D\u0022\u003e#-2\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="0.1 * 2 * 2 #-2" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">0.1</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #6A737D">#-2</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0.4</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"0.1 * 2 * 2 * 2 #-3","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #6A737D\u0022\u003e#-3\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="0.1 * 2 * 2 * 2 #-3" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">0.1</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #6A737D">#-3</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0.8</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"0.1 * 2 * 2 * 2 * 2 #-4","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #6A737D\u0022\u003e#-4\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="0.1 * 2 * 2 * 2 * 2 #-4" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">0.1</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #6A737D">#-4</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>1.6</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This is where the -4 comes from in the exponent.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This leaves 1.6 which has to be encoded in binary scientific notation to create the fraction. This is done by use of integer division using powers of 2. For convenience this can be done using a series of divmods:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(1.6, 2**0)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1.6\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(1.6, 2**0)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">1.6</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**</span><span style="color: #005CC5">0</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(1.0, 0.6000000000000001)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>All the powers are below a unit so a binary point will be added here:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>.</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(0.6000000000000001, 2**-1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.6000000000000001\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**-\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(0.6000000000000001, 2**-1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.6000000000000001</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**-</span><span style="color: #005CC5">1</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(1.0, 0.10000000000000009)</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(0.09999999999999998, 2**-2)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.09999999999999998\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**-\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(0.09999999999999998, 2**-2)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.09999999999999998</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**-</span><span style="color: #005CC5">2</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(0.0, 0.09999999999999998)</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(0.09999999999999998, 2**-3)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.09999999999999998\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**-\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e3\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(0.09999999999999998, 2**-3)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.09999999999999998</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**-</span><span style="color: #005CC5">3</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(0.0, 0.09999999999999998)</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(0.09999999999999998, 2**-4)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.09999999999999998\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**-\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e4\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(0.09999999999999998, 2**-4)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.09999999999999998</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**-</span><span style="color: #005CC5">4</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(1.0, 0.03749999999999998)</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(0.03749999999999998, 2**-5)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.03749999999999998\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**-\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e5\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(0.03749999999999998, 2**-5)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.03749999999999998</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**-</span><span style="color: #005CC5">5</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(1.0, 0.006249999999999978)</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(0.006249999999999978, 2**-6)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.006249999999999978\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**-\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(0.006249999999999978, 2**-6)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.006249999999999978</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**-</span><span style="color: #005CC5">6</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(0.0, 0.006249999999999978)</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(0.006249999999999978, 2**-7)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.006249999999999978\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**-\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e7\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(0.006249999999999978, 2**-7)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.006249999999999978</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**-</span><span style="color: #005CC5">7</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(0.0, 0.006249999999999978)</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(0.006249999999999978, 2**-8)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.006249999999999978\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**-\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e8\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(0.006249999999999978, 2**-8)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.006249999999999978</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**-</span><span style="color: #005CC5">8</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(1.0, 0.002343749999999978)</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"divmod(0.002343749999999978, 2**-9)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003edivmod\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.002343749999999978\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**-\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e9\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="divmod(0.002343749999999978, 2**-9)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">divmod</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.002343749999999978</span><span style="color: #24292E">, </span><span style="color: #005CC5">2</span><span style="color: #D73A49">**-</span><span style="color: #005CC5">9</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>(1.0, 0.0003906249999999778)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This is essentially repeated until the divmod involving 2**-52 is reached.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If each integer division value is taken alongside the binary point, this gives:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1.100110011...</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The ... represents  further digits that occur past the binary point. This is actually a recurring number and therefore becomes:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1.1001100110011001100110011001100110011001100110011010</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Because the binary unit is always <strong>1.</strong> for binary scientific notation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>1.</strong>1001100110011001100110011001100110011001100110011010</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To save memory, it is excluded in the encoding. The fraction is therefore encoded as:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1001100110011001100110011001100110011001100110011010</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To recap a float is encoded in binary using 64 bits. For the float 0.1:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>0th bit is the sign which is 0</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>1st-12th bit is the biased exponent which is 01111111011 and corresponds to an biased power of -4</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>The leading 1. is constant and is not encoded</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>12th-64th bit is the fraction which is 1001100110011001100110011001100110011001100110011010</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>These can also be expressed using a hexadecimal floating-point literal:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"'+0x1.999999999999ap-4'","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;+0x1.999999999999ap-4\u0026#39;\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="'+0x1.999999999999ap-4'" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #032F62">&#39;+0x1.999999999999ap-4&#39;</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>The + represents the sign</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>The 0x represents hexadecimal</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>The 1. which is constant for a binary number is explicitly shown.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>The 999999999999ap is the 12-64th bit fraction expressed in hexadecimal, recall that 1001 (binary) is 9 (hexadecimal)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>The p-4 represents an unbiased power of -4</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The class method fromhex can be used to create a float from a hexadecimal floating-point literal:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"num = float.fromhex('0x1.999999999999ap-4')\nnum","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003efloat\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e.fromhex(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0x1.999999999999ap-4\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="num = float.fromhex('0x1.999999999999ap-4')
num" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">num </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">float</span><span style="color: #24292E">.fromhex(</span><span style="color: #032F62">&#39;0x1.999999999999ap-4&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">num</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>0.1</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>There is also the associated method hex, which returns the hexadecimal floating-point literal of a float instance:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"num.hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum.hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="num.hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">num.hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0x1.999999999999ap-4'</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="rounding-data-model-identifiers">Rounding Data Model Identifiers</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The data model identifiers __round__, __floor__, __ceil__, __trunc__ define the behaviour behind the builtins function round and the math functions ceil, floor and trunc. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The round function has two input arguments, number which is the number to be rounded and ndigits which is the number of digits:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  round(number, ndigits=None)
Docstring:
Round a number to a given precision in decimal digits.

The return value is an integer if ndigits is omitted or None.  Otherwise
the return value has the same type as the number.  ndigits may be negative.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>ndigits has a default value of None:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"num1 = 3.925","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum1 \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e3.925\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="num1 = 3.925" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">num1 </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">3.925</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"round(num1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eround\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(num1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="round(num1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">round</span><span style="color: #24292E">(num1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>4</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"round(num1)\nround(num1, 2)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eround\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(num1)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eround\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(num1, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="round(num1)
round(num1, 2)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">round</span><span style="color: #24292E">(num1)</span></span>
<span class="line"><span style="color: #005CC5">round</span><span style="color: #24292E">(num1, </span><span style="color: #005CC5">2</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>3.93</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The math trunc function on the other hand will always truncate a number towards the nearest integer:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"import math","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003eimport\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e math\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="import math" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">import</span><span style="color: #24292E"> math</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  math.trunc(x, /)
Docstring:
Truncates the Real x to the nearest Integral toward 0.

Uses the __trunc__ magic method.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"math.trunc(num1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003emath.trunc(num1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="math.trunc(num1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">math.trunc(num1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>3</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The math floor function will always bring the number down to the nearest integer:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  math.floor(x, /)
Docstring:
Return the floor of x as an Integral.

This is the largest integer &lt;= x.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"math.floor(num1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003emath.floor(num1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="math.floor(num1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">math.floor(num1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>3</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>For positive numbers ceil and floor behave similarly, there is a difference when negative numbers are used:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"math.trunc(-num1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003emath.trunc(\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e-\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="math.trunc(-num1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">math.trunc(</span><span style="color: #D73A49">-</span><span style="color: #24292E">num1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>-3</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"math.floor(-num1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003emath.floor(\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e-\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003enum1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="math.floor(-num1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">math.floor(</span><span style="color: #D73A49">-</span><span style="color: #24292E">num1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>-4</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The math ceil (ceiling) function will always bring the number up to the nearest integer:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  math.ceil(x, /)
Docstring:
Return the ceiling of x as an Integral.

This is the smallest integer >= x.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"math.ceil(num1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003emath.ceil(num1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="math.ceil(num1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">math.ceil(num1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>4</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="casting-data-model-identifiers">Casting Data Model Identifiers</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The __int__ data model identifier defines the behaviour when a float is cast to an integer using the builtins int class. This essentially does the same as the math trunc function:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"int(num1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(num1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="int(num1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">int</span><span style="color: #24292E">(num1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>3</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The __bool__ data model identifier defines the behaviour when a float is cast to a bool using the builtins bool class. All non-zero values are True and a zero value is False:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bool(num1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebool\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(num1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bool(num1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bool</span><span style="color: #24292E">(num1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>True</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bool(0.0)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebool\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bool(0.0)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bool</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.0</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>False</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The __float__ data model identifier defines the behaviour when a float is cast to a float using the builtins float class, because it is already a float, a copy of the float is returned:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"float(num1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003efloat\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(num1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="float(num1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">float</span><span style="color: #24292E">(num1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>3.925</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="binary-comparison-data-model-identifiers">Binary Comparison Data Model Identifiers</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Since float are ordinal, the 6 comparison operators are configured:</p>
<!-- /wp:paragraph -->

<!-- wp:table {"className":"is-style-stripes"} -->
<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Data Model Identifier </td><td>Operator</td></tr><tr><td>__eq__</td><td>==</td></tr><tr><td>__ne__</td><td>!=</td></tr><tr><td>__gt__</td><td>&gt;</td></tr><tr><td>__lt__</td><td>&lt;</td></tr><tr><td>__ge__</td><td>&gt;=</td></tr><tr><td>__le__</td><td>&lt;=</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>Care with these comparison operators needs to be taken due to recursive rounding issues. In the example seen earlier for example:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"0.1 + 0.2 == 0.3","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e==\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.3\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="0.1 + 0.2 == 0.3" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">0.1</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> </span><span style="color: #005CC5">0.2</span><span style="color: #24292E"> </span><span style="color: #D73A49">==</span><span style="color: #24292E"> </span><span style="color: #005CC5">0.3</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>False</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This can be changed by rounding the result:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"round(0.1 + 0.2, 6) == round(0.3, 6)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eround\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e) \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e==\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eround\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0.3\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true,"buttonTheme":"heroicons"} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="round(0.1 + 0.2, 6) == round(0.3, 6)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">round</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.1</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> </span><span style="color: #005CC5">0.2</span><span style="color: #24292E">, </span><span style="color: #005CC5">6</span><span style="color: #24292E">) </span><span style="color: #D73A49">==</span><span style="color: #24292E"> </span><span style="color: #005CC5">round</span><span style="color: #24292E">(</span><span style="color: #005CC5">0.3</span><span style="color: #24292E">, </span><span style="color: #005CC5">6</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>True</code></pre>
<!-- /wp:code -->