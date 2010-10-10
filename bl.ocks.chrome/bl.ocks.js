var gist_re = /^https?\:\/\/gist\.github\.com\/(\d*)/i,
    rel_re = /^\/?(\d+)$/,
    on_gist = gist_re.test(location.href);
$('a').each(function() {
  var href = $(this).attr('href'),
      m = href.match(gist_re);
  if (on_gist && !(m && m[1])) {
    m = href.match(rel_re);
  }
  if (m && m[1]) {
    $(this).after(' <a href="http://bl.ocks.org/' + m[1] + '">[bl.ocks.org]</a>');
  }
});
