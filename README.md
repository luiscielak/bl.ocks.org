bl.ocks.org Google Chrome extension and bookmarklet
===================================================

This is a simple bookmarklet/Google Chrome extension that finds [Gist][1] links
in the current page and appends a link to the corresponding [bl.ock][2].

[1]: http://gist.github.com/
[2]: http://bl.ocks.org/

Installation
------------

To install the bookmarklet, simply add the contents of
`bl.ocks.bookmarklet.min.js` as a bookmark to your Web browser, and click
whenever you want to insert the links.

To package the Google Chrome extension, visit <chrome://extensions/> and click
on 'Developer mode'.  Then click 'Pack extension...' and select the
`bl.ocks.chrome` directory.  This will create a file called
`bl.ocks.chrome.crx` that you can open in Google Chrome and install.  Once
installed, it will add the links automatically to any page you visit.
