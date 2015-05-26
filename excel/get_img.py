from pyxlchart import Pyxlchart
xl = Pyxlchart()
xl.WorkbookDirectory = "D:\\"
xl.WorkbookFilename = "chart_column.xlsx"
xl.SheetName = ""
#xl.ImageFilename = "MyChart1"
xl.ExportPath = "d:\\"
xl.ChartName = ""
xl.start_export()
