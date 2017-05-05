# References:
# http://johnnado.com/pyqt-qtest-example/
# In particular, see the BitBucket link on that page

import PyQt5.QtCore as QtCore
from PyQt5.QtTest import QTest
import PyQt5.QtGui as QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import Qt
import sys
import unittest

from viewer import ImageViewerWindow

# helper to simulate a mouse drag
def dragMouse(p1, p2, viewport, modifiers=Qt.NoModifier):
    QTest.mousePress(viewport, Qt.LeftButton, pos=p1, modifier=modifiers)

    # Fake a mouseMove manually; QTest.mouseMove does not work
    event = QtGui.QMouseEvent(QtGui.QMouseEvent.MouseMove, p2, Qt.LeftButton, Qt.LeftButton, modifiers)
    QtCore.QCoreApplication.sendEvent(viewport, event)

    QTest.mouseRelease(viewport, QtCore.Qt.LeftButton, pos=p2, delay=100, modifier=modifiers)

app = QApplication(sys.argv)
class WindowTest(unittest.TestCase):
    def setUp(self):
        input_image = "angry_unicorn.png"
        image = QtGui.QImage()
        image.load(input_image)
        self.window = ImageViewerWindow(image, input_image)
        self.window.show()

        self.viewport = self.window.image_view.viewport()

    def test_doubleClick(self): pass

    def test_drag(self): pass

unittest.main()
