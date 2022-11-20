import re

html = input()
title_information_pattern = r"<title>.*?<\/title>"
content_information_pattern = r"<body>.*?<\/body>"

valid_information_pattern = r"(?<=>).*?(?=<)"

title_information = re.search(title_information_pattern, html).group()
delete_this_for_title = re.sub(r"\\n", "", title_information)
title = "".join(re.findall(valid_information_pattern, delete_this_for_title))

content_information = re.search(content_information_pattern, html).group()
delete_this_for_content = re.sub(r"\\n", "", content_information)
content = "".join(re.findall(valid_information_pattern, delete_this_for_content))

print(f"""Title: {title}
Content: {content}""")
