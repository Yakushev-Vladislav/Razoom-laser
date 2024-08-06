from custom_hovertip import CustomTooltipLabel


class BindEntry:
    def __init__(self, widget, text='-'):
        """
        Класс, реализующий установку фонового текста в поля ввода.
        :param widget: Виджет, на который устанавливается фоновый текст.
        """
        self.text = text
        self.widget = widget
        self.not_use_child = None
        self.to_add_entry_child()

        self.widget.bind('<FocusIn>', self.erase_entry_child)
        self.widget.bind('<FocusOut>', self.to_add_entry_child)

    def to_add_entry_child(self, event=None):
        if self.widget.get() == "":
            self.widget.insert(0, self.text)
            self.widget.config(foreground='grey')
        self.not_use_child = event

    def erase_entry_child(self, event=None):
        if self.widget.get() == self.text:
            self.widget.delete(0, 'end')
            self.widget.config(foreground='black')
        self.not_use_child = event


class BalloonTips:
    def __init__(self, widget, text=None):
        """
        Класс реализующий подсказки к элементам интерфейса
        :param widget: Виджет, на который устанавливается подсказка.
        :param text: Текст, который выводится при наведении на виджет.
        """
        # A80000 - Яркий контрастный цвет
        # eeeeee - Серенький
        CustomTooltipLabel(anchor_widget=widget,
                           text=text,
                           background="white",
                           foreground='grey',
                           relief='flat'
                           )
