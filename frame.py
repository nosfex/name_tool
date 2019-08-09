import wx
import wx.lib.scrolledpanel as scrolled
import webbrowser
import subprocess
from load_function import parse
from filewalker import Filewalker

class MainFrame(wx.Frame):

    def __init__(self, filewalker: Filewalker):
        wx.Frame.__init__(self, None, wx.ID_ANY, "CHULIO CHECK", size=wx.Size(600, 400))
        self.filewalker = filewalker
        self.SetMenuBar(MenuBar(self))
        self.pass_panel = TextPanel(self)
        self.fail_panel = TextPanel(self)
        self.sizer = wx.GridSizer(1, 2, 0, 0)
        self.sizer.Add(self.pass_panel, flag=wx.EXPAND)
        self.sizer.Add(self.fail_panel, flag=wx.EXPAND)
        self.SetSizer(self.sizer)

    def on_open_click(self, event):
        del event
        dialog = wx.DirDialog(None, "Choose a Directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        if dialog.ShowModal() == wx.ID_OK:
            self.pass_panel.clear()
            self.fail_panel.clear()
            self.filewalker.walk(dialog.GetPath())

            for file in self.filewalker.passing_files:
                self.pass_panel.add_element(file)
            self.pass_panel.render()

            for file in self.filewalker.failing_files:
                self.fail_panel.add_element(file)
            self.fail_panel.render()

    def on_quit_click(self, event):
        del event
        wx.CallAfter(self.Destroy)

    def on_load_filter(self, event):
        del event
        dialog = wx.FileDialog(None, "Choose a filter:", defaultDir="", defaultFile="", wildcard="*.json", style= wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            nomenclature_filter = parse(path, 'nomenclature_filter')
            self.filewalker = Filewalker(nomenclature_filter.file,
                                    nomenclature_filter.prefix,
                                    nomenclature_filter.suffix)


    def on_svn_open(self, event):
        del event
        process = subprocess.call('svn', shell=True)

    def on_help_box(self, event):
        del event

        help_box = wx.MessageBox('Contact: gerardo.heidel@ngdstudios.com', 'Helpful Message Box', wx.OK | wx.ICON_INFORMATION)

class MenuBar(wx.MenuBar):
    def __init__(self, parent, *args, **kwargs):
        super(MenuBar, self).__init__(*args, **kwargs)

        file_menu = wx.Menu()
        self.Append(file_menu, '&File')

        open_menu_item = wx.MenuItem(file_menu, wx.ID_OPEN)
        parent.Bind(wx.EVT_MENU, parent.on_open_click, id=wx.ID_OPEN)

        quit_menu_item = wx.MenuItem(file_menu, wx.ID_EXIT)
        parent.Bind(wx.EVT_MENU, parent.on_quit_click, id=wx.ID_EXIT)

        file_filter_item = wx.MenuItem(file_menu, wx.ID_ANY, "Filter" )
        parent.Bind(wx.EVT_MENU, parent.on_load_filter, file_filter_item)

        file_menu.Append(open_menu_item)
        file_menu.Append(quit_menu_item)
        file_menu.Append(file_filter_item)

        help_menu = wx.Menu()
        self.Append(help_menu, '&Help')

        help_item = wx.MenuItem(help_menu, wx.ID_ANY, "HelpBox")
        parent.Bind(wx.EVT_MENU, parent.on_help_box, help_item)

        help_menu.Append(help_item)

class TextPanel(scrolled.ScrolledPanel):
    def __init__(self, parent):
        super(TextPanel, self).__init__(parent, -1, style=wx.TAB_TRAVERSAL | wx.SUNKEN_BORDER, name="ScrollPanel")
        self.SetAutoLayout(1)
        self.SetupScrolling()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.AddSpacer(10)
        self.SetSizer(self.sizer)

    def add_element(self, text):
        element = Button(self, id=wx.ID_ANY, label=text.file, pos=wx.Point(0, 0), path=text.path)
        self.sizer.Add(element, proportion=0)

    def render(self):
        self.sizer.FitInside(self)

    def clear(self):
        self.sizer.Clear(True)
        self.sizer.FitInside(self)

class Button(wx.Button):
    def __init__(self, parent, id, label, pos, size=wx.Size(200, 20), style=0, validator=wx.Validator(), name="", path=None):
        super(Button, self).__init__(parent, id, label, pos, size, style, validator, name)
        self.path = path
        self.Bind(wx.EVT_BUTTON, self.on_text_ctrl_mouse_down)

    def on_text_ctrl_mouse_down(self, event):
        print("wtf")
        webbrowser.open('file:///' + self.path)
