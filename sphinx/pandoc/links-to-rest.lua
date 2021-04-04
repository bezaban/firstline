function Link(el)
  el.target = string.gsub(el.target, "%.html", ".rst")
  return el
end
