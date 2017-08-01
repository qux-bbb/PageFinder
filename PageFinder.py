# coding:utf8

#简单目录、页面爆破

import sys
import requests
from optparse import OptionParser


def crack(url, web_type):
	result = ""
	dic = open("dic/" + web_type + ".txt", 'r').read().split("\n")
	dic_len = len(dic)
	for i in range(dic_len):
		aurl = url + dic[i]
		res = requests.get(aurl, allow_redirects=False, timeout = 1)
		if res.status_code == 200:
			sys.stdout.write("%-70s\n"%aurl)  # %-70s输出以覆盖进度条
			result += aurl + "\n"
		# 输出进度
		sch_bar = '#'*(int((float(i+1)/dic_len)*40))
		sys.stdout.write("Schedule: [%-40s]%d/%d\r"%(sch_bar, i + 1, dic_len))

	open("result.txt","w").write(result)
	sys.stdout.write("\nDone! The result saved in result.txt")


if __name__ == '__main__':

	parser = OptionParser(
        "Usage:    python PageFinder.py [options]\nExample:  python PageFinder.py -u http://hello.com/hello -t php")
	parser.add_option(
        "-u", "--url", dest="url", help="a base url")
	parser.add_option(
        "-t", "--type", dest="web_type", help="web page type, like: php asp jsp html")
	(options, args) = parser.parse_args()

	url = options.url
	web_type = options.web_type

	if url == None or web_type == None:
		parser.print_help()
		exit(0)

	crack(url, web_type)