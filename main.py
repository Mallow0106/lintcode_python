
import argparse
import os

lintcode_parser = argparse.ArgumentParser(description='lintcode debugging tool')
lintcode_parser.add_argument('q', help='question number')


args = lintcode_parser.parse_args()
if args.q is not None:
    module_name = 'lintcode{0}'.format(args.q)
    datainput = "lintcode{0}_datainput".format(args.q)

lintcode = __import__(module_name)
inputs = []
if os.path.isfile(datainput):
    with open(datainput, 'r') as f:
        for line in f:
            inputs.append(line)

solver = lintcode.Solution()
for output in solver.solve(inputs):
    print output
    print


