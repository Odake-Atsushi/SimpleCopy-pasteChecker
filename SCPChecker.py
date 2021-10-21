import re
import itertools
import PySimpleGUI as sg


def check(number, filename1, filename2, classification):
    conf_n = number  # 3
    # ファイル読み込み
    file1 = open(filename1, 'r', encoding='utf-8')
    file2 = open(filename2, 'r', encoding='utf-8')
    text1 = file1.read()
    text2 = file2.read()
    file1.close()
    file2.close()

    # チェック
    if classification == True:
        # text1_split = re.split(
        #     '\s',
        #     re.sub('[^a-zA-Z_0-9 ]', '', re.sub('\s+', ' ', text1.rstrip())))
        # text2_split = re.split(
        #     '\s',
        #     re.sub('[^a-zA-Z_0-9 ]', '', re.sub('\s+', ' ', text2.rstrip())))
        #######################################################
        text1_split = re.split('\s+', re.sub('[^\w\']+', ' ', text1).strip())
        text2_split = re.split('\s+', re.sub('[^\w\']+', ' ', text2).strip())
    else:
        # text1_split = re.split(
        #     '\s',
        #     re.sub('[^a-zA-Z_0-9 ]', '',
        #            re.sub('\s+', ' ', (text1.lower()).rstrip())))
        # text2_split = re.split(
        #     '\s',
        #     re.sub('[^a-zA-Z_0-9 ]', '',
        #            re.sub('\s+', ' ', (text2.lower()).rstrip())))
        #######################################################
        text1_split = re.split('\s+',
                               re.sub('[^\w\']+', ' ', text1.lower()).strip())
        text2_split = re.split('\s+',
                               re.sub('[^\w\']+', ' ', text2.lower()).strip())

    check_list = []
    check_count = 0

    for x, y in itertools.product(range(len(text1_split) - (conf_n - 1)),
                                  range(len(text2_split) - (conf_n - 1))):
        check_count = 0
        for i in range(conf_n):
            if text1_split[x + i] == text2_split[y + i]:
                check_count += 1
            if check_count >= conf_n:
                check_count = 0
                matched_list = []
                for j in range(conf_n):
                    matched_list.append(text1_split[x + j])
                check_list.append(matched_list)

    if len(check_list) == 0:
        check_list.append('該当なし')
    return (check_list)


def error_window(msg):
    error_layout = [[sg.Text(msg, key='error')],
                    [sg.Button('OK', key='ok', expand_x=True)]]
    sub_window = sg.Window('エラー',
                           error_layout,
                           modal=True,
                           keep_on_top=True,
                           auto_size_text=True)
    while True:
        sub_event, sub_value = sub_window.read()
        sub_window['error'].update(msg)
        if sub_event == sg.WIN_CLOSED:  #ウィンドウのXボタンを押したときの処理
            break
        if sub_event == 'ok':
            break
    sub_window.close()


sg.theme('Default')

main_layout = [[sg.Text('検証対象のファイルと連続単語数を指定してください')],
               [
                   sg.Text('ファイル1'),
                   sg.InputText('', key='inputFile1Path'),
                   sg.FileBrowse('ファイルを選択',
                                 target='inputFile1Path',
                                 file_types=(('テキストファイル', '*.txt'), ))
               ],
               [
                   sg.Text('ファイル2'),
                   sg.InputText('', key='inputFile2Path'),
                   sg.FileBrowse('ファイルを選択',
                                 target='inputFile2Path',
                                 file_types=(('テキストファイル', '*.txt'), ))
               ],
               [
                   sg.Text('連続単語数'),
                   sg.InputText('', size=(5, 1), key='inputNumber')
               ],
               [
                   sg.Text('大文字,小文字の区別'),
                   sg.Combo(('なし', 'あり'),
                            size=(5, 1),
                            default_value="なし",
                            key='distinction')
               ], [sg.Button('検索', key='check', expand_x=True)],
               [
                   sg.Text('検証結果'),
                   sg.Listbox([],
                              enable_events=True,
                              key='output_list',
                              expand_x=True,
                              expand_y=True)
               ]]

main_window = sg.Window('簡易コピペチェッカー',
                        main_layout,
                        resizable=True,
                        auto_size_buttons=True,
                        auto_size_text=True,
                        finalize=True)

main_window.set_min_size((550, 300))

while True:
    event, values = main_window.read()

    if event == sg.WIN_CLOSED:  #ウィンドウのXボタンを押したときの処理
        break

    if event == 'check':

        if not values['inputFile1Path']:
            error_window('ファイル１が選択されていません．')
        elif not values['inputFile2Path']:
            error_window('ファイル２が選択されていません．')
        elif not values['inputNumber']:
            error_window('連続単語数が入力されていません．')
        else:
            if values['distinction'] == 'あり':
                Large_and_small_distinction = True
            else:
                Large_and_small_distinction = False
            Answer = check(int(values['inputNumber']),
                           str(values['inputFile1Path']),
                           str(values['inputFile2Path']),
                           Large_and_small_distinction)
            main_window['output_list'].update(Answer)

main_window.close()