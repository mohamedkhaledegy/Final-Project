from PySide2 import QtWidgets as qtw

def set_circle_design(self):
    self.frame_1_circle_progres = self.findChild(qtw.QWidget,"widget_square_1")
    self.frame_2_circle_progres = self.findChild(qtw.QWidget,"widget_square_2")
    self.frame_3_circle_progres = self.findChild(qtw.QWidget,"widget_square_3")
    self.frame_4_circle_progres = self.findChild(qtw.QWidget,"widget_square_4")
    self.frame_1_circle_progres.hide()
    self.frame_2_circle_progres.hide()
    self.frame_3_circle_progres.hide()
    self.frame_4_circle_progres.hide()
    
    self.frame_1_circle_progres.rpb_setBarStyle("Pie")
    self.frame_2_circle_progres.rpb_setBarStyle("Pizza")
    self.frame_3_circle_progres.rpb_setBarStyle("Donet")
    self.frame_4_circle_progres.rpb_setBarStyle("Hybrid2")
    self.frame_1_circle_progres.rpb_setLineWidth(10)
    self.frame_2_circle_progres.rpb_setLineWidth(12)
    self.frame_3_circle_progres.rpb_setLineWidth(15)
    self.frame_4_circle_progres.rpb_setLineWidth(20)
    self.frame_4_circle_progres.rpb_setLineCap('RoundCap')
    self.frame_3_circle_progres.rpb_setLineCap('RoundCap')
    self.frame_2_circle_progres.rpb_setLineCap('RoundCap')
    self.frame_1_circle_progres.rpb_setLineCap('RoundCap')
    
def reset_circle_val(self):
    self.frame_1_circle_progres.rpb_setValue(0)
    self.frame_2_circle_progres.rpb_setValue(0)
    self.frame_3_circle_progres.rpb_setValue(0)
    self.frame_4_circle_progres.rpb_setValue(0)
    self.frame_3_circle_progres.rpb_setLineCap('RoundCap')
    self.frame_2_circle_progres.rpb_setLineCap('RoundCap')