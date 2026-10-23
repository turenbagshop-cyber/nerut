import os, sys
src = sys.argv[1]; out = sys.argv[2]
base = open(os.path.join(src, 'app/src/main/assets/index.html'), encoding='utf-8').read()
assert base.rstrip().endswith('</html>')
def variant(title, brand, mode, hide_tabs, extra_css=''):
    h = base.replace('<title>TURENLabs Editor</title>', '<title>%s</title>' % title, 1)
    h = h.replace('<span class="hide-m">TURENLabs Editor</span>', '<span class="hide-m">%s</span>' % brand, 1)
    css = '<style>%s %s</style>' % (' '.join('#tabs button[data-m="%s"]{display:none}' % t for t in hide_tabs), extra_css)
    js = ("<script>document.addEventListener('DOMContentLoaded',function(){try{window.__app.setMode('%s');}catch(e){console.error(e);}});</script>" % mode)
    return h.replace('</body>', css + js + '</body>', 1)
files = {
 'layout-editor/index.html': variant('Layout Editor – TURENLabs', 'Layout Editor', 'layout', ['rx3']),
 'rx3-editor/index.html': variant('RX3 Editor – TURENLabs', 'RX3 Editor', 'rx3', ['layout','links','code','assets','styles','big'], '#left,#right,#mobbar,#m-save,#b-undo,#b-redo{display:none!important}#body,#body.no-right{grid-template-columns:1fr!important}'),
}
for p, c in files.items():
    fp = os.path.join(out, p); os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, 'w', encoding='utf-8').write(c); print(p, len(c))
