config.load_autoconfig(False)
config.set('content.cookies.accept', 'never', 'chrome-devtools://*')
config.set('content.cookies.accept', 'never', 'devtools://*')
config.set('content.javascript.enabled', False, 'chrome-devtools://*')
config.set('content.javascript.enabled', False, 'devtools://*')
config.set('content.javascript.enabled', False, 'chrome://*/*')
config.set('content.javascript.enabled', False, 'qute://*/*')
c.url.default_page = 'about:blank'
c.url.searchengines = {
    'DEFAULT': 'https://searxng.site/searxng/?q={}', 
    'aw': 'https://wiki.archlinux.org/?search={}', 
    'w': 'https://en.wikipedia.org/?search={}', 
    'yt': 'https://youtube.com/results?search_query={}', 
    'ub' : 'https://gu-se-primo.hosted.exlibrisgroup.com/primo-explore/search?query=any,contains,{}&vid=46GUB_VU1&search_scope=default_scope&sortby=rank&lang=sv_SE',
    'r': 'https://old.reddit.com/r/{}'
}
c.url.start_pages = 'about:blank'
c.colors.webpage.darkmode.enabled = True
