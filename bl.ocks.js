var reGist = /^https?\:\/\/gist\.github\.com\/(\d*)/i,
    reRel = /^\/?(\d+)$/,
    gist = reGist.test(location.href),
    anchors = document.querySelectorAll("a"),
    anchor,
    image,
    i = -1,
    n = anchors.length,
    href,
    match;
while (++i < n) {
  match = (href = (anchor = anchors[i]).getAttribute("href")).match(reGist);
  if (gist && !(match && match[1])) match = href.match(reRel);
  if (match && match[1]) {
    anchor = anchor.appendChild(document.createElement("a"));
    anchor.setAttribute("href", "http://bl.ocks.org/" + match[1]);
    anchor.setAttribute("title", "View bl.ock #" + match[1] + ".");
    anchor.style.position = "relative";
    anchor.style.marginLeft = "2px";
    anchor.style.marginRight = "18px";
    image = anchor.appendChild(document.createElement("img"));
    image.setAttribute("src", safari.extension.baseURI + "bl.ocks.png");
    image.style.position = "absolute";
  }
}
