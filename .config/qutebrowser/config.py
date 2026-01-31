config.load_autoconfig(False)
config.set('content.cookies.accept', 'never', 'chrome-devtools://*')
config.set('content.cookies.accept', 'never', 'devtools://*')
config.set('content.javascript.enabled', False, 'chrome-devtools://*')
config.set('content.javascript.enabled', False, 'devtools://*')
config.set('content.javascript.enabled', False, 'chrome://*/*')
config.set('content.javascript.enabled', False, 'qute://*/*')
c.url.default_page = 'about:blank'
c.url.searchengines = {
    'DEFAULT': 'https://search.brave.com/search?q={}',
    'aw': 'https://wiki.archlinux.org/?search={}', 
    'we': 'https://en.wikipedia.org/?search={}', 
    'ws': 'https://sv.wikipedia.org/?search={}', 
    'yt': 'https://youtube.com/results?search_query={}', 
    'ub' : 'https://gu-se-primo.hosted.exlibrisgroup.com/primo-explore/search?query=any,contains,{}&vid=46GUB_VU1&search_scope=default_scope&sortby=rank&lang=sv_SE',
    'r': 'https://old.reddit.com/search?q={}'
}
c.url.start_pages = 'about:blank'
c.colors.webpage.darkmode.enabled = True
config.bind('<Ctrl+o>', 'hint links spawn --detach mpv {hint-url}')
config.bind('ch', 'history-clear')
