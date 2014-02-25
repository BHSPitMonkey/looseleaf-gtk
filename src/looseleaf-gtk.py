#!/usr/bin/python
import sys

from gi.repository import Gtk, Gio, WebKit


class LooseleafApp(Gtk.Application):
    """Defines our custom GtkApplication"""

    class MainWindow(Gtk.Window):
        """Defines our Main Window UI"""

        def __init__(self):
            Gtk.Window.__init__(self,
                                title="Notes - Looseleaf",
                                type=Gtk.WindowType.TOPLEVEL)
            self.set_size_request(800, 600)

            # Set up a layout box
            hbox = Gtk.Box(spacing=6)
            self.add(hbox)
            
            # Set up our file browser tree data store
            self.tree_store = Gtk.TreeStore(str)
            dir1 = self.tree_store.append(None, ["School"])  # TODO
            dir2 = self.tree_store.append(None, ["Work"])  # TODO
            self.tree_store.append(dir1, ["Schedule.md"])  # TODO
            self.tree_store.append(dir1, ["CSCE 4010.md"])  # TODO
            self.tree_store.append(dir2, ["Migration Project.md"])  # TODO
            
            # Set up left sidebar (file browser tree)
            treeview = Gtk.TreeView(self.tree_store)
            treeview.set_headers_visible(False)
            treeview.expand_all()
            hbox.pack_start(treeview, True, True, 0)
            
            # Configure how the tree view displays
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(None, renderer, text=0)
            treeview.append_column(column)
            
            # Set up our WebView
            self.webview = WebKit.WebView()
            self.webview.load_string("<h1>Hello, World!</h1>", "text/html", "UTF-8", "")
            hbox.pack_start(self.webview, True, True, 0)
            
        def on_button1_clicked(self, widget):
            print("Hello")

        def on_button2_clicked(self, widget):
            print("Goodbye")

        def on_button_clicked(self, widget):
            print("Hello World")

    def __init__(self):
        """Constructor for our GtkApplication"""
        Gtk.Application.__init__(self, application_id="apps.test.helloworld",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def on_activate(self, data=None):
        """Called when the "activate" signal is received"""
        window = self.MainWindow()
        window.show_all()
        self.add_window(window)

    def on_window_close(self, event=None, something=None):
        # TODO: Teardown
        pass


def main(argv):
    """Entry point for the application"""
    app = LooseleafApp()
    return app.run(argv)

if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Handle CTRL-C correctly
    main(sys.argv)
