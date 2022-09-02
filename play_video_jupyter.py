# jupyter在线播放视屏
# ########## display
from IPython.display import display, HTML
p4 = "https://prod-streaming-video-msn-com.akamaized.net/9752d732-2354-483f-a678-a6d0cd2c22b7/1a5ed13a-43f5-4e85-95c8-6579065c4d7c.mp4"

html_str = '''<video controls width=\"480\" height=\"300\" src=\"{}\">animation</video>'''.format(p4)
# print(html_str)
display(HTML(html_str))
