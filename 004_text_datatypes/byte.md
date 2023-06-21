<!-- wp:paragraph -->
<p>In the previous tutorial the string class was examined and was seen to be a Sequence on Unicode characters. The bytes class is an immutable Sequence of byte values and was essentially the foundation for strings in Python 2. The main difference between a byte and a Unicode string is the fundamental unit, a byte uses a byte and a string uses a Unicode character. For an ASCII character the byte and the Unicode character are the same making the data types interchangeable for this limited set of characters. Unicode strings have been designed to make it easier to work with non-English characters.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let's examine each printable ASCII character and the byte integer sequence in decimal, binary and hexadecimal:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"import string\nfor character in string.printable:\n    formalstr = repr(character)\n    hexint = hex(ord(character))\n    hexint = '0x' + hexint.removeprefix('0x').zfill(2)\n    decint = ord(character)\n    binint = bin(ord(character))\n    binint = '0b' + binint.removeprefix('0b').zfill(8)\n    print(formalstr, decint, binint, hexint)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003eimport\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e string\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003efor\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e character \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003ein\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e string.printable:\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    formalstr \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003erepr\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(character)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    hexint \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eord\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(character))\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    hexint \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0x\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e hexint.removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0x\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    decint \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eord\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(character)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    binint \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eord\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(character))\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    binint \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e binint.removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e8\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e    \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003eprint\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(formalstr, decint, binint, hexint)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="import string
for character in string.printable:
    formalstr = repr(character)
    hexint = hex(ord(character))
    hexint = '0x' + hexint.removeprefix('0x').zfill(2)
    decint = ord(character)
    binint = bin(ord(character))
    binint = '0b' + binint.removeprefix('0b').zfill(8)
    print(formalstr, decint, binint, hexint)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #D73A49">import</span><span style="color: #24292E"> string</span></span>
<span class="line"><span style="color: #D73A49">for</span><span style="color: #24292E"> character </span><span style="color: #D73A49">in</span><span style="color: #24292E"> string.printable:</span></span>
<span class="line"><span style="color: #24292E">    formalstr </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">repr</span><span style="color: #24292E">(character)</span></span>
<span class="line"><span style="color: #24292E">    hexint </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">hex</span><span style="color: #24292E">(</span><span style="color: #005CC5">ord</span><span style="color: #24292E">(character))</span></span>
<span class="line"><span style="color: #24292E">    hexint </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #032F62">&#39;0x&#39;</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> hexint.removeprefix(</span><span style="color: #032F62">&#39;0x&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">2</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">    decint </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">ord</span><span style="color: #24292E">(character)</span></span>
<span class="line"><span style="color: #24292E">    binint </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">ord</span><span style="color: #24292E">(character))</span></span>
<span class="line"><span style="color: #24292E">    binint </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> binint.removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">8</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">    </span><span style="color: #005CC5">print</span><span style="color: #24292E">(formalstr, decint, binint, hexint)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0' 48 0b00110000 0x30
'1' 49 0b00110001 0x31
'2' 50 0b00110010 0x32
'3' 51 0b00110011 0x33
'4' 52 0b00110100 0x34
'5' 53 0b00110101 0x35
'6' 54 0b00110110 0x36
'7' 55 0b00110111 0x37
'8' 56 0b00111000 0x38
'9' 57 0b00111001 0x39
'a' 97 0b01100001 0x61
'b' 98 0b01100010 0x62
'c' 99 0b01100011 0x63
'd' 100 0b01100100 0x64
'e' 101 0b01100101 0x65
'f' 102 0b01100110 0x66
'g' 103 0b01100111 0x67
'h' 104 0b01101000 0x68
'i' 105 0b01101001 0x69
'j' 106 0b01101010 0x6a
'k' 107 0b01101011 0x6b
'l' 108 0b01101100 0x6c
'm' 109 0b01101101 0x6d
'n' 110 0b01101110 0x6e
'o' 111 0b01101111 0x6f
'p' 112 0b01110000 0x70
'q' 113 0b01110001 0x71
'r' 114 0b01110010 0x72
's' 115 0b01110011 0x73
't' 116 0b01110100 0x74
'u' 117 0b01110101 0x75
'v' 118 0b01110110 0x76
'w' 119 0b01110111 0x77
'x' 120 0b01111000 0x78
'y' 121 0b01111001 0x79
'z' 122 0b01111010 0x7a
'A' 65 0b01000001 0x41
'B' 66 0b01000010 0x42
'C' 67 0b01000011 0x43
'D' 68 0b01000100 0x44
'E' 69 0b01000101 0x45
'F' 70 0b01000110 0x46
'G' 71 0b01000111 0x47
'H' 72 0b01001000 0x48
'I' 73 0b01001001 0x49
'J' 74 0b01001010 0x4a
'K' 75 0b01001011 0x4b
'L' 76 0b01001100 0x4c
'M' 77 0b01001101 0x4d
'N' 78 0b01001110 0x4e
'O' 79 0b01001111 0x4f
'P' 80 0b01010000 0x50
'Q' 81 0b01010001 0x51
'R' 82 0b01010010 0x52
'S' 83 0b01010011 0x53
'T' 84 0b01010100 0x54
'U' 85 0b01010101 0x55
'V' 86 0b01010110 0x56
'W' 87 0b01010111 0x57
'X' 88 0b01011000 0x58
'Y' 89 0b01011001 0x59
'Z' 90 0b01011010 0x5a
'!' 33 0b00100001 0x21
'"' 34 0b00100010 0x22
'#' 35 0b00100011 0x23
'$' 36 0b00100100 0x24
'%' 37 0b00100101 0x25
'&amp;' 38 0b00100110 0x26
"'" 39 0b00100111 0x27
'(' 40 0b00101000 0x28
')' 41 0b00101001 0x29
'*' 42 0b00101010 0x2a
'+' 43 0b00101011 0x2b
',' 44 0b00101100 0x2c
'-' 45 0b00101101 0x2d
'.' 46 0b00101110 0x2e
'/' 47 0b00101111 0x2f
':' 58 0b00111010 0x3a
';' 59 0b00111011 0x3b
'&lt;' 60 0b00111100 0x3c
'=' 61 0b00111101 0x3d
'&gt;' 62 0b00111110 0x3e
'?' 63 0b00111111 0x3f
'@' 64 0b01000000 0x40
'&#91;' 91 0b01011011 0x5b
'\\' 92 0b01011100 0x5c
']' 93 0b01011101 0x5d
'^' 94 0b01011110 0x5e
'_' 95 0b01011111 0x5f
'`' 96 0b01100000 0x60
'{' 123 0b01111011 0x7b
'|' 124 0b01111100 0x7c
'}' 125 0b01111101 0x7d
'~' 126 0b01111110 0x7e
' ' 32 0b00100000 0x20
'\t' 9 0b00001001 0x09
'\n' 10 0b00001010 0x0a
'\r' 13 0b00001101 0x0d
'\x0b' 11 0b00001011 0x0b
'\x0c' 12 0b00001100 0x0c</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="initialisation-signature">Initialisation Signature</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Inputting bytes() will display the docstring of the initialisation signature of the byte class as a popup balloon. Recall some IDEs such as JupyterLab may require the keypress shift ⇧ and tab ↹ to invoke the docstring:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Init signature:  bytes(self, /, *args, **kwargs)
Docstring:     
bytes(iterable_of_ints) -> bytes
bytes(string, encoding[, errors]) -> bytes
bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
bytes(int) -> bytes object of size given by the parameter initialized with null bytes
bytes() -> empty bytes object

Construct an immutable array of bytes from:
  - an iterable yielding integers in range(256)
  - a text string encoded using the specified encoding
  - any object implementing the buffer API.
  - an integer
Type:           type
Subclasses:   </pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>Notice in the output of the for loop of printable ASCII characters that each ASCII character is a decimal of 0-127. If a tuple sequence of decimal integers is computed:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"integers = (104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33)\nbytes(integers)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eintegers \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e (\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e104\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e101\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e108\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e108\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e111\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e32\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e119\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e111\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e114\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e108\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e100\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e33\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(integers)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="integers = (104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33)
bytes(integers)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">integers </span><span style="color: #D73A49">=</span><span style="color: #24292E"> (</span><span style="color: #005CC5">104</span><span style="color: #24292E">, </span><span style="color: #005CC5">101</span><span style="color: #24292E">, </span><span style="color: #005CC5">108</span><span style="color: #24292E">, </span><span style="color: #005CC5">108</span><span style="color: #24292E">, </span><span style="color: #005CC5">111</span><span style="color: #24292E">, </span><span style="color: #005CC5">32</span><span style="color: #24292E">, </span><span style="color: #005CC5">119</span><span style="color: #24292E">, </span><span style="color: #005CC5">111</span><span style="color: #24292E">, </span><span style="color: #005CC5">114</span><span style="color: #24292E">, </span><span style="color: #005CC5">108</span><span style="color: #24292E">, </span><span style="color: #005CC5">100</span><span style="color: #24292E">, </span><span style="color: #005CC5">33</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #005CC5">bytes</span><span style="color: #24292E">(integers)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'hello world!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The decimal numbering system is the numbering system we are used to but isn't easy to visualise what is stored in the byte sequence physically. Instead the binary values can be supplied, these are machine readable and relate to the physical values stored in a byte for each character but they aren't very human readable:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"integers = (0b01101000,\n            0b01100101,\n            0b01101100,\n            0b01101100,\n            0b01101111,\n            0b00100000,\n            0b01110111,\n            0b01101111,\n            0b01110010,\n            0b01101100,\n            0b01100100,\n            0b00100001)\n            \nbytes(integers)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eintegers \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e (\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01101000\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01100101\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01101100\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01101100\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01101111\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e00100000\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01110111\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01101111\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01110010\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01101100\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e01100100\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0b\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e00100001\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(integers)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="integers = (0b01101000,
            0b01100101,
            0b01101100,
            0b01101100,
            0b01101111,
            0b00100000,
            0b01110111,
            0b01101111,
            0b01110010,
            0b01101100,
            0b01100100,
            0b00100001)
            
bytes(integers)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">integers </span><span style="color: #D73A49">=</span><span style="color: #24292E"> (</span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01101000</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01100101</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01101100</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01101100</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01101111</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">00100000</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01110111</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01101111</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01110010</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01101100</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">01100100</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0b</span><span style="color: #005CC5">00100001</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">            </span></span>
<span class="line"><span style="color: #005CC5">bytes</span><span style="color: #24292E">(integers)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'hello world!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>If the 0b prefix is removed and the binary values are split into groupings of 4:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"integers = (0110 1000,\n            0110 0101,\n            0110 1100,\n            0110 1100,\n            0110 1111,\n            0010 0000,\n            0111 0111,\n            0110 1111,\n            0111 0010,\n            0110 1100,\n            0110 0100,\n            0010 0001)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eintegers = (0110 1000,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0110 0101,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0110 1100,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0110 1100,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0110 1111,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0010 0000,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0111 0111,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0110 1111,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0111 0010,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0110 1100,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0110 0100,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            0010 0001)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"make","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="integers = (0110 1000,
            0110 0101,
            0110 1100,
            0110 1100,
            0110 1111,
            0010 0000,
            0111 0111,
            0110 1111,
            0111 0010,
            0110 1100,
            0110 0100,
            0010 0001)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">integers = (0110 1000,</span></span>
<span class="line"><span style="color: #24292E">            0110 0101,</span></span>
<span class="line"><span style="color: #24292E">            0110 1100,</span></span>
<span class="line"><span style="color: #24292E">            0110 1100,</span></span>
<span class="line"><span style="color: #24292E">            0110 1111,</span></span>
<span class="line"><span style="color: #24292E">            0010 0000,</span></span>
<span class="line"><span style="color: #24292E">            0111 0111,</span></span>
<span class="line"><span style="color: #24292E">            0110 1111,</span></span>
<span class="line"><span style="color: #24292E">            0111 0010,</span></span>
<span class="line"><span style="color: #24292E">            0110 1100,</span></span>
<span class="line"><span style="color: #24292E">            0110 0100,</span></span>
<span class="line"><span style="color: #24292E">            0010 0001)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>Each of the groupings of 4 can be replaced by their corresponding hexadecimal values:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"integers = (6 8,\n            6 5,\n            6 c,\n            6 c,\n            6 f,\n            2 0,\n            7 7,\n            6 f,\n            7 2,\n            6 c,\n            6 4,\n            2 1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eintegers = (6 8,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            6 5,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            6 c,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            6 c,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            6 f,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            2 0,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            7 7,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            6 f,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            7 2,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            6 c,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            6 4,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            2 1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"make","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="integers = (6 8,
            6 5,
            6 c,
            6 c,
            6 f,
            2 0,
            7 7,
            6 f,
            7 2,
            6 c,
            6 4,
            2 1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">integers = (6 8,</span></span>
<span class="line"><span style="color: #24292E">            6 5,</span></span>
<span class="line"><span style="color: #24292E">            6 c,</span></span>
<span class="line"><span style="color: #24292E">            6 c,</span></span>
<span class="line"><span style="color: #24292E">            6 f,</span></span>
<span class="line"><span style="color: #24292E">            2 0,</span></span>
<span class="line"><span style="color: #24292E">            7 7,</span></span>
<span class="line"><span style="color: #24292E">            6 f,</span></span>
<span class="line"><span style="color: #24292E">            7 2,</span></span>
<span class="line"><span style="color: #24292E">            6 c,</span></span>
<span class="line"><span style="color: #24292E">            6 4,</span></span>
<span class="line"><span style="color: #24292E">            2 1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>Removing the space and adding the 0x prefix gives the more human readable hexadecimal values that are also easy to translate physically to the byte sequence.</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"integers = (0x68,\n            0x65,\n            0x6c,\n            0x6c,\n            0x6f,\n            0x20,\n            0x77,\n            0x6f,\n            0x72,\n            0x6c,\n            0x64,\n            0x21)\n            \nbytes(integers)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eintegers \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e (\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e68\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e65\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6c\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6c\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6f\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e20\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e77\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6f\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e72\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e6c\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e64\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e,\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e21\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e            \u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(integers)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="integers = (0x68,
            0x65,
            0x6c,
            0x6c,
            0x6f,
            0x20,
            0x77,
            0x6f,
            0x72,
            0x6c,
            0x64,
            0x21)
            
bytes(integers)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">integers </span><span style="color: #D73A49">=</span><span style="color: #24292E"> (</span><span style="color: #D73A49">0x</span><span style="color: #005CC5">68</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">65</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">6c</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">6c</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">6f</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">20</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">77</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">6f</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">72</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">6c</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">64</span><span style="color: #24292E">,</span></span>
<span class="line"><span style="color: #24292E">            </span><span style="color: #D73A49">0x</span><span style="color: #005CC5">21</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">            </span></span>
<span class="line"><span style="color: #005CC5">bytes</span><span style="color: #24292E">(integers)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'hello world!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>A byte string can also be created using the equivalent hexadecimal escape characters notice that the encoding needs to also be specified and in this case is 'ASCII'. Encoding is essentially a translation mapping each byte to a Unicode character:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting = bytes('\\x68\\x65\\x6c\\x6c\\x6f\\x20\\x77\\x6f\\x72\\x6c\\x64\\x21', encoding='ASCII')\ngreeting","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e\\x68\\x65\\x6c\\x6c\\x6f\\x20\\x77\\x6f\\x72\\x6c\\x64\\x21\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ASCII\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting = bytes('\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64\x21', encoding='ASCII')
greeting" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;</span><span style="color: #005CC5">\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64\x21</span><span style="color: #032F62">&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ASCII&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'hello world!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>A bytes sequence can be created by casting a Unicode string to an integer, once again the encoding is specified as 'ASCII':</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting = bytes('hello world!', encoding='ASCII')\ngreeting","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;hello world!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ASCII\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting = bytes('hello world!', encoding='ASCII')
greeting" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;hello world!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ASCII&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greeting</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'hello world!'</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Encoding and Decoding</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If a string with non-ASCII characters is cast into a bytes Sequence, the equivalent encoding needs to be specified. The most common encoding is UTF-8 which handles both ASCII and non-ASCII characters:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bytes('Γειά σου Κόσμε!', encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bytes('Γειά σου Κόσμε!', encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Notice the output displays all the Greek characters using a 2 byte hexadecimal escape sequence. Only the ASCII characters are shown using their character, the ' ' and '!' respectively.</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>To decode a byte sequence to a Unicode string, the decode identifier can be used:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  greek_greeting.decode(encoding='utf-8', errors='strict')
Docstring:
Decode the bytes using the codec registered for encoding.

encoding
  The encoding with which to decode the bytes.
errors
  The error handling scheme to use for the handling of decoding errors.
  The default is 'strict' meaning that decoding errors raise a
  UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
  as well as any other name registered with codecs.register_error that
  can handle UnicodeDecodeErrors.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>This requires the correct encoding scheme to use to map each byte to a corresponding Unicode character:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting.decode('UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting.decode(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting.decode('UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting.decode(</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'Γειά σου Κόσμε!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>If the wrong encoding scheme is specified an error usually displays:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting.decode('ASCII')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting.decode(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ASCII\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting.decode('ASCII')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting.decode(</span><span style="color: #032F62">&#39;ASCII&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>UnicodeDecodeError: 'ascii' codec can't decode byte 0xce in position 0: ordinal not in range(128)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The identifier hex will cast the byte into a hexadecimal Unicode string, each byte will be shown as a 2 digit hexadecimal character:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Docstring:
Create a string of hexadecimal numbers from a bytes object.

  sep
    An optional single character or byte to separate hex bytes.
  bytes_per_sep
    How many bytes between separators.  Positive values count from the
    right, negative values count from the left.

Example:
>>> value = b'\xb9\x01\xef'
>>> value.hex()
'b901ef'
>>> value.hex(':')
'b9:01:ef'
>>> value.hex(':', 2)
'b9:01ef'
>>> value.hex(':', -2)
'b901:ef'
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting.hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting.hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting.hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting.hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ce93ceb5ceb9ceac20cf83cebfcf8520ce9acf8ccf83cebcceb521'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The __len__ data model identifier defines the behaviour of the builtins function len. In the case of the byte this returns the number of bytes and not the number of hexadecimal characters in the Unicode string:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p> </p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"len(greek_greeting) # number of bytes\nlen(greek_greeting.hex()) # hexadecimal Unicode string 2 hexadecimal characters per byte\nlen(greek_greeting.decode('UTF-8')) # decoded Unicode string","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003elen\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greek_greeting) \u003c/span\u003e\u003cspan style=\u0022color: #6A737D\u0022\u003e# number of bytes\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003elen\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greek_greeting.hex()) \u003c/span\u003e\u003cspan style=\u0022color: #6A737D\u0022\u003e# hexadecimal Unicode string 2 hexadecimal characters per byte\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003elen\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greek_greeting.decode(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)) \u003c/span\u003e\u003cspan style=\u0022color: #6A737D\u0022\u003e# decoded Unicode string\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="len(greek_greeting) # number of bytes
len(greek_greeting.hex()) # hexadecimal Unicode string 2 hexadecimal characters per byte
len(greek_greeting.decode('UTF-8')) # decoded Unicode string" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">len</span><span style="color: #24292E">(greek_greeting) </span><span style="color: #6A737D"># number of bytes</span></span>
<span class="line"><span style="color: #005CC5">len</span><span style="color: #24292E">(greek_greeting.hex()) </span><span style="color: #6A737D"># hexadecimal Unicode string 2 hexadecimal characters per byte</span></span>
<span class="line"><span style="color: #005CC5">len</span><span style="color: #24292E">(greek_greeting.decode(</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)) </span><span style="color: #6A737D"># decoded Unicode string</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>27
54
15</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Note that there are 12 Greek letters which are Unicode characters which occupy 2 bytes and 3 ASCII letters which are ASCII characters and occupy 1 byte in the encoding scheme 'UTF-8':</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"12*2 + 3*1","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e3\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="12*2 + 3*1" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">12</span><span style="color: #D73A49">*</span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> </span><span style="color: #005CC5">3</span><span style="color: #D73A49">*</span><span style="color: #005CC5">1</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>27</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The 8 in UTF-8 means 8 bits in a byte which is the memory used for an ASCII character. UTF-8 is however adaptive and for the most common Unicode characters out with ASCII, 2 bytes (16 bits) are used to encode the character. Since character sets of other languages alongside emojis are being added to Unicode the number of combinations for 16 bits has been exceeded:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"2 ** 16","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e16\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="2 ** 16" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #D73A49">**</span><span style="color: #24292E"> </span><span style="color: #005CC5">16</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>65536</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>and therefore some newer characters occupy 4 bytes (32 bits):</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"2 ** 64","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e**\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e64\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="2 ** 64" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">2</span><span style="color: #24292E"> </span><span style="color: #D73A49">**</span><span style="color: #24292E"> </span><span style="color: #005CC5">64</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>18446744073709551616</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The number of combinations available from 4 bytes is ample and is nowhere nearbeing exceeded.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Before the adaptive encoding scheme 'UTF-8' became the standard there were different encoding schemes such as 'UTF-16' which contained the most commonly used characters in Western European languages. The 16 in UTF-16 means that each ASCII and supported Unicode character is encoded in 2 bytes or 16 bit. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A comparison can be made between 'UTF-8' and 'UTF-16':</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')\ngreek_greeting.hex()\nlen(greek_greeting)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting.hex()\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003elen\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greek_greeting)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')
greek_greeting.hex()
len(greek_greeting)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greek_greeting.hex()</span></span>
<span class="line"><span style="color: #005CC5">len</span><span style="color: #24292E">(greek_greeting)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ce93ceb5ceb9ceac20cf83cebfcf8520ce9acf8ccf83cebcceb521'</code></pre>
<!-- /wp:code -->

<!-- wp:code -->
<pre class="wp-block-code"><code>27</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting16 = bytes('Γειά σου Κόσμε!', encoding='UTF-16')\ngreek_greeting16.hex()\nlen(greek_greeting16)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting16 \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-16\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting16.hex()\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003elen\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greek_greeting16)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting16 = bytes('Γειά σου Κόσμε!', encoding='UTF-16')
greek_greeting16.hex()
len(greek_greeting16)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting16 </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-16&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greek_greeting16.hex()</span></span>
<span class="line"><span style="color: #005CC5">len</span><span style="color: #24292E">(greek_greeting16)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'fffe9303b503b903ac032000c303bf03c50320009a03cc03c303bc03b5032100'</code></pre>
<!-- /wp:code -->

<!-- wp:code -->
<pre class="wp-block-code"><code>32</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The UTF-8 encoding assigns the 3 ASCII characters to 1 byte and the 12 Unicode characters to 2 bytes:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"3*1 + 12*2 ","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e3\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e12\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="3*1 + 12*2 " style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">3</span><span style="color: #D73A49">*</span><span style="color: #005CC5">1</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> </span><span style="color: #005CC5">12</span><span style="color: #D73A49">*</span><span style="color: #005CC5">2</span><span style="color: #24292E"> </span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>27</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The UTF-8 encoding assigns the 15 characters to to 2 bytes:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"15 * 2","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e15\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e*\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="15 * 2" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">15</span><span style="color: #24292E"> </span><span style="color: #D73A49">*</span><span style="color: #24292E"> </span><span style="color: #005CC5">2</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>30</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Notice that the length is 32, this is because a byte order marker occupying 2 bytes has been prefixed:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bom = bytes('', encoding='UTF-16')\nbom.hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ebom \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-16\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ebom.hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bom = bytes('', encoding='UTF-16')
bom.hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">bom </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-16&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">bom.hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'fffe'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The translation table for the Unicode characters is different however the translation table for the ASCII characters is similar. If the last byte is examined it has a value '2100' in 'UTF-16' and '21' in 'UTF-8'. The reason it is '2100' and not '0021' is that UTF-16 uses little endian; each character corresponds to a byte pair and the least significant value in this case the trailing zeros are stored first.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The endian value can be specified:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting16le = bytes('Γειά σου Κόσμε!', encoding='UTF-16-LE')\ngreek_greeting16le.hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting16le \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-16-LE\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting16le.hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting16le = bytes('Γειά σου Κόσμε!', encoding='UTF-16-LE')
greek_greeting16le.hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting16le </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-16-LE&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greek_greeting16le.hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'9303b503b903ac032000c303bf03c50320009a03cc03c303bc03b5032100'</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting16be = bytes('Γειά σου Κόσμε!', encoding='UTF-16-BE')\ngreek_greeting16be.hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting16be \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-16-BE\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting16be.hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting16be = bytes('Γειά σου Κόσμε!', encoding='UTF-16-BE')
greek_greeting16be.hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting16be </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-16-BE&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greek_greeting16be.hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'039303b503b903ac002003c303bf03c50020039a03cc03c303bc03b50021'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>When the endian is specified, there is no BOM. Notice the difference in the byte ordering by examining every 4 hexadecimal characters. Each byte (2 hexadecimal characters) pair is swapped.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Although 'UTF-8' does not use a BOM, Microsoft have a tendency to add BOMs to 'UTF-8':</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')\ngreek_greeting.hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting.hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')
greek_greeting.hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greek_greeting.hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ce93ceb5ceb9ceac20cf83cebfcf8520ce9acf8ccf83cebcceb521'</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting_bom = bytes('Γειά σου Κόσμε!', encoding='UTF-8-SIG')\ngreek_greeting_bom.hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting_bom \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8-SIG\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting_bom.hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting_bom = bytes('Γειά σου Κόσμε!', encoding='UTF-8-SIG')
greek_greeting_bom.hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting_bom </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8-SIG&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greek_greeting_bom.hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">'efbbbfce93ceb5ceb9ceac20cf83cebfcf8520ce9acf8ccf83cebcceb521'</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>And just to clarify:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bom = bytes('', encoding='UTF-8-SIG')\nbom.hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ebom \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8-SIG\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003ebom.hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bom = bytes('', encoding='UTF-8-SIG')
bom.hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">bom </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8-SIG&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">bom.hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'efbbbf'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>ASCII values range between 0 (inclusive) and 128 (exclusive). The last value is at 127:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"'0b' + bin(127).removeprefix('0b').zfill(8)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e127\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e8\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="'0b' + bin(127).removeprefix('0b').zfill(8)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> </span><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #005CC5">127</span><span style="color: #24292E">).removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">8</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0b01111111'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Notice this spans only half the values in the byte. Originally the other half of the byte was used for 'Latin1' for English and North European languages which expanded the character set to 191 characters and included for example the '£' sign:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"price = bytes('£123.45', encoding='latin1')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eprice \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;£123.45\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;latin1\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="price = bytes('£123.45', encoding='latin1')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">price </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;£123.45&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;latin1&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'\xa3123.45'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Notice that the '£' sign is not encoded and instead displays the hexadecimal escape sequence '\xa3' which still occupies the space of 1 byte but is larger than the value of 127. The remaining characters in the bytes Sequence are ASCII and are encoded:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"'0b' + bin(0xa3).removeprefix('0b').zfill(8)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e+\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebin\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e0x\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ea3\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0b\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e).zfill(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e8\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="'0b' + bin(0xa3).removeprefix('0b').zfill(8)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E"> </span><span style="color: #D73A49">+</span><span style="color: #24292E"> </span><span style="color: #005CC5">bin</span><span style="color: #24292E">(</span><span style="color: #D73A49">0x</span><span style="color: #005CC5">a3</span><span style="color: #24292E">).removeprefix(</span><span style="color: #032F62">&#39;0b&#39;</span><span style="color: #24292E">).zfill(</span><span style="color: #005CC5">8</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'0b10100011'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Although 'Latin-1' was commonly in the English speaking world, there were a number of regional variations:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"price.decode('latin-1)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eprice.decode(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;latin-1)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="price.decode('latin-1)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">price.decode(</span><span style="color: #032F62">&#39;latin-1)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>£123.45</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>'latin-2' and 'latin-3' were used in eastern and southern Europe respectively. 'greek' was used in Greece and 'cyrillic' is used in countries that use the Cyrillic alphabet. Since these all use the same byte sequence but map to a character in a different mapping, these characters were often replaced with the wrong character in a phenomenon known as mojibake which was common in the early advent of the internet:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"price.decode('latin2')\nprice.decode('latin3')\nprice.decode('greek')\nprice.decode('cyrillic')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eprice.decode(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;latin2\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eprice.decode(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;latin3\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eprice.decode(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;greek\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003eprice.decode(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;cyrillic\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="price.decode('latin2')
price.decode('latin3')
price.decode('greek')
price.decode('cyrillic')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">price.decode(</span><span style="color: #032F62">&#39;latin2&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">price.decode(</span><span style="color: #032F62">&#39;latin3&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">price.decode(</span><span style="color: #032F62">&#39;greek&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">price.decode(</span><span style="color: #032F62">&#39;cyrillic&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'Ł123.45'
'£123.45'
'£123.45'
'Ѓ123.45'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The fundamental unit of a bytes instance is a byte. If a bytes instance is created:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>It can be indexed using square brackets:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting[0]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting[0]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting[</span><span style="color: #005CC5">0</span><span style="color: #24292E">]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>206</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Notice that a number if returned that is &lt;256 and corresponds to a byte. This can be seen more clearly if the hex values of the byte sequence are examined:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting.hex()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting.hex()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting.hex()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting.hex()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ce93ceb5ceb9ceac20cf83cebfcf8520ce9acf8ccf83cebcceb521'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>And if the hex function is used on the returned integer with the '0x' prefix removed. The first byte is the 1st and 2nd characters of the hexadecimal string:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"hex(greek_greeting[0]).removeprefix('0x')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greek_greeting[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e0\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0x\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="hex(greek_greeting[0]).removeprefix('0x')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">hex</span><span style="color: #24292E">(greek_greeting[</span><span style="color: #005CC5">0</span><span style="color: #24292E">]).removeprefix(</span><span style="color: #032F62">&#39;0x&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ce'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The second byte is the 3rd and 4th characters of the hexadecimal string:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"hex(greek_greeting[1]).removeprefix('0x')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehex\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(greek_greeting[\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]).removeprefix(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;0x\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="hex(greek_greeting[1]).removeprefix('0x')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">hex</span><span style="color: #24292E">(greek_greeting[</span><span style="color: #005CC5">1</span><span style="color: #24292E">]).removeprefix(</span><span style="color: #032F62">&#39;0x&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'93'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Slicing on the other hand returns a bytes string even if the slice only returns a single element:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting[:1]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting[:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting[:1]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting[:</span><span style="color: #005CC5">1</span><span style="color: #24292E">]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'\xce'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Note that the first Unicode character 'Γ ' spans 2 bytes but the slice above only returns the first byte. Attempting to decode this will lead to a UnicodeDecodeError:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting[:1].decode(encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting[:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e1\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].decode(\u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting[:1].decode(encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting[:</span><span style="color: #005CC5">1</span><span style="color: #24292E">].decode(</span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>UnicodeDecodeError: 'utf-8' codec can't decode byte 0xce in position 0: unexpected end of data</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Slicing to get the 1st and 2nd byte will decode properly:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting[:2]","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting[:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e]\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting[:2]" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting[:</span><span style="color: #005CC5">2</span><span style="color: #24292E">]</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'\xce\x93'</code></pre>
<!-- /wp:code -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting[:2].decode(encoding='UTF-8')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting[:\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003e2\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e].decode(\u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting[:2].decode(encoding='UTF-8')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting[:</span><span style="color: #005CC5">2</span><span style="color: #24292E">].decode(</span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'Γ'</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Identifiers and Data Model Identifiers</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If the method resolution order of bytes is checked, it has the object as a parent class:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"bytes.mro()","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e.mro()\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="bytes.mro()" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">bytes</span><span style="color: #24292E">.mro()</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>&#91;bytes, object]</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>If help is used on bytes, details about the defined identifiers split into the three groupings:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>methods</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>class methods</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>static methods</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"help(bytes)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ehelp\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="help(bytes)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #005CC5">help</span><span style="color: #24292E">(</span><span style="color: #005CC5">bytes</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>Help on class bytes in module builtins:

class bytes(object)
 |  bytes(iterable_of_ints) -> bytes
 |  bytes(string, encoding&#91;, errors]) -> bytes
 |  bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
 |  bytes(int) -> bytes object of size given by the parameter initialized with null bytes
 |  bytes() -> empty bytes object
 |  
 |  Construct an immutable array of bytes from:
 |    - an iterable yielding integers in range(256)
 |    - a text string encoded using the specified encoding
 |    - any object implementing the buffer API.
 |    - an integer
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __bytes__(self, /)
 |      Convert this value to exact type bytes.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
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
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
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
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __str__(self, /)
 |      Return str(self).
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
 |  count(...)
 |      B.count(sub&#91;, start&#91;, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of subsection sub in
 |      bytes B&#91;start:end].  Optional arguments start and end are interpreted
 |      as in slice notation.
 |  
 |  decode(self, /, encoding='utf-8', errors='strict')
 |      Decode the bytes using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding with which to decode the bytes.
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
 |      Create a string of hexadecimal numbers from a bytes object.
 |      
 |        sep
 |          An optional single character or byte to separate hex bytes.
 |        bytes_per_sep
 |          How many bytes between separators.  Positive values count from the
 |          right, negative values count from the left.
 |      
 |      Example:
 |      >>> value = b'\xb9\x01\xef'
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
 |      Concatenate any number of bytes objects.
 |      
 |      The bytes whose method is called is inserted in between each pair.
 |      
 |      The result is returned as a new bytes object.
 |      
 |      Example: b'.'.join(&#91;b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.
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
 |      If the argument is omitted or None, strip leading  ASCII whitespace.
 |  
 |  partition(self, sep, /)
 |      Partition the bytes into three parts using the given separator.
 |      
 |      This will search for the separator sep in the bytes. If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original bytes
 |      object and two empty bytes objects.
 |  
 |  removeprefix(self, prefix, /)
 |      Return a bytes object with the given prefix string removed if present.
 |      
 |      If the bytes starts with the prefix string, return bytes&#91;len(prefix):].
 |      Otherwise, return a copy of the original bytes.
 |  
 |  removesuffix(self, suffix, /)
 |      Return a bytes object with the given suffix string removed if present.
 |      
 |      If the bytes ends with the suffix string and that suffix is not empty,
 |      return bytes&#91;:-len(prefix)].  Otherwise, return a copy of the original
 |      bytes.
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
 |      Partition the bytes into three parts using the given separator.
 |      
 |      This will search for the separator sep in the bytes, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty bytes
 |      objects and the original bytes object.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the sections in the bytes, using sep as the delimiter.
 |      
 |        sep
 |          The delimiter according which to split the bytes.
 |          None (the default value) means split on ASCII whitespace characters
 |          (space, tab, return, newline, formfeed, vertical tab).
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splitting is done starting at the end of the bytes and working to the front.
 |  
 |  rstrip(self, bytes=None, /)
 |      Strip trailing bytes contained in the argument.
 |      
 |      If the argument is omitted or None, strip trailing ASCII whitespace.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the sections in the bytes, using sep as the delimiter.
 |      
 |      sep
 |        The delimiter according which to split the bytes.
 |        None (the default value) means split on ASCII whitespace characters
 |        (space, tab, return, newline, formfeed, vertical tab).
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the bytes, breaking at line boundaries.
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
 |      Create a bytes object from a string of hexadecimal numbers.
 |      
 |      Spaces between two numbers are accepted.
 |      Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
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
</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Because the string and bytes class are similar, most of the identifiers are consistent to those found in the string class and behave analogously. The slight difference in behaviour due to a byte being a fundamental unit opposed to a Unicode string was seen when using the __getitem__ and __len__ data model identifiers. The decode and hex method are additional methods associated with this difference. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There is also a class method fromhex which is an alternative constructor and can be used to construct a bytes instance from a hex string:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  bytes.fromhex(string, /)
Docstring:
Create a bytes object from a string of hexadecimal numbers.

Spaces between two numbers are accepted.
Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>The alternative constructor essentially does the reverse of the hex method:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')\ngreek_greeting_hex = greek_greeting.hex()\ngreek_greeting_hex","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;Γειά σου Κόσμε!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;UTF-8\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting_hex \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e greek_greeting.hex()\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting_hex\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting = bytes('Γειά σου Κόσμε!', encoding='UTF-8')
greek_greeting_hex = greek_greeting.hex()
greek_greeting_hex" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;Γειά σου Κόσμε!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;UTF-8&#39;</span><span style="color: #24292E">)</span></span>
<span class="line"><span style="color: #24292E">greek_greeting_hex </span><span style="color: #D73A49">=</span><span style="color: #24292E"> greek_greeting.hex()</span></span>
<span class="line"><span style="color: #24292E">greek_greeting_hex</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>'ce93ceb5ceb9ceac20cf83cebfcf8520ce9acf8ccf83cebcceb521'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The alternative constructor is a class method and is typically called from a class:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greek_greeting2 = bytes.fromhex(greek_greeting_hex)\ngreek_greeting2","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting2 \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e.fromhex(greek_greeting_hex)\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreek_greeting2\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greek_greeting2 = bytes.fromhex(greek_greeting_hex)
greek_greeting2" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greek_greeting2 </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">.fromhex(greek_greeting_hex)</span></span>
<span class="line"><span style="color: #24292E">greek_greeting2</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xbf\xcf\x85 \xce\x9a\xcf\x8c\xcf\x83\xce\xbc\xce\xb5!'</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>There is also the static method maketrans which is not bound to a class or an instance but associated with the bytes class and therefore found in the name space of the bytes class:</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  bytes.maketrans(frm, to, /)
Docstring:
Return a translation table useable for the bytes or bytearray translate method.

The returned table will be one where each byte in frm is mapped to the byte at
the same position in to.

The bytes objects frm and to must be of the same length.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>It can be used to create a translation table from lower case to upper case letters:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"translation_table = bytes.maketrans(bytes('abcdefghijklmnopqrstuvwxyz', \n                                          encoding='ASCII'),\n                                    bytes('ABCDEFGHIJKLMNOPQRSTUVWXYZ', \n                                          encoding='ASCII'))","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003etranslation_table \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e.maketrans(\u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;abcdefghijklmnopqrstuvwxyz\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e                                          \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ASCII\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e),\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e                                    \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ABCDEFGHIJKLMNOPQRSTUVWXYZ\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e                                          \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ASCII\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e))\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="translation_table = bytes.maketrans(bytes('abcdefghijklmnopqrstuvwxyz', 
                                          encoding='ASCII'),
                                    bytes('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                                          encoding='ASCII'))" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">translation_table </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">.maketrans(</span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;abcdefghijklmnopqrstuvwxyz&#39;</span><span style="color: #24292E">, </span></span>
<span class="line"><span style="color: #24292E">                                          </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ASCII&#39;</span><span style="color: #24292E">),</span></span>
<span class="line"><span style="color: #24292E">                                    </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;ABCDEFGHIJKLMNOPQRSTUVWXYZ&#39;</span><span style="color: #24292E">, </span></span>
<span class="line"><span style="color: #24292E">                                          </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ASCII&#39;</span><span style="color: #24292E">))</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:paragraph -->
<p>The translation table can be used with the method translate:</p>
<!-- /wp:paragraph -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting = bytes('hello world!', encoding='ASCII')","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting \u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e \u003c/span\u003e\u003cspan style=\u0022color: #005CC5\u0022\u003ebytes\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e(\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;hello world!\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e, \u003c/span\u003e\u003cspan style=\u0022color: #E36209\u0022\u003eencoding\u003c/span\u003e\u003cspan style=\u0022color: #D73A49\u0022\u003e=\u003c/span\u003e\u003cspan style=\u0022color: #032F62\u0022\u003e\u0026#39;ASCII\u0026#39;\u003c/span\u003e\u003cspan style=\u0022color: #24292E\u0022\u003e)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting = bytes('hello world!', encoding='ASCII')" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting </span><span style="color: #D73A49">=</span><span style="color: #24292E"> </span><span style="color: #005CC5">bytes</span><span style="color: #24292E">(</span><span style="color: #032F62">&#39;hello world!&#39;</span><span style="color: #24292E">, </span><span style="color: #E36209">encoding</span><span style="color: #D73A49">=</span><span style="color: #032F62">&#39;ASCII&#39;</span><span style="color: #24292E">)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:enlighter/codeblock {"language":"raw","linenumbers":"false"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="false" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">Signature:  greeting.translate(table, /, delete=b'')
Docstring:
Return a copy with each character mapped by the given translation table.

  table
    Translation table, which must be a bytes object of length 256.

All characters occurring in the optional argument delete are removed.
The remaining characters are mapped through the given translation table.
Type:      builtin_function_or_method</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:kevinbatdorf/code-block-pro {"code":"greeting.translate(translation_table)","codeHTML":"\u003cpre class=\u0022shiki github-light\u0022 style=\u0022background-color: #fff\u0022 tabindex=\u00220\u0022\u003e\u003ccode\u003e\u003cspan class=\u0022line\u0022\u003e\u003cspan style=\u0022color: #24292E\u0022\u003egreeting.translate(translation_table)\u003c/span\u003e\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e","language":"python","theme":"github-light","bgColor":"#fff","textColor":"#24292e","fontSize":".875rem","lineHeight":"1.25rem","headerType":"headlights","seeMoreString":"","seeMoreAfterLine":"","seeMoreTransition":false,"lineHighlightColor":"rgba(16, 41, 67, 0.2)","copyButton":true} -->
<div class="wp-block-kevinbatdorf-code-block-pro" style="font-size:.875rem;line-height:1.25rem"><span style="display:block;padding:16px 0 0 16px;margin-bottom:-1px;width:100%;text-align:left;background-color:#fff"><svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg></span><span role="button" tabindex="0" data-code="greeting.translate(translation_table)" style="color:#24292e;display:none" aria-label="Copy" class="code-block-pro-copy-button"><svg xmlns="http://www.w3.org/2000/svg" style="width:24px;height:24px" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path class="with-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path><path class="without-check" stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></span><pre class="shiki github-light" style="background-color: #fff" tabindex="0"><code><span class="line"><span style="color: #24292E">greeting.translate(translation_table)</span></span></code></pre></div>
<!-- /wp:kevinbatdorf/code-block-pro -->

<!-- wp:code -->
<pre class="wp-block-code"><code>b'HELLO WORLD!'</code></pre>
<!-- /wp:code -->