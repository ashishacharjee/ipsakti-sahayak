import codecs
html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
# Let's find exactly this piece and remove the extra </div>
idx = html.find("tContent = val + '")
# The string looks like:
# tContent = val + ' • Prior Art Cross-Examination';
#         }
#       });
#     }
#   })();
# </script>
# </div><!-- /view-gazette -->

# Wait, if `</div><!-- /view-gazette -->` is the extra div...
# No, in `check_divs.py`:
# tag == '/div', if stack is empty, it prints.
# That means there is literally ONE extra </div> anywhere BEFORE that point, which causes the stack to be empty.
# If I delete `</div><!-- /view-gazette -->`, then the `/view-gazette` won't be closed!
# Wait! In `check_divs.py`, it prints "Extra closing div at char 52679".
# The characters at 52679 is exactly `</div><!-- /view-gazette -->`.
# Let's find what is right before it!
