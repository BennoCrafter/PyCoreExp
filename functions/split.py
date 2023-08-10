def split(txt, delimeter):
  final = []
  word = ""
  pos = 0
  while pos != len(txt):
    if txt[pos: pos + len(delimeter)] == delimeter:
          final.append(word)
          word = ""
          pos += len(delimeter)
          char = ""
    else:
      word += txt[pos]
      pos += 1
  final.append(word)
  return final 
