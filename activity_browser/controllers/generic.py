# -*- coding: utf-8 -*-
import pickle
from PySide2.QtCore import QObject, Slot

from activity_browser.signals import signals
from activity_browser.utils import savefilepath


class GenericController(QObject):
    """A controller for any task that is not specific to projects, databases, activities, exchanges, etc."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = parent

        signals.export_as_pickle.connect(self.export_as_pickle)

    @Slot(str, name="exportAsPickle")
    def export_as_pickle(self, objects: list = None, filename: str = 'pickled_data') -> None:
        """Export any object as pickle."""
        if not objects:
            raise ValueError('No data provided for export as pickle.')

        filepath = savefilepath(default_file_name=filename, file_filter="Pickle (*.pkl)")

        with open(filepath, 'wb') as outp:  # Overwrites any existing file.
            pickle.dump(objects, outp, pickle.HIGHEST_PROTOCOL)

