# -*- coding: utf-8 -*-
import brightway2 as bw
from PyQt5 import QtWidgets

from .. import activity_cache
from ..tabs import ActivityTab, CFsTab
from ..utils import get_name
from ...signals import signals
from ...settings import user_project_settings


class Panel(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super(Panel, self).__init__(parent)
        self.setMovable(True)

    def select_tab(self, obj):
        self.setCurrentIndex(self.indexOf(obj))


class MethodsPanel(Panel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.tab_dict = {}
        signals.method_selected.connect(self.open_method_tab)
        signals.project_selected.connect(self.close_all)

    def open_method_tab(self, method):
        if method not in self.tab_dict:
            tab = CFsTab(self, method)
            full_tab_label = ' '.join(method)
            label = full_tab_label[:min((10, len(full_tab_label)))] + '..'
            self.tab_dict[method] = tab
            self.addTab(tab, label)
        else:
            tab = self.tab_dict[method]

        self.select_tab(tab)
        signals.method_tabs_changed.emit()

    def close_tab(self, index):
        tab = self.widget(index)
        del self.tab_dict[tab.method]
        self.removeTab(index)
        signals.method_tabs_changed.emit()

    def close_all(self):
        self.clear()
        self.tab_dict = {}
        signals.method_tabs_changed.emit()


class ActivitiesPanel(Panel):
    def __init__(self, parent=None):
        super(Panel, self).__init__(parent)
        self.side = 'activities'
        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)

        signals.open_activity_tab.connect(self.open_activity_tab)
        signals.activity_modified.connect(self.update_activity_name)
        signals.project_selected.connect(self.close_all_activity_tabs)

    def update_activity_name(self, key, field, value):
        if key in activity_cache and field == 'name':
            try:
                index = self.indexOf(activity_cache[key])
                self.setTabText(index, value)
            except:
                pass

    def open_activity_tab(self, side, key):
        # check if it's open already and go to it if it is
        # check if the activity is found in settings file as editable (default read_only)

        # whilst WIP: use a placeholder to simulate a file.
        # for testing, editable activities are first two Forwast, names:
        # 100 Health and social work, EU27
        # 100 Waste treatment, Biogasification of food waste, DK
        a = user_project_settings.settings
        print("settings:\n", a)
        read_only_file_placeholder = {'writable-activities': [('forwast', '1099994b5fb9dec17ce78eb9aa8fd66f'),
                                                              ('forwast', '04569c83a5f561672dfb0e41b4636a67')]
                                      }
        read_only_db_placeholder = {'writable-databases': ['forwast',
                                                           'foo']
                                    }
        if side == self.side:
            if key in activity_cache:
                self.select_tab(activity_cache[key])
            else:
                db_read_only = True
                writable_dbs = read_only_db_placeholder['writable-databases']
                if key[0] in writable_dbs:
                    db_read_only = False

                # activity can only be editable if db is, so only check if this is the case.
                act_read_only = True
                if not db_read_only:
                    editable_acts = read_only_file_placeholder['writable-activities']
                    if key in editable_acts:
                        act_read_only = False

                new_tab = ActivityTab(self, activity_key=key, read_only=act_read_only, db_read_only=db_read_only)
                activity_cache[key] = new_tab
                self.addTab(new_tab, get_name(bw.get_activity(key)))
                self.select_tab(new_tab)
            signals.activity_tabs_changed.emit()

    def close_tab(self, index):
        widget = self.widget(index)
        if isinstance(widget, ActivityTab):
            assert widget.activity in activity_cache
            del activity_cache[widget.activity]
        widget.deleteLater()
        self.removeTab(index)
        signals.activity_tabs_changed.emit()

    def close_all_activity_tabs(self):
        open_tab_count = len(activity_cache)
        for i in reversed(range(open_tab_count)):
            self.close_tab(i)