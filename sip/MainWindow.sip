%Module PyQtHybrid 0
%Import QtGui/QtGuimod.sip
%If (Qt_4_2_0 -)

class MainWindow : QMainWindow {
%TypeHeaderCode
#include "../MainWindow.h"
%End
public:
    MainWindow();
    virtual ~MainWindow();

signals:
    void runPythonCode(QString);

private slots:
    void runPythonCode();

public:
    QGraphicsView * viewer;
    QGraphicsScene * scene;
    QPlainTextEdit * editor;
    QPushButton * pb_commit;
};

%End
