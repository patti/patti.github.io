

files= 'bounding-boxes-and-benchmarking.html','hello-world.html','index.html'
for file in files:
	file = 'output/blog/'+file
	lines = open(file).readlines()
	outfile = open(file[:-5]+'.html','w')
	for i,line in enumerate(lines):
		if i==1:
			for s in ['<script>','code_show=true;','function code_toggle() {','if (code_show){',\
				'$(\'div.input\').hide();','$(\'div.prompt\').hide();','} else {','$(\'div.input\').show();',\
				'}','code_show = !code_show','}','</script>']: 
				outfile.write(s+'\n')
		if "<body" in line: line = line.replace('body','body onload=code_toggle()')
		outfile.write(line)
	outfile.close()