def clean_title(t):
 junk=['1080p','720p','x265','x264']
 t=t.lower()
 for j in junk:
   t=t.replace(j,'')
 return ' '.join(t.split())
