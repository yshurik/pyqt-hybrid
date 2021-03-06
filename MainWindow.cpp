#include <QtGui>
#include "MainWindow.h"

MainWindow::MainWindow():QMainWindow(0L) {
    QSplitter * splitter = new QSplitter;
    setCentralWidget(splitter);

    QWidget * editorContent = new QWidget;
    splitter->addWidget(editorContent);

    QVBoxLayout * layout = new QVBoxLayout;
    editorContent->setLayout(layout);

    editor = new QPlainTextEdit;
    layout->addWidget(editor);

    pb_commit = new QPushButton(tr("Commit"));
    connect(pb_commit, SIGNAL(clicked()), this, SLOT(runPythonCode()));
    layout->addWidget(pb_commit);

    scene = new QGraphicsScene(this);
    viewer = new QGraphicsView;
    viewer->setScene(scene);
    splitter->addWidget(viewer);

    splitter->setSizes(QList<int>() << 400 << 600);
}

MainWindow::~MainWindow() {;}

void MainWindow::runPythonCode() {
    emit runPythonCode(editor->toPlainText());
}
