bl.ocks.org Google Chrome extension and bookmarklet
===================================================

This is a simple bookmarklet/Google Chrome extension that finds [Gist][1] links
in the current page and appends a link to the corresponding [bl.ock][2].

[1]: http://gist.github.com/
[2]: http://bl.ocks.org/

Installation
------------

To install the Google Chrome extension, download [bl.ocks.chrome.crx][extension].

To install the bookmarklet, add the contents of `bl.ocks.bookmarklet.min.js` as
a bookmark.

[extension]: http://github.com/downloads/jasondavies/bl.ocks.chrome/bl.ocks.chrome.crx

Developers
----------

To package the Google Chrome extension, visit <chrome://extensions/> and click
on 'Developer mode'.  Then click 'Pack extension...' and select the
`bl.ocks.chrome` directory.  This will create a file called
`bl.ocks.chrome.crx` that you can open in Google Chrome and install.  Once
installed, it will add the links automatically to any page you visit.
