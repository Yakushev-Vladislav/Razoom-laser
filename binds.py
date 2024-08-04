class BindEntry:
    def __init__(self, widget):
        self.widget = widget
        self.not_use_child = None
        self.to_add_entry_child()

        self.widget.bind('<FocusIn>', self.erase_entry_child)
        self.widget.bind('<FocusOut>', self.to_add_entry_child)

    def to_add_entry_child(self, event=None):
        if self.widget.get() == "":
            self.widget.insert(0, '-')
        self.not_use_child = event

    def erase_entry_child(self, event=None):
        if self.widget.get() == '-':
            self.widget.delete(0, 'end')
        self.not_use_child = event
