# Exercises for chapter 3:

# Name: John Wei

# 1

# repeat_lyrics()
# def print_lyrics():
#     print "I'm a lumberjack, and I'm okay."
#     print "I sleep all night and I work all day."

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# it doesnt work because you are calling the function before its defined

# 2

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# def print_lyrics():
#     print "I'm a lumberjack, and I'm okay."
#     print "I sleep all night and I work all day."

# repeat_lyrics()
# no change

# 3

# def right_justify(s):
#   columns =  70
#   word_length = len(s)
#   justified_word = (columns - word_length)* ' ' + s
#   print justified_word

# right_justify('blllgggaahh')
# remember it is the last letter that needs to be at col 70

#4

# def do_twice(f,value):
#     f(value)
#     f(value)

# def print_spam(value):
#     print value

# do_twice(print_spam, 'spam!')

# def print_twice(a):
#   do_twice(print_spam,a)

# print_twice('hotdogs!')

#5

def draw_h():
  line = '+ - - - - + - - - - +'
  print line

def draw_v():
  col = '|         |         |'
  print col

def draw_square():
  draw_h()
  draw_v()
  draw_v()
  draw_v()
  draw_v()
  draw_h()
  draw_v()
  draw_v()
  draw_v()
  draw_v()
  draw_h()

draw_square()