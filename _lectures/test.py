# parse markdown table
import datetime
import re

table = """\
|     1         |  28-Aug   | Introduction to course, R, RStudio, RMarkdown         |                       |
|      2        |  30-Aug   | Introduction to Git, GitHub, and homework submission  | HW1 Assigned          |
|      3        |   4-Sep   | Labor Day - No Class                                  |                       |
|      4        |   6-Sep   | Basic R, data types and vectors                       |                       |
|      5        |  11-Sep   | Sorting, vector arithmetic, and indexing              |                       |
|      6        |  13-Sep   | Basic data wrangling                                  |                       |
|      7        |  18-Sep   | Basic plots and importing data                        |                       |
|      8        |  20-Sep   | Programming basics                                    | HW2 Assigned          |
|      9        |  25-Sep   | Introduction to ggplot2                               |                       |
|      10       |  27-Sep   | Gapminder                                             |                       |
|      11       |   2-Oct   | Maps and infographic                                  |                       |
|      12       |   4-Oct   | Data visualization principles                         |                       |
|      13       |   9-Oct   | Indigenous People’s Day - No Class                    |                       |
|      14       |  11-Oct   | Data visualization principles - continued             | HW3 Assigned          |
|      15       |  16-Oct   | Advanced data wrangling                               |                       |
|      16       |  18-Oct   | Advanced data wrangling - continued                   |                       |
|      17       |  23-Oct   | Date and times, web scraping                          |                       |
|      18       |  25-Oct   | String processing                                     |                       |
|      19       |  30-Oct   | Regression                                            |                       |
|      20       |   1-Nov   | Regression - continued                                |                       |
|      21       |   6-Nov   | Introduction to machine learning                      | HW4 Assigned          |
|      22       |   8-Nov   | Machine learning - continued                          |                       |
|      23       |  13-Nov   | Machine learning - continued                          |                       |
|      24       |  15-Nov   | Machine learning - continued                          |                       |
|      25       |  20-Nov   | Machine learning - continued                          |                       |
|      26       |  22-Nov   | Thanksgiving Recess - No Class                        |                       |
|      27       |  27-Nov   | Machine learning - continued                          |                       |
|      28       |  30-Nov   | Machine learning - continued                          |                       |
|      29       |   4-Dec   | Machine learning - continued                          |                       |
|      30       |   6-Dec   | Introduction to Shiny                                 |                       |
|      31       |  11-Dec   | Shiny - continued                                     |                       |
|      32       |  13-Dec   | Shiny - continued Next steps in data science          | Final project due     |"""

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
      date, '%d-%b').replace(year=2023).strftime('%Y-%m-%d')
  # set time to 11:30 AM
  date = date + ' 11:30:00'
  txt = md_file_template.format(date=date, title=title, content=note)
  # format filename into "lec01.md", "lec02.md", etc.
  filename = f'lec{idx.zfill(2)}.md'
  with open(f'{filename}', 'w') as f:
    f.write(txt)
