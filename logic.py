from PyQt6.QtWidgets import *
from gui import *
from csv import *
import formulas


class Logic(QMainWindow, Ui_window):
    '''
    Class to conatian the logic for the user interface
    '''

    def __init__(self) -> None:
        '''
        Method to set the inital positions of widgets, values of variables, and connect buttons to functions
        '''
        super().__init__()

        self.setupUi(self)
        self.distanceUi()
        self.fileUi()
        self.__fileName = ''
        self.dropDownDelimiter.setCurrentIndex(1)

        self.buttonSubmit.clicked.connect(lambda : self.submit())
        self.buttonClear.clicked.connect(lambda : self.erase())
        self.radioManual.clicked.connect(lambda : self.manualUi())
        self.radioFile.clicked.connect(lambda : self.fileUi())
        self.buttonFile.clicked.connect(lambda : self.selectFile())
        self.dropDownOperation.currentIndexChanged.connect(lambda : self.distanceUi())
        self.dropDownDelimiter.currentIndexChanged.connect(lambda : self.distanceUi())
        self.dropDownPoints.currentIndexChanged.connect(lambda : self.distanceUi())

    def distanceUi(self) -> None:
        '''
        Method to change the layout of user interface to match the distance option
        '''
        if self.dropDownOperation.currentIndex() == 9:
            for i in range(4):
                self.dropDownPoints.view().setRowHidden(i, False)
                self.dropDownDelimiter.view().setRowHidden(i, False)
            self.dropDownPoints.view().setRowHidden(self.dropDownDelimiter.currentIndex(), True)

            if self.dropDownDelimiter.currentIndex() == self.dropDownPoints.currentIndex():
                self.dropDownPoints.setCurrentIndex((self.dropDownDelimiter.currentIndex() + 1) % 4)

            self.dropDownDelimiter.view().setRowHidden(self.dropDownPoints.currentIndex(), True)
            
            self.dropDownPoints.show()
            self.labelPoints.show()
        else:
            self.dropDownPoints.hide()
            self.labelPoints.hide()
            for i in range(4):
                self.dropDownDelimiter.view().setRowHidden(i, False)
    
    def manualUi(self) -> None:
        '''
        Method to change the layout of user interface to match the manual input option
        '''
        self.buttonFile.hide()
        self.labelFile.hide()
        self.inputList.show()

    def fileUi(self) -> None:
        '''
        Method to change the layout of user interface to match the file input option
        '''
        self.inputList.hide()
        self.buttonFile.show()
        self.labelFile.show()

    def selectFile(self) -> None:
        '''
        Method to cleanse the input of choosing a file
        '''
        try:
            temp = self.fileSelector.getOpenFileName(caption = 'Open file', filter = "Text files (*.txt *.csv)")[0]
            tempFile = open(temp)

            charIndex = len(temp) - 1
            while(temp[charIndex] != '/'):
                charIndex -= 1
            shortHandFileName = temp[(charIndex + 1):]

            self.labelFile.setText(f'Current File:\n{shortHandFileName}')
            self.__fileName = temp
            tempFile.close()

        except:
            if self.__fileName != '':
                charIndex = len(self.__fileName) - 1
                while(self.__fileName[charIndex] != '/'):
                    charIndex -= 1
                shortHandFileName = self.__fileName[(charIndex + 1):]
            else:
                shortHandFileName = 'None'

            self.labelFile.setText(f'Could not Open File\nCurrent File:\n{shortHandFileName}')
        
    def submit(self) -> None:
        '''
        Method to check inputs and give the result of the selected values
        '''
        
        if self.dropDownDelimiter.currentIndex() == 0:
            delimiter = ','
        elif self.dropDownDelimiter.currentIndex() == 1:
            delimiter = '\n'
        elif self.dropDownDelimiter.currentIndex() == 2:
            delimiter = ';'
        elif self.dropDownDelimiter.currentIndex() == 3:
            delimiter = ' '
        
        if self.dropDownOperation.currentIndex() == 0:
            operation = 'addition'
        elif self.dropDownOperation.currentIndex() == 1:
            operation = 'subtraction'
        elif self.dropDownOperation.currentIndex() == 2:
            operation = 'multiplication'
        elif self.dropDownOperation.currentIndex() == 3:
            operation = 'division'
        elif self.dropDownOperation.currentIndex() == 4:
            operation = 'expontent'
        elif self.dropDownOperation.currentIndex() == 5:
            operation = 'gcd'
        elif self.dropDownOperation.currentIndex() == 6:
            operation = 'min'
        elif self.dropDownOperation.currentIndex() == 7:
            operation = 'max'
        elif self.dropDownOperation.currentIndex() == 8:
            operation = 'mean'
        elif self.dropDownOperation.currentIndex() == 9:
            operation = 'distance'

        if self.radioManual.isChecked():
            if self.inputList.toPlainText() == '':
                self.labelOutput.setText('Please input list')
                return
            list = self.inputList.toPlainText().strip().split(sep = delimiter)
        
        elif self.radioFile.isChecked():
            try:
                inputFile = open(self.__fileName)
                contents = inputFile.read().strip()
                inputFile.close()
                if contents == '':
                    self.labelOutput.setText('The entered file is empty')
                    return
                list = [item for item in contents.split(sep = delimiter)]

            except:
                self.labelOutput.setText('Please select input file')
                return
        
        if operation != 'distance' and operation != 'gcd':
            try:
                newList = []
                for item in list:
                    item.strip()
                    if not (item.isspace() or item == ''):
                        newList.append(float(item))
            except:
                self.labelOutput.setText(f"Inputs for {operation} must be numbers")
                return
        elif operation == 'gcd':
            try:
                newList = []
                for item in list:
                    item.strip()
                    if not (item.isspace() or item == ''):
                        newList.append(int(item))
            except:
                self.labelOutput.setText(f"Inputs for greatest common demoninator\nmust be integers")
                return

        else:
            if self.dropDownPoints.currentIndex() == 0:
                pointDelimiter = ','
            elif self.dropDownPoints.currentIndex() == 1:
                pointDelimiter = '\n'
            elif self.dropDownPoints.currentIndex() == 2:
                pointDelimiter = ';'
            elif self.dropDownPoints.currentIndex() == 3:
                pointDelimiter = ' '

            try:
                newList = []
                numEmptySlots = 0
                for i in range(len(list)):
                    if list[i] == '' or list[i].isspace():
                        numEmptySlots += 1
                        continue
                    list[i] = list[i].split(sep = pointDelimiter)
                    newList.append([])

                    if len(list[i]) != len(list[0]):
                        raise IndexError
                    
                    for j in range(len(list[i])):
                        if not (list[i][j].isspace() or list[i][j] == ''):
                            newList[i - numEmptySlots].append(float(list[i][j].strip()))

            except IndexError:
                self.labelOutput.setText(f"Inputs for distence must be the same size")
                return
            except ValueError:
                self.labelOutput.setText(f"Inputs for distence must all be numbers")
                return
        
        if operation == 'addition':
            result = formulas.add(newList)
        elif operation == 'subtraction':
            result = formulas.subtract(newList)
        elif operation == 'multiplication':
            result = formulas.multiply(newList)
        elif operation == 'division':
            if formulas.divide(newList) == None:
                self.labelOutput.setText('Cannot Divide by Zero')
                return
            else:
                result = formulas.divide(newList)
        elif operation == 'expontent':
            try:
                result = formulas.exponentiate(newList)
            except OverflowError:
                self.labelOutput.setText('Result is too large')
                return
        elif operation == 'min':
            result = formulas.min(newList)
        elif operation == 'max':
            result = formulas.max(newList)
        elif operation == 'mean':
            result = formulas.mean(newList)
        elif operation == 'gcd':
            newList.sort()
            result = formulas.gcd(newList)
        elif operation == 'distance':
            result = formulas.totalDistance(newList)
        
        self.labelOutput.setText(f'Result: {result}')

    def erase(self) -> None:
        '''
        Method to reset the user interface to the default values
        '''
        self.inputList.clear()

        self.__fileName = ''

        self.radioManual.setChecked(False)
        self.radioFile.setChecked(True)

        self.labelFile.setText('')
        self.labelOutput.setText('')

        self.inputList.hide()
        self.buttonFile.show()

        self.dropDownDelimiter.setCurrentIndex(1)
        self.dropDownOperation.setCurrentIndex(0)
        self.dropDownPoints.setCurrentIndex(0)

        self.fileUi()
        self.distanceUi()