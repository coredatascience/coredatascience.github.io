# parse markdown table
import datetime
import re

table = """\
|     1         |  03-Sep   | Introduction to course, R, RStudio, RMarkdown         |    HW1 Assigned    |
|      2        |  05-Sep   | Introduction to Git, GitHub, and homework submission  |           |
"""

# split table into rows
all_rows = table.split('\n')

# split rows into cells
table = [re.split('\s*\|\s*', row)[1:-1] for row in all_rows]

print(table)
md_file_template = """\
---
type: lecture
date: {date}
title: {title}
# tldr: ...
thumbnail: /static_files/lectures/placeholder.png
# links:
#     - url: https://github.com/coredatascience-fa23/BST219/blob/main/00_course_introduction/Lecture_01.pdf
#       name: lecture slides
hide_from_announcments: true
---
{content}
"""
for idx, date, title, note in table:
  # parse date of form "28-Aug" into "2023-08-28"
  date = datetime.datetime.strptime(
      date, '%d-%b').replace(year=2024).strftime('%Y-%m-%d')
  # set time to 09:45 AM
  date = date + ' 09:45:00'
  txt = md_file_template.format(date=date, title=title, content=note)
  # format filename into "lec01.md", "lec02.md", etc.
  filename = f'lec{idx.zfill(2)}.md'
  with open(f'{filename}', 'w') as f:
    f.write(txt)
