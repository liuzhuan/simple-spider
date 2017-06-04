# coding: utf8

class HtmlOutputer(object):
    
    def __init__(self, output = 'output.html'):
        self.datas = []
        self.output = output

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open(self.output, 'w')
        fout.write('<html>')
        fout.write('<style>table, td { border: 1px solid #ccc; border-collapse: collapse; } </style>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td><a href="%s" target="_blank">%s</a></td>' % (data['url'], data['title']))
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()