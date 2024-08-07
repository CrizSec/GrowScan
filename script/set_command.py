from PyQt5.QtCore import QProcess

def command(*radio_buttons, target_input=None, thread_combox=None, script_combox=None, additional_combox=None, output_line=None, result_text=None):
    target = target_input.text() if target_input else ''
    option = []
    output = ''
    
    for radio_button in radio_buttons:
        if radio_button.isChecked():
            option.append(radio_button.text())

    if thread_combox:
        combox = thread_combox.currentText()
        if combox == 'Select Option':
            option.append('')
        else:
            option.append(f'-{combox}')

    if additional_combox:
        combox = additional_combox.currentText()
        if combox == 'Select Option':
            option.append('')
        else:
            option.append(f'{combox}')

    if script_combox:
        combox = script_combox.currentText()
        if combox == 'Select Option':
            option.append('')
        else:
            option.append(f'--script {combox}')

    if output_line:
        combox = output_line.text()
        if combox == '':
            output = ''
        else:
            output = f' -oN {combox}'

    clean_option = [item for item in option if item]
    options = ' '.join(clean_option)

    nmap_command = f'nmap {options} {target}{output}'
    process = QProcess()
    process.setProcessChannelMode(QProcess.MergedChannels)
    process.readyRead.connect(lambda: read_output(process, result_text))
    process.start(nmap_command)
    
    return process

def read_output(process, result_text):
    data = process.readAllStandardOutput()
    result_text.moveCursor(result_text.textCursor().End)
    result_text.insertPlainText(data.data().decode())