# coding: utf-8

# from __future__ import unicode_literals

# need sys if output to stderr.
import sys

# ⚠ Don't use relative imports
from yt_dlp.extractor.common import InfoExtractor

# ℹ️ If you need to import from another plugin
# from yt_dlp_plugins.extractor.example import ExamplePluginIE

# ℹ️ Instructions on making extractors can be found at:
# 🔗 https://github.com/yt-dlp/yt-dlp/blob/master/CONTRIBUTING.md#adding-support-for-a-new-site


# ⚠ The class name must end in "IE"
class SamplePluginIE(InfoExtractor):
    _WORKING = False
#    IE_DESC = False
    IE_NAME = 'sample'
    _VALID_URL = r'^sampleplugin:'

    def _real_extract(self, url):
        self.to_screen('URL "%s" successfully captured' % url)
#        print('error message.', file=sys.stderr) # not recommend
#        sys.stderr.write('error message\n') # not recommend
#        self._downloader.to_stderr('error message')
#        self._downloader.to_stdout('normal message')
        self.write_debug('debug message')# it's output if '--verbose' id used.
        self.report_warning(f'Unable to ....; {stderr.strip()}') # if warning
#        cookiefile = self._downloader.params.get('cookiefile')
        for ck in self.cookiejar:
            print(f"Name: {ck.name}, Value: {ck.value}, Domain: {ck.domain}, Path: {ck.path}
, Expires: {ck.expires}")
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        title = self._html_search_regex(
                (r'<title[^>]*>([^<]+?)</title>',
                 r'<meta\s+property="og:title"\s+content="([^"]+)"\s*/>',
                 r"<meta\s+property='og:title'\s+content='([^']+)'\s*/>"),
                webpage,'title', default=IE_NAME+' '+video_id, fatal=False, flags=re.IGNORECASE)
