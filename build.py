#!/usr/bin/env python

import os
import jinja2
import markdown

# Load the template that we want.
template = open("template.html", 'r').read()

def main():
	# Create the site directory.
	if not os.path.exists("_site"):
		os.makedirs("_site")
    # TODO: Make this compile more than just the index.
	for x in ["index.md"]:
		convert(x)

def convert(name):
	with open(name, "r") as infile:
		with open("_site/" + name[:-3] + ".html", "w") as outfile:
			# Specify input, settings.
			instring = infile.read()
			extensions = ['extra', 'smarty']
			# Compile and insert HTML.
			html = markdown.markdown(instring, extensions=extensions, output_format='html5')
			doc = jinja2.Template(template).render(content=html)
			# Write output and cleanup.
			outfile.write(doc)

if __name__ == '__main__':
    main()