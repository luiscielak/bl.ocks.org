bl.ocks.org Google Chrome extension and bookmarklet
===================================================

This is a simple bookmarklet/Google Chrome extension that finds [Gist][1] links
in the current page and appends a link to the corresponding [bl.ock][2].

[1]: http://gist.github.com/
[2]: http://bl.ocks.org/

Installation
------------

To access bl.ocks.org from other sites, drag this link to your bookmarks bar:
[[bl.ocks.org]][bookmarklet]. This bookmarklet finds Gist links in the current page and
appends a link to the corresponding bl.ock.

To install the Google Chrome extension, download [bl.ocks.chrome.crx][extension].

[bookmarklet]: javascript:%28function%28e%2Ca%2Cg%2Ch%2Cf%2Cc%2Cb%2Cd%29%7Bif%28%21%28f%3De.jQuery%29%7C%7Cg%3Ef.fn.jquery%7C%7Ch%28f%29%29%7Bc%3Da.createElement%28%22script%22%29%3Bc.type%3D%22text/javascript%22%3Bc.src%3D%22http%3A//ajax.googleapis.com/ajax/libs/jquery/%22%2Bg%2B%22/jquery.min.js%22%3Bc.onload%3Dc.onreadystatechange%3Dfunction%28%29%7Bif%28%21b%26%26%28%21%28d%3Dthis.readyState%29%7C%7Cd%3D%3D%22loaded%22%7C%7Cd%3D%3D%22complete%22%29%29%7Bh%28%28f%3De.jQuery%29.noConflict%281%29%2Cb%3D1%29%3Bf%28c%29.remove%28%29%7D%7D%3Ba.documentElement.childNodes%5B0%5D.appendChild%28c%29%7D%7D%29%28window%2Cdocument%2C%221.4.2%22%2Cfunction%28%24%2CL%29%7Bvar%20gist_re%3D/%5Ehttps%3F%5C%3A%5C/%5C/gist%5C.github%5C.com%5C/%28%5Cd%2A%29/i%2Crel_re%3D/%5E%5C/%3F%28%5Cd%2B%29%24/%2Con_gist%3Dgist_re.test%28location.href%29%3B%24%28%22a%22%29.each%28function%28%29%7Bvar%20b%3D%24%28this%29.attr%28%22href%22%29%7C%7C%27%27%2Ca%3Db.match%28gist_re%29%3Bif%28on_gist%26%26%21%28a%26%26a%5B1%5D%29%29%7Ba%3Db.match%28rel_re%29%7Dif%28a%26%26a%5B1%5D%29%7B%24%28this%29.after%28%27%20%3Ca%20href%3D%22http%3A//bl.ocks.org/%27%2Ba%5B1%5D%2B%27%22%3E%5Bbl.ocks.org%5D%3C/a%3E%27%29%7D%7D%29%3B%7D%29%3B%0A
[extension]: http://github.com/downloads/jasondavies/bl.ocks.chrome/bl.ocks.chrome.crx

Developers
----------

The bookmarklet source is in `bl.ocks.bookmarklet.min.js`.

To package the Google Chrome extension, visit <chrome://extensions/> and click
on 'Developer mode'.  Then click 'Pack extension...' and select the
`bl.ocks.chrome` directory.  This will create a file called
`bl.ocks.chrome.crx` that you can open in Google Chrome and install.  Once
installed, it will add the links automatically to any page you visit.
