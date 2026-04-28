import re
from utils import clean_title

def parse_caption(text):
 p=r'(.+?)\((\d{4})\).*?(1080p|720p)?.*?(x265|x264)?'
 m=re.search(p,text,re.I)
 if not m:
   return None
 t=m.group(1).strip()
 return {
 'title':t,
 'normalized_title':clean_title(t),
 'year':m.group(2),
 'quality':m.group(3) or '1080p',
 'codec':m.group(4) or 'x265'
 }
