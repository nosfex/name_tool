import wx
import wx.lib.scrolledpanel as scrolled
from filewalker import Filewalker
from frame import Framewalker
def main():


    app = wx.App(False)
    frame = Framewalker()

    dialog = wx.DirDialog(None, "Choose a Directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

    frame.Layout()
    frame.Show(True)
    app.MainLoop()

def expanded(widget, padding = 30):
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(widget)
    return sizer
if __name__ == '__main__':
    main()
