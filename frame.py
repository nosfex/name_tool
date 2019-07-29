import wx
import wx.lib.scrolledpanel as scrolled
from filewalker import Filewalker

class Framewalker(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None,wx.ID_ANY, "CHULIO CHECK", size=wx.Size(600,400))
        self.dialog = wx.DirDialog(None, "Choose a Directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        self.walker = None
        self.pass_text = []
        self.fail_text = []

        self.fail_panel, self.fail_scroller = self.add_panel_scroller(wx.Point(200, 10))
        self.pass_panel, self.pass_scroller = self.add_panel_scroller(wx.Point(0, 10))
        if self.dialog.ShowModal() == wx.ID_OK:
            self.walker = Filewalker(self.dialog.GetPath())

        self.fail_sizer = None
        self.pass_sizer = None
        if self.walker:
            for file in self.walker.passing_files:
                self.pass_text.append( wx.StaticText(self.pass_scroller, id=wx.ID_ANY, label=file, pos=wx.Point(0,0 )))
                if self.pass_sizer is None:
                    self.pass_sizer = self.expanded(self.pass_text[-1])
                else:
                    self.pass_sizer.Add(self.pass_text[-1], proportion=0)

            for file in self.walker.failing_files:
                self.fail_text.append( wx.StaticText(self.fail_scroller, id=wx.ID_ANY, label=file, pos=wx.Point(0,0 )))
                if self.fail_sizer is None:
                    self.fail_sizer = self.expanded(self.fail_text[-1])
                else:
                    self.fail_sizer.Add(self.fail_text[-1], proportion=0)

        if len(self.fail_text) > 0:
            self.fail_scroller.SetSizerAndFit(self.fail_sizer)
            self.fail_sizer.AddSpacer(10)

            fail_panel_sizer = self.expanded(self.fail_scroller)
            fail_panel_sizer.SetDimension(0, 0, 300, 300)
            self.fail_panel.SetSizerAndFit(fail_panel_sizer)

        if len(self.pass_text) > 0:
            self.pass_scroller.SetSizerAndFit(self.pass_sizer)
            self.pass_sizer.AddSpacer(10)
            pass_panel_sizer = self.expanded(self.pass_scroller)
            self.pass_panel.SetSizerAndFit(pass_panel_sizer)

    def add_panel_scroller(self, panel_pos=wx.Point(0,0)):
        panel = wx.Panel(self, id=wx.ID_ANY, pos=panel_pos)
        scroller = scrolled.ScrolledPanel(panel, -1, style = wx.TAB_TRAVERSAL | wx.SUNKEN_BORDER, name="ScrollPanel")
        scroller.SetAutoLayout(1)
        scroller.SetupScrolling()
        return panel, scroller

    def setup_sizer_panel(self, scroller, panel, scroller_sizer, panel_sizer):
        scroller.SetSizerAndFit(scroller_sizer)
        panel_sizer.AddSpacer(10)
        panel.SetSizerAndFit(panel_sizer)
        return scroller, panel_sizer, panel

    def fill_panel_data(self, scroller, files, sizer, text_list):
        for file in files:
            text_list.append( wx.StaticText(scroller, id=wx.ID_ANY, label=file, pos=wx.Point(0,0 )))
            if sizer is None:
                sizer = self.expanded(text_list[-1])
            else:
                sizer.Add(text_list[-1])
        return sizer, text_list

    def expanded(self, widget, padding = 30, flag =wx.VERTICAL):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(widget, proportion=0)
        return sizer
