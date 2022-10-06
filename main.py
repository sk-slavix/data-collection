from parser.absparser import AbsParser
from excelGenerator.generatorXlsx import XlsxGenerator


parser = AbsParser()
parser.getData()

xlsxGenerator = XlsxGenerator()
xlsxGenerator.generateFile()

