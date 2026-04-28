from rapidfuzz import process

def best_match(query,choices):
 r=process.extractOne(query,choices)
 return r[0] if r else None
