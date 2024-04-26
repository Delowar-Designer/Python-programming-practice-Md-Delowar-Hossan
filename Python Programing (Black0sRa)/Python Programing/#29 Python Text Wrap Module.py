# Python Text Wrap Module
import textwrap
value = "Python Text Wrapping and Filling. In python the textwrap module is used is used to format and wrap plain"

# wrap_text = textwrap.fill(value,width=20)
# print(*wrap_text)

# wrap_text = textwrap.shorten(value,width=60,placeholder='....')
# print(wrap_text)

fill_text = textwrap.fill(value,width=20)
warp_text = textwrap.indent(fill_text,'$-- ',lambda line: True)
print(warp_text)