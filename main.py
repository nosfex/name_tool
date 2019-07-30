import wx
from filewalker import Filewalker
from frame import MainFrame
from load_function import parse
def main():
    app = wx.App(False)

    nomenclature_filter = parse("file_filter.json", "nomenclature_filter")
    filewalker = Filewalker(nomenclature_filter.file, nomenclature_filter.prefix, nomenclature_filter.suffix)
    frame = MainFrame(filewalker)
    frame.Layout()
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
